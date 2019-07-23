import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "PyQt5 Window"
        top = 500
        left = 200
        width = 300
        height = 250
        iconName = "./icons/home.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)

        self.UiComponents()
        self.show()

    def UiComponents(self):
        button = QPushButton("Click Me", self)
        # button.move(50,50)
        button.setGeometry(QRect(100,100, 111, 50))
        button.setIcon(QtGui.QIcon("./icons/home.png"))
        button.setIconSize(QtCore.QSize(40,40))
        button.setToolTip("<h2>This Is Click Me Button<h2>")

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())