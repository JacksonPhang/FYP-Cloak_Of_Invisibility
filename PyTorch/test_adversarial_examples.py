import torch
from os.path import dirname, abspath
import torchvision.datasets
import torchvision.transforms as transforms
from torchvision.utils import save_image
from torch.utils.data import DataLoader
from torch.autograd import Variable
import models
from models import MNIST_target_net
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from resnet import CifarResNet
from resnet import BasicBlock

MAX_PERTURB_LEVEL = 100
MAX_SCALED_PERTURB_LEVEL = 2
relative_directory = dirname(abspath(__file__))
output_directory = relative_directory + "\\IO_images\\output_img.jpg"

use_cuda=True
loop = 30
# Define what device we are using
device = torch.device("cuda" if (use_cuda and torch.cuda.is_available()) else "cpu")
saved_state = [None,None,None] #saved state of input image, adv image and target model
output_state = [None,None,None] #saved state of input prediction label, output prediction label and output label list

def adversarial_attack(dataset, perturb_level, input_directory = None):
    if dataset == "cifar":
        image_nc = 3
        pretrained_model = relative_directory + "\\CIFAR100_target_model.pth"
        pretrained_generator_path = relative_directory + "\\models\\cifar_epoch_60.pth"
        target_model = CifarResNet(BasicBlock, [9, 9, 9]).to(device)
        size = 32
    else:
        image_nc = 1
        pretrained_model = relative_directory + "\\MNIST_target_model.pth"
        pretrained_generator_path = relative_directory + "\\models\\netG_epoch_60.pth"
        target_model = MNIST_target_net().to(device)
        size = 28
    batch_size = 128
    gen_input_nc = image_nc

    # load the pretrained model
    target_model.load_state_dict(torch.load(pretrained_model))
    target_model.eval()

    # load the generator of adversarial examples
    pretrained_G = models.Generator(gen_input_nc, image_nc).to(device)
    if torch.cuda.is_available():
        pretrained_G.load_state_dict(torch.load(pretrained_generator_path))
    else:
        pretrained_G.load_state_dict(torch.load(pretrained_generator_path, map_location=torch.device('cpu')))
    pretrained_G.eval()

    data_transforms = transforms.Compose([
        transforms.Resize((size,size)),
        transforms.ToTensor()
    ])

    # load input image
    if not input_directory:
        image = Image.open(relative_directory + "\\IO_images\\input_bowl.jpg")
    else:
        image = Image.open(input_directory)
    width, height = image.size
    image = data_transforms(image)
    if dataset == "cifar":
        image.unsqueeze_(0)
        image.expand(3,3,size,size)
    else:
        image.unsqueeze_(1)
    x = image.to(device)
    perturbation = pretrained_G(x)
    perturbation = torch.clamp(perturbation, -0.3, 0.3)
    scaled_perturb_level = perturb_level * MAX_SCALED_PERTURB_LEVEL / MAX_PERTURB_LEVEL
    adv_img = (perturbation * scaled_perturb_level) + image
    adv_img = torch.clamp(adv_img, 0, 1)
    saved_state[1] = adv_img
    adv_img_def_size = torch.nn.functional.interpolate(adv_img, size=(height, width))

    plt.axis('off')
    plt.imshow(np.transpose(adv_img_def_size[0].detach().numpy(), (1, 2, 0)))
    plt.savefig(output_directory, bbox_inches='tight')

    saved_state[0] = image
    saved_state[2] = target_model

def test_accuracy():
    image = (Variable(saved_state[0])).to(device)
    adv_img = (Variable(saved_state[1])).to(device)
    target_model = saved_state[2]

    input_label_list = [] #list to store all prediction labels of input image
    adv_label_list = [] #list to store adversarial output prediction
    for i in range(loop):
        output = target_model(image)
        index = output.data.cpu().numpy().argmax()
        input_label_list.append(index)

        output = target_model(adv_img)
        index = output.data.cpu().numpy().argmax()
        adv_label_list.append(index)

    # print(input_label_list)
    # print(adv_label_list)

    output_state[0] = max(input_label_list, key=input_label_list.count)
    output_state[1] = max(adv_label_list, key=adv_label_list.count)
    output_state[2] = adv_label_list

    return output_state
     
def get_label_accuracy(dataset):
    input_label = output_state[0]
    adv_label = output_state[1]
    adv_label_list = output_state[2]

    if dataset == "cifar":
        target_dataset = torchvision.datasets.CIFAR100(relative_directory + "\\dataset", train=True, transform=transforms.ToTensor(), download=True)
    else:
        target_dataset = torchvision.datasets.MNIST(relative_directory + "\\dataset", train=True, transform=transforms.ToTensor(), download=True)
    
    classes = target_dataset.classes
    # print("original prediction :", classes[input_label], "\nadversarial prediction :", classes[adv_label])
    # print("adversarial accuracy :", (adv_label_list.count(input_label)/loop)*100)
    return classes[input_label], classes[adv_label],  (adv_label_list.count(input_label)/loop)*100


if __name__ == "__main__":
    ans = adversarial_attack('cifar',12)
    test_accuracy()
    get_label_accuracy('cifar')