import sys
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout
from PyQt5 import QtGui

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.top = 500
        self.left = 200
        self.width = 300
        self.height = 250
        self.iconName = "./icons/home.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        label = QLabel("This is PyQt5 Label")
        vbox.addWidget(label)

        label2 = QLabel("This is PyQt5 GUI Application Development")
        label2.setFont(QtGui.QFont("Sanserif ", 20))
        label2.setStyleSheet('color : red')
        vbox.addWidget(label2)

        self.setLayout(vbox)

        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())