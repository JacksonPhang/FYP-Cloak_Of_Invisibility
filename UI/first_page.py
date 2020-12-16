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
        self.imageUpload = QtWidgets.QLabel(Form)
        self.imageUpload.setText("")
        self.imageUpload.setPixmap(QtGui.QPixmap("Screenshot (106).png"))
        self.imageUpload.setScaledContents(True)
        self.imageUpload.setObjectName("imageUpload")
        self.gridLayout_2.addWidget(self.imageUpload, 0, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(26, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(14, 151, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 2, 1, 1)
        self.browseButton = QtWidgets.QPushButton(Form)
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
        spacerItem2 = QtWidgets.QSpacerItem(73, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 2)
        self.generateButton = QtWidgets.QPushButton(Form)
        self.generateButton.setObjectName("generateButton")
        self.gridLayout.addWidget(self.generateButton, 9, 1, 1, 2)
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 5, 0, 1, 4)
        self.inputTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.inputTextEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.inputTextEdit.setAutoFillBackground(False)
        self.inputTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.inputTextEdit, 2, 0, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 9, 0, 1, 1)
        self.perturbationLabel = QtWidgets.QLabel(Form)
        self.perturbationLabel.setObjectName("perturbationLabel")
        self.gridLayout.addWidget(self.perturbationLabel, 4, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 2, 1, 2)
        self.perturbationSpinBox = QtWidgets.QSpinBox(Form)
        self.perturbationSpinBox.setMinimum(1)
        self.perturbationSpinBox.setMaximum(100)
        self.perturbationSpinBox.setObjectName("perturbationSpinBox")
        self.gridLayout.addWidget(self.perturbationSpinBox, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        self.learnButton = QtWidgets.QPushButton(Form)
        self.learnButton.setObjectName("learnButton")
        self.gridLayout_2.addWidget(self.learnButton, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(665, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 1, 1, 1)

        self.retranslateUi(Form)
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