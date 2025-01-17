"""
Script used to train advgan model. To train for mnist, change image_nc, pretrained_model and dataset used
"""

import torch
import torchvision.datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from advGAN import AdvGAN_Attack
from models import MNIST_target_net
from resnet import CifarResNet
from resnet import BasicBlock

if __name__ == "__main__":
    use_cuda=True
    image_nc=3 #3 channels for cifar dataset, 1 channel for mnist dataset
    epochs = 60
    batch_size = 5
    BOX_MIN = 0
    BOX_MAX = 1

    # Define what device we are using
    print("CUDA Available: ",torch.cuda.is_available())
    device = torch.device("cuda" if (use_cuda and torch.cuda.is_available()) else "cpu")

    pretrained_model = "./CIFAR100_target_model.pth"
    targeted_model = CifarResNet(BasicBlock, [9, 9, 9]).to(device)
    targeted_model.load_state_dict(torch.load(pretrained_model))
    targeted_model.eval()
    model_num_labels = 100

    # cifar train dataset and dataloader declaration
    cifar_dataset = torchvision.datasets.CIFAR100('./dataset', train=True, transform=transforms.ToTensor(), download=True)
    dataloader = DataLoader(cifar_dataset, batch_size=batch_size, shuffle=True, num_workers=1)
    advGAN = AdvGAN_Attack(device,
                            targeted_model,
                            model_num_labels,
                            image_nc,
                            BOX_MIN,
                            BOX_MAX)

    advGAN.train(dataloader, epochs)
