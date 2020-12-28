from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "\\UI")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "\\PyTorch")

from UI.first_page import Ui_FormOne
from UI.second_page import Ui_FormTwo

class main_ui(QtWidgets.QWidget):
    """
    Main UI class
    Spawns both pages of the application
    """

    def __init__(self):
        """
        Initialise Object

        Spawns the UI pages
        Adds pages into containers
        """
        super().__init__()
        
        self.setWindowTitle("Masking Application")
        self.setObjectName("maskingApplicationUI")

        ##############################################
        #    Create the Layout and the UI element    #
        ##############################################
        mainLayout = QtWidgets.QVBoxLayout()
        self.firstPageUI = Ui_FormOne(self)
        self.secondPageUI = Ui_FormTwo(self)

        self.stackWidget = QtWidgets.QStackedWidget()
        self.stackWidget.addWidget(self.firstPageUI) # Index 0
        self.stackWidget.addWidget(self.secondPageUI) # Index 1

        mainLayout.addWidget(self.stackWidget)
        self.setLayout(mainLayout)
        ##############################################

    #####################################################################################################
    #                                         Helper Functions                                          #
    #####################################################################################################
    def getPerturbationVariable(self):
        """ (Testing With Backend Required)
        Helper Function

        Used to obtain the input from the user based
        on the UI slider
        """
        # print(self.firstPageUI.perturbationSpinBox.value)
        return self.firstPageUI.perturbationSpinBox.value

    def getInputImage(self):
        """ (Testing With Backend Required)
        Helper Function

        Used to obtain the input image address from 
        the user
        """
        # print(self.firstPageUI.file_path)
        return self.firstPageUI.file_path

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_ui_reference = main_ui()
    main_ui_reference.show()
    sys.exit(app.exec_())