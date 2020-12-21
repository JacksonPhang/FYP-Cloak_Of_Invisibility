from PyQt5 import QtCore, QtGui, QtWidgets
from first_page import Ui_FormOne
from second_page import Ui_FormTwo

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
        secondPageUI = Ui_FormTwo(self)

        self.stackWidget = QtWidgets.QStackedWidget()
        self.stackWidget.addWidget(self.firstPageUI) # Index 0
        self.stackWidget.addWidget(secondPageUI) # Index 1

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

    def getCheckBox(self):
        """ (Testing With Backend Required)
        Helper Function

        Used to obtain the checkbox value from the
        user
        """
        checkbox_value = {
            1: "CIFAR10",
            2: "MNIST"
        }
        return checkbox_value.get(self.buttonGroup.checkedId(), "Error")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_ui_reference = main_ui()
    main_ui_reference.show()
    sys.exit(app.exec_())