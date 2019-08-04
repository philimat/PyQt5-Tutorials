import sys
from PyQt5.QtWidgets import QDialog, QApplication, QGroupBox, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5 import QtGui, QtCore

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Radio Button"
        self.top = 300
        self.left = 400
        self.width = 400
        self.height = 100

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("./icons/home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.radioButton()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()

    def radioButton(self):
        self.groupBox = QGroupBox("What is Your Favorite Sport?")
        self.groupBox.setFont(QtGui.QFont("Sanserif", 13))

        hboxLayout = QHBoxLayout()

        self.radiobtn1 = QRadioButton("Football")
        self.radiobtn1.setChecked(True)
        self.radiobtn1.setIcon(QtGui.QIcon("./icons/football.png"))
        self.radiobtn1.setIconSize(QtCore.QSize(40,40))
        self.radiobtn1.setFont(QtGui.QFont("Sanserif", 13))
        self.radiobtn1.toggled.connect(self.OnRadioBtn)
        hboxLayout.addWidget(self.radiobtn1)

        self.radiobtn2 = QRadioButton("Cricket")
        self.radiobtn2.setIcon(QtGui.QIcon("./icons/cricket.png"))
        self.radiobtn2.setIconSize(QtCore.QSize(40,40))
        self.radiobtn2.setFont(QtGui.QFont("Sanserif", 13))
        self.radiobtn2.toggled.connect(self.OnRadioBtn)
        hboxLayout.addWidget(self.radiobtn2)

        self.radiobtn3 = QRadioButton("Tennis")
        self.radiobtn3.setIcon(QtGui.QIcon("./icons/tennis.png"))
        self.radiobtn3.setIconSize(QtCore.QSize(40,40))
        self.radiobtn3.setFont(QtGui.QFont("Sanserif", 13))
        self.radiobtn3.toggled.connect(self.OnRadioBtn)
        hboxLayout.addWidget(self.radiobtn3)

        self.groupBox.setLayout(hboxLayout)

    def OnRadioBtn(self):
        radioBtn = self.sender()

        if radioBtn:
            self.label.setText("You Have Selected " + radioBtn.text())

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())