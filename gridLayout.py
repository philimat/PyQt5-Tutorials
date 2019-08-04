import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QVBoxLayout, QGridLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Grid Layout"
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

        self.CreateLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.setLayout(vbox)

        self.show()

    def CreateLayout(self):
        self.groupBox = QGroupBox("What Is Your Favorite Programming Language?")
        gridLayout = QGridLayout()

        button1 = QPushButton("Python", self)
        button1.setStyleSheet("color: black")
        button1.setIcon(QtGui.QIcon("./icons/python.png"))
        button1.setIconSize(QtCore.QSize(40,40))
        button1.setMinimumHeight(60)

        gridLayout.addWidget(button1, 0, 0)

        button2 = QPushButton("C++", self)
        button2.setStyleSheet("color: black")
        button2.setIcon(QtGui.QIcon("./icons/cpp.png"))
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setMinimumHeight(60)
        gridLayout.addWidget(button2, 0, 1)

        button3 = QPushButton("Swift", self)
        button3.setStyleSheet("color: black")
        button3.setIcon(QtGui.QIcon("./icons/swift.png"))
        button3.setIconSize(QtCore.QSize(40,40))
        button3.setMinimumHeight(60)
        gridLayout.addWidget(button3, 1, 0)

        button4 = QPushButton("C#", self)
        button4.setStyleSheet("color: black")
        button4.setIcon(QtGui.QIcon("./icons/csharp.png"))
        button4.setIconSize(QtCore.QSize(40,40))
        button4.setMinimumHeight(60)
        gridLayout.addWidget(button4, 1, 1)

        self.groupBox.setLayout(gridLayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())