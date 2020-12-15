from PyQt5 import QtCore, QtGui, QtWidgets
from my_qlabel import MyQLabel
from my_qplaintextedit import MyQPlainTextEdit

"""
The first page of the User Interface
Do not edit unless you know what's up
"""                
class Ui_FormOne(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self._parent = parent

        Form = QtWidgets.QWidget()
        Form.setObjectName("Form")
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
        self.generateButton.clicked.connect(self.generateButtonFunction)
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
        self.learnButton.clicked.connect(self.learnButtonFunction)
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

    #####################################################################################################
    #                                       Button Functionality                                        #
    #####################################################################################################
    """
    Generate Button Functionality

    Changes the selection of the application to the second page
    """    
    def generateButtonFunction(self):
        # Change to second page
        self._parent.stackWidget.setCurrentIndex(1)

    """
    Browse Button Functionality

    Open default file browser to select input file    
    """
    def browseButtonFunction(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "File Browser", "","Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            self.imageUpload.setPixmap(QtGui.QPixmap(fileName))
            self.setFilePath(fileName)

    """
    Learn Button Function

    Used to create a message pop up window to 
    provide the user with more information
    about the application
    """
    def learnButtonFunction(self):
        popup = QtWidgets.QMessageBox()
        popup.setWindowTitle("Application Information")
        popup.setWindowModality(QtCore.Qt.ApplicationModal)
        popup.setIcon(QtWidgets.QMessageBox.Information)
        popup.setStandardButtons(QtWidgets.QMessageBox.Ok)
        popup.setText("Computer Science Final Year Project\nCloak Of Invisibility")
        popup.setInformativeText("Add In Information Here")
        popup.exec_()

    #####################################################################################################
    #                                         Helper Functions                                          #
    #####################################################################################################
    """
    Helper Function

    Used to set the file path of the chosen image file to
    the text edit as a display to the user
    """
    def setFilePath(self, fileName):
        _translate = QtCore.QCoreApplication.translate
        self.plainTextEdit.clear()
        self.plainTextEdit.setPlainText(_translate("Form", fileName))