"""
Script to set up and install all required libraries
"""
import os

def install():
    #install required libraries
    os.system('python -m pip install --upgrade pip')
    os.system('pip install --upgrade matplotlib')
    os.system('pip install --upgrade PyQt5')
    os.system('pip install torch')
    os.system('pip install torchvision')

if __name__ == "__main__":
    install()
