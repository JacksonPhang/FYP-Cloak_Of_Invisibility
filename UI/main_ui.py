from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
from os.path import isfile

ACCEPTED_INPUT_FILE = ["png", "jpg", "jpeg", "bmp"]

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

"""
The first page of the User Interface
Do not edit unless you know what's up
"""                
class Ui_FormOne(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        Form = QtWidgets.QWidget()
        Form.setObjectName("Form1")
        Form.resize(980, 550)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.imageUpload = MyQLabel(Form, self)
        self.imageUpload.setText("")
        self.imageUpload.setPixmap(QtGui.QPixmap(".\\Screenshot (106).png"))
        self.imageUpload.setScaledContents(True)
        self.imageUpload.setObjectName("imageUpload")
        self.imageUpload.setMaximumSize(QtCore.QSize(1900, 1000))
        self.gridLayout_2.addWidget(self.imageUpload, 0, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.filePathLabel = QtWidgets.QLabel(Form)
        self.filePathLabel.setObjectName("filePathLabel")
        self.gridLayout.addWidget(self.filePathLabel, 1, 0, 1, 2)
        self.plainTextEdit = MyQPlainTextEdit(Form, self)
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 2, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(73, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 2)
        self.browseButton = QtWidgets.QPushButton(Form)
        self.browseButton.setObjectName("browseButton")
        self.browseButton.clicked.connect(self.browseButtonFunction)
        self.gridLayout.addWidget(self.browseButton, 3, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(14, 151, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        self.generateButton = QtWidgets.QPushButton(Form)
        self.generateButton.setObjectName("generateButton")
        self.generateButton.clicked.connect(generateButtonFunction)
        self.gridLayout.addWidget(self.generateButton, 5, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(26, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 3, 1, 1)
        self.inputConfigLabel = QtWidgets.QLabel(Form)
        self.inputConfigLabel.setMinimumSize(QtCore.QSize(200, 50))
        self.inputConfigLabel.setAutoFillBackground(True)
        self.inputConfigLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.inputConfigLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputConfigLabel.setObjectName("inputConfigLabel")
        self.gridLayout.addWidget(self.inputConfigLabel, 0, 0, 1, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        self.learnButton = QtWidgets.QPushButton(Form)
        self.learnButton.setObjectName("learnButton")
        self.gridLayout_2.addWidget(self.learnButton, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(665, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.setLayout(self.gridLayout_2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.filePathLabel.setText(_translate("Form", "Choose A File:"))
        self.plainTextEdit.setPlainText(_translate("Form", "Input File Path"))
        self.browseButton.setText(_translate("Form", "Browse"))
        self.generateButton.setText(_translate("Form", "GENERATE"))
        self.inputConfigLabel.setText(_translate("Form", "INPUT CONFIGURATION"))
        self.learnButton.setText(_translate("Form", "Learn More"))

    def browseButtonFunction(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "File Browser", "","Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            self.imageUpload.setPixmap(QtGui.QPixmap(fileName))
            self.setFilePath(fileName)

    def setFilePath(self, fileName):
        _translate = QtCore.QCoreApplication.translate
        self.plainTextEdit.clear()
        self.plainTextEdit.setPlainText(_translate("Form", fileName))

"""
The second page of the User Interface
Do not edit unless you know what's up
"""
class Ui_FormTwo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        Form = QtWidgets.QWidget()
        Form.setObjectName("Form2")
        Form.resize(980, 550)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.imageOutput = QtWidgets.QLabel(Form)
        self.imageOutput.setText("")
        self.imageOutput.setPixmap(QtGui.QPixmap(".\\Screenshot (106).png"))
        self.imageOutput.setScaledContents(True)
        self.imageOutput.setObjectName("imageOutput")
        self.gridLayout.addWidget(self.imageOutput, 0, 0, 1, 4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.outputLabel = QtWidgets.QLabel(Form)
        self.outputLabel.setMinimumSize(QtCore.QSize(200, 50))
        self.outputLabel.setAutoFillBackground(True)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.verticalLayout.addWidget(self.outputLabel)
        self.compareButton = QtWidgets.QPushButton(Form)
        self.compareButton.setEnabled(True)
        self.compareButton.setCheckable(False)
        self.compareButton.setDefault(False)
        self.compareButton.setFlat(False)
        self.compareButton.setObjectName("compareButton")
        self.verticalLayout.addWidget(self.compareButton)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.differentImageButton = QtWidgets.QPushButton(Form)
        self.differentImageButton.setObjectName("differentImageButton")
        self.differentImageButton.clicked.connect(differentImageButtonFunction)
        self.verticalLayout.addWidget(self.differentImageButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(314, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(313, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.setLayout(self.gridLayout)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.outputLabel.setText(_translate("Form", "OUTPUT"))
        self.compareButton.setText(_translate("Form", "COMPARE  WITH CLASSIFIERS"))
        self.differentImageButton.setText(_translate("Form", "TRY DIFFERENT IMAGE"))
        self.saveButton.setText(_translate("Form", "SAVE IMAGE"))

main_ui_reference = None
class main_ui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QtWidgets.QVBoxLayout()
        firstPageUI = Ui_FormOne()
        secondPageUI = Ui_FormTwo()

        self.stackWidget = QtWidgets.QStackedWidget()
        self.stackWidget.addWidget(firstPageUI) # Index 0
        self.stackWidget.addWidget(secondPageUI) # Index 1

        mainLayout.addWidget(self.stackWidget)
        self.setLayout(mainLayout)

def generateButtonFunction():
    # Change to second page
    main_ui_reference.stackWidget.setCurrentIndex(1)

def differentImageButtonFunction():
    # Change to first page
    main_ui_reference.stackWidget.setCurrentIndex(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_ui_reference = main_ui()
    main_ui_reference.show()
    sys.exit(app.exec_())