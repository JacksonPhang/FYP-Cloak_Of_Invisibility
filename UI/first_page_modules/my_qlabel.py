from PyQt5 import QtCore, QtGui, QtWidgets

class MyQLabel(QtWidgets.QLabel):
    """
    Custom QLabel
    Used to hold a image

    Functions as the drag and drop box for user to upload images
    """

    def __init__(self, Form, parent):
        """
        Initialise Object

        Allows class to accept files to be dropped on its object
        """
        super().__init__(Form)
        self._parent = parent
        self.setAcceptDrops(True)
        self.setScaledContents(True)

    def setPixmap(self, pixmap, scale=True):
        """
        Allows class to accept image event which enters
        the boundary of the class object
        """
        if scale: 
            super().setPixmap(pixmap.scaled(1580, 880, QtCore.Qt.KeepAspectRatio))
        else:
            super().setPixmap(pixmap)


    def dragEnterEvent(self, event):
        """
        Override Parent Function

        Allows class to accept image event which enters
        the boundary of the class object
        """
        event.accept() if event.mimeData().hasImage else event.ignore()

    def dragMoveEvent(self, event):
        """
        Override Parent Function

        Allows class to accept image event which moves
        within the boundary of the class object
        """
        event.accept() if event.mimeData().hasImage else event.ignore()
   
    def dropEvent(self, event):
        """
        Override Parent Function

        Allows class to accept image event which drops
        within the boundary of the class object
        """ 
        if event.mimeData().hasImage:
            event.setDropAction(QtCore.Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            print(file_path)
            self.setPixmap(QtGui.QPixmap(file_path))
            self._parent.setFilePath(file_path)

            event.accept()
        else:
            event.ignore()