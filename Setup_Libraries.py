import os

def install():
    #install required libraries
    os.system('pip install --upgrade matplotlib')
    os.system('python -m pip install --upgrade pip')
    os.system('pip install torch')
    os.system('pip install torchvision')

if __name__ == "__main__":
    install()
