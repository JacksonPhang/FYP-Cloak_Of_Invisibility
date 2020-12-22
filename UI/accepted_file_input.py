"""
Constant Definition For File Input

Used to control what files will be accepted by the application
"""
ACCEPTED_INPUT_FILE = ["png", "jpg", "jpeg", "bmp"]

def getAcceptInput():
    return "(" + " ".join(["*." + string for string in ACCEPTED_INPUT_FILE])  + ")"