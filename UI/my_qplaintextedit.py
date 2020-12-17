from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from os.path import isfile
from accepted_file_input import ACCEPTED_INPUT_FILE

class MyQPlainTextEdit(QtWidgets.QPlainTextEdit):
    """
    Custom QPlainTextEdit

    Used to display file path of chosen picture
    Used to enter file path manually if user intends to do so
    """

    def __init__(self, Form, parent):
        """
        Initialise Object
        """
        super().__init__(Form)
        self._parent = parent

    def keyPressEvent(self, event):
        """
        Override Parent Function 
        
        Allows for the customisation of the class's
        response when user presses the enter key
        """
        if event.key() == Qt.Qt.Key_Return:
            file_path = self.toPlainText()
            if isfile(file_path) and self.isImageFile(file_path):
                self._parent.imageUpload.setPixmap(QtGui.QPixmap(file_path))
                self._parent.file_path = file_path
        else:
            super().keyPressEvent(event)

    def isImageFile(self, file):
        """
        Checks whether the file path provided 
        references an image file
        """
        return file.split(".")[-1] in ACCEPTED_INPUT_FILE