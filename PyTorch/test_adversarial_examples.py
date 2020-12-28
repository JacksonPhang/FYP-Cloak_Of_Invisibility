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
MAX_SCALED_PERTURB_LEVEL = 5
relative_directory = dirname(abspath(__file__))
output_directory = relative_directory + "\\IO_images\\output_img.jpg"

def adversarial_attack(dataset, perturb_level, input_directory = None):
    print(dataset)
    print(perturb_level)
    print(input_directory)
    use_cuda=True
    # Define what device we are using
    print("CUDA Available: ", torch.cuda.is_available())
    device = torch.device("cuda" if (use_cuda and torch.cuda.is_available()) else "cpu")

    if dataset == "cifar":
        image_nc = 3
        pretrained_model = relative_directory + "\\CIFAR100_target_model.pth"
        pretrained_generator_path = relative_directory + "\\models\\cifar_epoch_60.pth"
        target_model = CifarResNet(BasicBlock, [9, 9, 9]).to(device)
    else:
        image_nc = 1
        pretrained_model = relative_directory + "\\MNIST_target_model.pth"
        pretrained_generator_path = relative_directory + "\\models\\netG_epoch_60.pth"
        target_model = MNIST_target_net().to(device)
    batch_size = 128
    gen_input_nc = image_nc

    # load the pretrained model
    target_model.load_state_dict(torch.load(pretrained_model))
    target_model.eval()

    # load the generator of adversarial examples
    pretrained_G = models.Generator(gen_input_nc, image_nc).to(device)
    pretrained_G.load_state_dict(torch.load(pretrained_generator_path, map_location=torch.device('cpu')))
    pretrained_G.eval()

    data_transforms = transforms.Compose([
        transforms.RandomResizedCrop(256, ratio=(1, 1)),
        transforms.ToTensor()
    ])

    # load input image
    if not input_directory:
        image = Image.open(relative_directory + "\\IO_images\\input_test.jpg")
    else:
        image = Image.open(input_directory)
    image = data_transforms(image)
    if dataset == "cifar":
        image.unsqueeze_(0)
        image.expand(3,3,256,256)
    else:
        image.unsqueeze_(1)
    x = image.to(device)
    perturbation = pretrained_G(x)
    perturbation = torch.clamp(perturbation, -0.3, 0.3)
    perturb_level = perturb_level*MAX_SCALED_PERTURB_LEVEL/MAX_PERTURB_LEVEL
    perturbation = perturbation/perturb_level
    adv_img = perturbation + image
    adv_img = torch.clamp(adv_img, 0, 1)
    plt.axis('off')
    plt.imshow(np.transpose(adv_img[0].detach().numpy(), (1, 2, 0)))
    plt.savefig(output_directory, bbox_inches='tight')
    plt.show()

    # Input = Variable(image)
    # Input = Input.to(device)
    # output = target_model(Input)
    # print(output)
    # index = output.data.cpu().numpy().argmax()
    # return (index)

def test_accuracy(dataset, index, input_directory=None):
    if dataset == "cifar":
        target_dataset = torchvision.datasets.CIFAR100(relative_directory + "\\dataset", train=True, transform=transforms.ToTensor(), download=True)
        classes = target_dataset.classes
        print(classes[index])
    else:
        target_dataset = torchvision.datasets.MNIST(relative_directory + "\\dataset", train=True, transform=transforms.ToTensor(), download=True)

    if input_directory is not None:
        ori_image = Image.open(input_directory)
    else:
        ori_image = Image.open(relative_directory + "\\IO_images\\input_img.jpg")
    pert_image = Image.open(output_directory)


    
    
    # # test adversarial examples in MNIST training dataset
    # mnist_dataset = torchvision.datasets.MNIST('./dataset', train=True, transform=transforms.ToTensor(), download=True)
    # train_dataloader = DataLoader(mnist_dataset, batch_size=batch_size, shuffle=False, num_workers=1)
    # num_correct = 0
    # for i, data in enumerate(train_dataloader, 0):
    #     test_img, test_label = data
    #     test_img, test_label = test_img.to(device), test_label.to(device)
    #     perturbation = pretrained_G(test_img)
    #     perturbation = torch.clamp(perturbation, -0.3, 0.3)
    #     adv_img = perturbation + test_img
    #     adv_img = torch.clamp(adv_img, 0, 1)
    #     pred_lab = torch.argmax(target_model(adv_img),1)
    #     num_correct += torch.sum(pred_lab==test_label,0)
    #
    # print('MNIST training dataset:')
    # print('num_correct: ', num_correct.item())
    # print('accuracy of adv imgs in training set: %f\n'%(num_correct.item()/len(mnist_dataset)))
    #
    # # test adversarial examples in MNIST testing dataset
    # mnist_dataset_test = torchvision.datasets.MNIST('./dataset', train=False, transform=transforms.ToTensor(), download=True)
    # test_dataloader = DataLoader(mnist_dataset_test, batch_size=batch_size, shuffle=False, num_workers=1)
    # num_correct = 0
    # for i, data in enumerate(test_dataloader, 0):
    #     test_img, test_label = data
    #     test_img, test_label = test_img.to(device), test_label.to(device)
    #     perturbation = pretrained_G(test_img)
    #     perturbation = torch.clamp(perturbation, -0.3, 0.3)
    #     adv_img = perturbation + test_img
    #     adv_img = torch.clamp(adv_img, 0, 1)
    #     pred_lab = torch.argmax(target_model(adv_img),1)
    #     num_correct += torch.sum(pred_lab==test_label,0)
    #
    # print('num_correct: ', num_correct.item())
    # print('accuracy of adv imgs in testing set: %f\n'%(num_correct.item()/len(mnist_dataset_test)))

if __name__ == "__main__":
    ans = adversarial_attack('cifar',50)
    test_accuracy('cifar', ans)