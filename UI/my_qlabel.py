from PyQt5 import QtCore, QtGui, QtWidgets

"""
Custom QLabel
Used to hold a image

Functions as the drag and drop box for user to upload images
"""
class MyQLabel(QtWidgets.QLabel):
        def __init__(self, Form, parent):
            super().__init__(Form)
            self._parent = parent
            self.setAcceptDrops(True)
            self.setScaledContents(True)

        def dragEnterEvent(self, event):
            event.accept() if event.mimeData().hasImage else event.ignore()
    
        def dragMoveEvent(self, event):
            event.accept() if event.mimeData().hasImage else event.ignore()
    
        def dropEvent(self, event):
            if event.mimeData().hasImage:
                event.setDropAction(QtCore.Qt.CopyAction)
                file_path = event.mimeData().urls()[0].toLocalFile()
                self.setPixmap(QtGui.QPixmap(file_path))
                self._parent.setFilePath(file_path)
    
                event.accept()
            else:
                event.ignore()