from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import dirname, abspath
from accepted_file_input import getAcceptInput
from PyTorch.test_adversarial_examples import test_accuracy
from PyTorch.test_adversarial_examples import get_label_accuracy
from PyTorch.test_adversarial_examples import compare_display

class Ui_FormTwo(QtWidgets.QWidget):
    """
    The second page of the User Interface
    """

    def __init__(self, parent):
        """
        Initialise Object

        Spawns the UI elements and sets element positions 
        """
        super().__init__()
        self._parent = parent
        self.file_path = dirname(dirname(abspath(__file__))) + "/PyTorch/IO_images/output_img.jpg"
        self.display = None

        Form = QtWidgets.QWidget()
        Form.setObjectName("Form")
        Form.resize(980, 550)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.imageOutput = QtWidgets.QLabel(Form)
        self.imageOutput.setPixmap(QtGui.QPixmap(self.file_path))
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
        self.compareButton.clicked.connect(self.compareButtonFunction)
        self.verticalLayout.addWidget(self.compareButton)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.differentImageButton = QtWidgets.QPushButton(Form)
        self.differentImageButton.setObjectName("differentImageButton")
        self.differentImageButton.clicked.connect(self.differentImageButtonFunction)
        self.verticalLayout.addWidget(self.differentImageButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(314, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.saveButtonFunction)
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(313, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.setLayout(self.gridLayout)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.outputLabel.setText(_translate("Form", "OUTPUT"))
        self.compareButton.setText(_translate("Form", "COMPARE  IMAGES"))
        self.differentImageButton.setText(_translate("Form", "TRY DIFFERENT IMAGE"))
        self.saveButton.setText(_translate("Form", "SAVE IMAGE"))

    #####################################################################################################
    #                                       Button Functionality                                        #
    #####################################################################################################
    def differentImageButtonFunction(self):
        """
        Different Image Button Functionality

        Changes the selection of the application to the first page
        """ 
        # Change to first page
        if self.display is not None:
            self.display.close()
        self._parent.stackWidget.setCurrentIndex(0)

    def compareButtonFunction(self):
        """
        Compare Image Button Functionality

        Compare the input inmage with the output image
        """
        output_state = test_accuracy()
        dataset = self._parent.firstPageUI.getCheckBox()
        output_data = get_label_accuracy(dataset, output_state)
        self.display = compare_display(output_data)
        self.display.show()

    def saveButtonFunction(self):
        """
        Save Button Functionality

        Saves the image into local storage
        """
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "File Browser", "", "Image Files " + getAcceptInput())
        if fileName:
            with open(self.file_path, "rb") as read_file, open(fileName, "wb") as write_file:
                for data in read_file:
                    write_file.write(data)

    #####################################################################################################
    #                                         Helper Functions                                          #
    #####################################################################################################
    def setImage(self):
        """
        Helper Function

        Used to set the image based on the file path
        """
        self.imageOutput.setPixmap(QtGui.QPixmap(self.file_path).scaled(1080, 480, QtCore.Qt.KeepAspectRatio))