"""
Primary function for adding perturbation onto input image and obtaining prediction label
"""

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
    """
    Conducts the adversarial attack on input image

    Args:
        dataset ([String]): name of dataset selected by the user
        perturb_level ([int]): Integer level from 1 to 100 signifying perturbation intensity level
        input_directory ([String], optional): file path for input image location. Defaults to None.
    """
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

    # apply transformations to the image
    # resize the image to match the dataset model's input image size
    data_transforms = transforms.Compose([
        transforms.Resize((size,size)),
        transforms.ToTensor()
    ])

    # load input image
    if not input_directory:
        image = Image.open(relative_directory + "\\IO_images\\input_test.jpg")
    else:
        image = Image.open(input_directory)

    # retain original image dimensions
    width, height = image.size
    image = data_transforms(image)

    # modify the input to the dataset models to match the input dimensions and weights
    if dataset == "cifar":
        image.unsqueeze_(0)
        image.expand(3,3,size,size)
    else:
        image.unsqueeze_(1)

    x = image.to(device)
    # generate perturbation
    perturbation = pretrained_G(x)
    perturbation = torch.clamp(perturbation, -0.3, 0.3)
    # scale the perturbation depending on the perturb_level provided by the user
    scaled_perturb_level = perturb_level * MAX_SCALED_PERTURB_LEVEL / MAX_PERTURB_LEVEL
    # add scaled perturbation to the image
    adv_img = (perturbation * scaled_perturb_level) + image
    adv_img = torch.clamp(adv_img, 0, 1)
    saved_state[1] = adv_img
    # resize the image back to the original image dimensions
    adv_img_def_size = torch.nn.functional.interpolate(adv_img, size=(height, width))

    plt.axis('off')
    # convert tensor image into a matplotlib image figure
    plt.imshow(np.transpose(adv_img_def_size[0].detach().numpy(), (1, 2, 0)))
    # save the image in the output directory
    plt.savefig(output_directory, bbox_inches='tight')

    saved_state[0] = image
    saved_state[2] = target_model

def test_accuracy():
    """
    Runs prediction and predicts labels for the input image and adversarial image

    Returns:
        [list]: List containing input label index, output label index and output label list
    """
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

    # get most common prediction for input label
    output_state[0] = max(input_label_list, key=input_label_list.count)
    # get most common prediction for adversarial label
    output_state[1] = max(adv_label_list, key=adv_label_list.count)
    output_state[2] = adv_label_list

    return output_state
     
def get_label_accuracy(dataset, output_state):
    """
    Get the labels of the images and the accuracy percentage of the adversarial label prediction

    Args:
        dataset ([String]): dataset selected by user
        output_state ([list]): list containing input label index, output label index and output label list

    Returns:
        [list]: list containing input label, output label and output label accuracy
    """
    input_label = output_state[0]
    adv_label = output_state[1]
    adv_label_list = output_state[2]

    # load target dataset
    if dataset == "cifar":
        target_dataset = torchvision.datasets.CIFAR100(relative_directory + "\\dataset", train=True, transform=transforms.ToTensor(), download=True)
    else:
        target_dataset = torchvision.datasets.MNIST(relative_directory + "\\dataset", train=True, transform=transforms.ToTensor(), download=True)
    
    classes = target_dataset.classes
    return classes[input_label], classes[adv_label],  (adv_label_list.count(input_label)/loop)*100

if __name__ == "__main__":
    ans = adversarial_attack('cifar',12)
    test_accuracy()
    get_label_accuracy('cifar')