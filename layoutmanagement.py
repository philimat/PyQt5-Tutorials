import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Layout Management"
        self.top = 500
        self.left = 200
        self.width = 400
        self.height = 100
        self.iconName = "./icons/home.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox("What Is Your Favorite Sport?")
        hboxlayout = QHBoxLayout()

        button1 = QPushButton("Football", self)
        button1.setIcon(QtGui.QIcon("./icons/football.png"))
        button1.setIconSize(QtCore.QSize(40,40))
        button1.setMinimumHeight(40)
        hboxlayout.addWidget(button1)

        button2 = QPushButton("Cricket", self)
        button2.setIcon(QtGui.QIcon("./icons/cricket.png"))
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setMinimumHeight(40)
        hboxlayout.addWidget(button2)

        button3 = QPushButton("Tennis", self)
        button3.setIcon(QtGui.QIcon("./icons/tennis.png"))
        button3.setIconSize(QtCore.QSize(40,40))
        button3.setMinimumHeight(40)
        hboxlayout.addWidget(button3)

        self.groupBox.setLayout(hboxlayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())