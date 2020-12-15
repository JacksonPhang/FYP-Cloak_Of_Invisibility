from PyQt5 import QtCore, QtGui, QtWidgets

"""
The second page of the User Interface
Do not edit unless you know what's up
"""
class Ui_FormTwo(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self._parent = parent

        Form = QtWidgets.QWidget()
        Form.setObjectName("Form")
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
        self.differentImageButton.clicked.connect(self.differentImageButtonFunction)
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

    #####################################################################################################
    #                                       Button Functionality                                        #
    #####################################################################################################
    """
    Different Image Button Functionality

    Changes the selection of the application to the first page
    """ 
    def differentImageButtonFunction(self):
        # Change to first page
        self._parent.stackWidget.setCurrentIndex(0)