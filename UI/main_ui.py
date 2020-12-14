from PyQt5 import QtCore, QtGui, QtWidgets
from first_page import Ui_FormOne
from second_page import Ui_FormTwo

"""
Main UI class
Spawns both pages of the application
"""
class main_ui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Masking Application")
        self.setObjectName("maskingApplicationUI")

        ##############################################
        #    Create the Layout and the UI element    #
        ##############################################
        mainLayout = QtWidgets.QVBoxLayout()
        firstPageUI = Ui_FormOne(self)
        secondPageUI = Ui_FormTwo(self)

        self.stackWidget = QtWidgets.QStackedWidget()
        self.stackWidget.addWidget(firstPageUI) # Index 0
        self.stackWidget.addWidget(secondPageUI) # Index 1

        mainLayout.addWidget(self.stackWidget)
        self.setLayout(mainLayout)
        ##############################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_ui_reference = main_ui()
    main_ui_reference.show()
    sys.exit(app.exec_())