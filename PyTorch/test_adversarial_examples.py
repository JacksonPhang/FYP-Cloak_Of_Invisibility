import torch
import torchvision.datasets
import torchvision.transforms as transforms
from torchvision.utils import save_image
from torch.utils.data import DataLoader
import models
from models import MNIST_target_net
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from resnet import CifarResNet
from resnet import BasicBlock

MAX_PERTURB_LEVEL = 100
MAX_SCALED_PERTURB_LEVEL = 5

def adversarial_attack(perturb_level):
    use_cuda=True
    image_nc=3
    batch_size = 128

    gen_input_nc = image_nc

    # Define what device we are using
    print("CUDA Available: ",torch.cuda.is_available())
    device = torch.device("cuda" if (use_cuda and torch.cuda.is_available()) else "cpu")

    # load the pretrained model
    pretrained_model = "./CIFAR100_target_model.pth"
    target_model = CifarResNet(BasicBlock, [9, 9, 9]).to(device)
    target_model.load_state_dict(torch.load(pretrained_model))
    target_model.eval()

    # load the generator of adversarial examples
    pretrained_generator_path = './models/cifar_epoch_20.pth'
    pretrained_G = models.Generator(gen_input_nc, image_nc).to(device)
    pretrained_G.load_state_dict(torch.load(pretrained_generator_path))
    pretrained_G.eval()

    data_transforms = transforms.Compose([
        transforms.RandomResizedCrop(256, ratio=(1, 1)),
        transforms.ToTensor()
    ])

    image = Image.open('./IO_images/input_img.jpg')
    image = data_transforms(image)
    image.unsqueeze_(0)
    image.expand(3,3,256,256)
    x = image.to(device)
    perturbation = pretrained_G(x)
    perturbation = torch.clamp(perturbation, -0.3, 0.3)
    perturb_level = perturb_level*MAX_SCALED_PERTURB_LEVEL/MAX_PERTURB_LEVEL
    perturbation = perturbation/perturb_level
    adv_img = perturbation + image
    adv_img = torch.clamp(adv_img, 0, 1)
    plt.axis('off')
    plt.imshow(np.transpose(adv_img[0].detach().numpy(), (1, 2, 0)))
    plt.savefig('./IO_images/output_img.jpg', bbox_inches='tight')
    plt.show()

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
    adversarial_attack(50)