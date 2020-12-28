"""
Constant Definition For File Input

Used to control what files will be accepted by the application
"""
ACCEPTED_INPUT_FILE = ["png", "jpg", "jpeg", "bmp"]

def getAcceptInput(join = True):
    if join:
        return "(" + " ".join(["*." + string for string in ACCEPTED_INPUT_FILE])  + ")"
    else:
        return ACCEPTED_INPUT_FILE