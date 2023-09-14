import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("New window")
        self.setGeometry(300, 300, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('New Text')
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.new_button = QtWidgets.QPushButton(self)
        self.new_button.move(70, 150)
        self.new_button.setText('Button')
        self.new_button.setFixedWidth(200)

        self.new_button.clicked.connect(self.add_label)


    def add_label(self):
        self.new_text.setText('Second text')
        self.new_text.move(100, 50)
        self.new_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()

    # window.setWindowTitle("New window")
    # window.setGeometry(300, 300, 350, 200)

    # main_text = QtWidgets.QLabel(window)
    # main_text.setText('New Text')
    # main_text.move(100, 100)
    # main_text.adjustSize()

    # new_button = QtWidgets.QPushButton(window)
    # new_button.move(70, 150)
    # new_button.setText('Button')
    # new_button.setFixedWidth(200)

    # new_button.clicked.connect(add_label)

    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    application()

