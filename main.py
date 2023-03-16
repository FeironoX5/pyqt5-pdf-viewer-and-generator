# Hi, thanks for your interest in the project!
# My name is Gleb Kiva, I enjoy web development and design.
# Subscribe to my Instagram https://www.instagram.com/gleb.kiva,
# if you want to support me and follow my activities.

import sys
from PyQt5 import QtWidgets

import design


class MyApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
