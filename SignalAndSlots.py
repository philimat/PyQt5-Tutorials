import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "PyQt5 Events And Signals"
        top = 500
        left = 200
        width = 300
        height = 250
        iconName = "./icons/home.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)

        self.CreateButton()
        self.show()

    def CreateButton(self):
        button = QPushButton("Close Application", self)
        # button.move(50,50)
        button.setGeometry(QRect(100, 100, 150, 50))
        button.setIcon(QtGui.QIcon("./icons/home.png"))
        button.setIconSize(QtCore.QSize(40,40))
        button.clicked.connect(self.ClickMe)

    def ClickMe(self):
        sys.exit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())