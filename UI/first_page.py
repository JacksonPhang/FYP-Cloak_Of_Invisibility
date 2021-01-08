from PyQt5 import QtCore, QtGui, QtWidgets
import os
from first_page_modules.my_qlabel import MyQLabel
from first_page_modules.my_qplaintextedit import MyQPlainTextEdit
from accepted_file_input import getAcceptInput
from PyTorch.test_adversarial_examples import adversarial_attack

class Ui_FormOne(QtWidgets.QWidget):
    """
    The first page of the User Interface
    Do not edit unless you know what's up
    """

    def __init__(self, parent):
        """
        Initialise Object

        Spawns the UI elements and sets element positions 
        """
        super().__init__()
        self._parent = parent
        self.file_path = ""

        Form = QtWidgets.QWidget()
        Form.setObjectName("Form")
        Form.resize(980, 550)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.imageUpload = MyQLabel(Form, self)
        self.imageUpload.setPixmap(QtGui.QPixmap(os.path.dirname(os.path.abspath(__file__)) + "\\images\\Screenshot (106).png"))
        self.imageUpload.setScaledContents(True)
        self.imageUpload.setObjectName("imageUpload")
        self.gridLayout_2.addWidget(self.imageUpload, 0, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(73, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 14, 0, 1, 1)
        self.cifarCheckBox = QtWidgets.QRadioButton(Form)
        self.cifarCheckBox.setChecked(True)
        self.cifarCheckBox.setObjectName("cifarCheckBox")
        self.gridLayout.addWidget(self.cifarCheckBox, 4, 0, 1, 1)
        self.mnistCheckBox = QtWidgets.QRadioButton(Form)
        self.mnistCheckBox.setObjectName("mnistCheckBox")
        self.gridLayout.addWidget(self.mnistCheckBox, 5, 0, 1, 1)
        self.buttonGroup = QtWidgets.QButtonGroup()
        self.buttonGroup.addButton(self.cifarCheckBox, 1)
        self.buttonGroup.addButton(self.mnistCheckBox, 2)
        self.browseButton = QtWidgets.QPushButton(Form)
        self.browseButton.clicked.connect(self.browseButtonFunction)
        self.browseButton.setObjectName("browseButton")
        self.gridLayout.addWidget(self.browseButton, 3, 2, 1, 2)
        self.filePathLabel = QtWidgets.QLabel(Form)
        self.filePathLabel.setObjectName("filePathLabel")
        self.gridLayout.addWidget(self.filePathLabel, 1, 0, 1, 2)
        self.inputConfigLabel = QtWidgets.QLabel(Form)
        self.inputConfigLabel.setMinimumSize(QtCore.QSize(200, 50))
        self.inputConfigLabel.setAutoFillBackground(True)
        self.inputConfigLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.inputConfigLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputConfigLabel.setObjectName("inputConfigLabel")
        self.gridLayout.addWidget(self.inputConfigLabel, 0, 0, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 2, 1, 2)
        self.generateButton = QtWidgets.QPushButton(Form)
        self.generateButton.clicked.connect(self.generateButtonFunction)
        self.generateButton.setObjectName("generateButton")
        self.gridLayout.addWidget(self.generateButton, 14, 1, 1, 2)
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 8, 0, 1, 4)
        self.inputTextEdit = MyQPlainTextEdit(Form, self)
        self.inputTextEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.inputTextEdit.setAutoFillBackground(False)
        self.inputTextEdit.setObjectName("inputTextEdit")
        self.gridLayout.addWidget(self.inputTextEdit, 2, 0, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(26, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 14, 3, 1, 1)
        self.perturbationLabel = QtWidgets.QLabel(Form)
        self.perturbationLabel.setObjectName("perturbationLabel")
        self.gridLayout.addWidget(self.perturbationLabel, 6, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(14, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 9, 2, 1, 1)
        self.perturbationSpinBox = QtWidgets.QSpinBox(Form)
        self.perturbationSpinBox.setMinimum(1)
        self.perturbationSpinBox.setMaximum(100)
        self.perturbationSpinBox.setValue(50)
        self.perturbationSpinBox.setObjectName("perturbationSpinBox")
        self.gridLayout.addWidget(self.perturbationSpinBox, 6, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        self.learnButton = QtWidgets.QPushButton(Form)
        self.learnButton.clicked.connect(self.learnButtonFunction)
        self.learnButton.setObjectName("learnButton")
        self.gridLayout_2.addWidget(self.learnButton, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(665, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 1, 1, 1)

        self.retranslateUi(Form)
        # Link the slider and the spinbox value to ensure consistent and correct value
        self.perturbationSpinBox.valueChanged['int'].connect(self.horizontalSlider.setValue)
        self.horizontalSlider.valueChanged['int'].connect(self.perturbationSpinBox.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.setLayout(self.gridLayout_2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.browseButton.setText(_translate("Form", "Browse"))
        self.filePathLabel.setText(_translate("Form", "Choose A File:"))
        self.inputConfigLabel.setText(_translate("Form", "INPUT CONFIGURATION"))
        self.generateButton.setText(_translate("Form", "GENERATE"))
        self.inputTextEdit.setPlainText(_translate("Form", "Input File Path"))
        self.perturbationLabel.setText(_translate("Form", "Perturbation Level:"))
        self.mnistCheckBox.setText(_translate("Form", "MNIST"))
        self.cifarCheckBox.setText(_translate("Form", "CIFAR"))
        self.learnButton.setText(_translate("Form", "Learn More"))

    #####################################################################################################
    #                                       Button Functionality                                        #
    #####################################################################################################  
    def generateButtonFunction(self):
        """
        Generate Button Functionality

        Changes the selection of the application to the second page
        """
        # adversarial_attack(dataset, perturb_level, input_directory = None)
        popup = QtWidgets.QMessageBox()
        popup.setWindowTitle("Application Information")
        popup.setWindowModality(QtCore.Qt.ApplicationModal)
        popup.setIcon(QtWidgets.QMessageBox.Information)
        popup.setStandardButtons(QtWidgets.QMessageBox.Ok)
        popup.setText("Application Generating Perturbated Image")
        popup.setInformativeText("Click Ok to continue\nApplication will automatically switch to next page when image has been generated")
        popup.exec_()

        # Backend functionality which will generate the perturbed image
        adversarial_attack(self.getCheckBox(), self.perturbationSpinBox.value(), self.file_path)
        self._parent.secondPageUI.setImage()

        # Change to second page
        self._parent.stackWidget.setCurrentIndex(1)

    def browseButtonFunction(self):
        """
        Browse Button Functionality

        Open default file browser to select input file    
        """
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "File Browser", "","Image Files " + getAcceptInput())
        if fileName:
            self.setPixMapAndPath(fileName)

    def learnButtonFunction(self):
        """
        Learn Button Function

        Used to create a message pop up window to 
        provide the user with more information
        about the application
        """
        popup = QtWidgets.QMessageBox()
        popup.setWindowTitle("Application Information")
        popup.setWindowModality(QtCore.Qt.ApplicationModal)
        popup.setIcon(QtWidgets.QMessageBox.Information)
        popup.setStandardButtons(QtWidgets.QMessageBox.Ok)
        popup.setText("Computer Science Final Year Project\nCloak Of Invisibility")
        text1 = "First select the file which you would like to perturb\nThen choose which dataset to use for the perturbation\n"
        text2 = "Use the slider to set how much perturbation you want\nFinally click the Generate button to start perturbating the image\n\n"
        text3 = "CIFAR is used for general images\nMNIST is used for number images\nThe slider value of 1 for the least perturbed and 100 for the most perturbed\n\n"
        text4 = "Created images may appear pixelated due to the perturbation algorithm only accepting a limited amount of pixels"
        texts = text1 + text2 + text3 + text4
        popup.setInformativeText(texts)
        popup.exec_()

    #####################################################################################################
    #                                         Helper Functions                                          #
    #####################################################################################################
    def setPixMapAndPath(self, file_path):
        """
        Helper Function

        Scales the image before setting it to the UI
        Sets the file path of the chosen image file to
        the text edit as a display to the user
        """
        self.imageUpload.setPixmap(QtGui.QPixmap(file_path).scaled(1080, 480, QtCore.Qt.KeepAspectRatio))
        self.file_path = file_path
        _translate = QtCore.QCoreApplication.translate
        self.inputTextEdit.clear()
        self.inputTextEdit.setPlainText(_translate("Form", file_path))

    def isImageFile(self, file):
        """
        Helper Function

        Checks whether the file path provided 
        references an accepted image file
        """
        return file.split(".")[-1] in getAcceptInput(False)

    def getCheckBox(self):
        """
        Helper Function

        Used to obtain the checkbox value from the user
        """
        checkbox_value = {
            1: "cifar",
            2: "mnist"
        }
        return checkbox_value.get(self.buttonGroup.checkedId(), "Error")