from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from os.path import isfile
from accepted_file_input import ACCEPTED_INPUT_FILE

"""
Custom QPlainTextEdit
Used to display file path of chosen picture
Used to enter file path manually if user intends to do so
"""
class MyQPlainTextEdit(QtWidgets.QPlainTextEdit):
    def __init__(self, Form, parent):
        super().__init__(Form)
        self._parent = parent

    def keyPressEvent(self, event):
        if event.key() == Qt.Qt.Key_Return:
            file_path = self.toPlainText()
            if isfile(file_path) and self.isImageFile(file_path):
                self._parent.imageUpload.setPixmap(QtGui.QPixmap(file_path))
        else:
            super().keyPressEvent(event)

    def isImageFile(self, file):
        return file.split(".")[-1] in ACCEPTED_INPUT_FILE