import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Events And Signals"
        self.top = 500
        self.left = 200
        self.width = 300
        self.height = 250
        iconName = "home.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateButton()
        self.show()

    def CreateButton(self):
        button = QPushButton("Close Application", self)
        # button.move(50,50)
        button.setGeometry(QRect(100, 100, 150, 50))
        button.setIcon(QtGui.QIcon("home.png"))
        button.setIconSize(QtCore.QSize(40,40))
        button.clicked.connect(self.ClickMe)

    def ClickMe(self):
        sys.exit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())