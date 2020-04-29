import sys

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtUiTools

from button1_widget import UIWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.commandLinkButton.clicked.connect(self.check)
        self.ui.commandLinkButton_2.clicked.connect(self.open_widget1)

        self.img = QPixmap("/Users/New Account/Desktop/DockerV/images/docker_pic2.png")  #need to use absolute path
        self.ui.label.setPixmap(self.img)
        self.ui.label.show()

        self.setWindowIcon(self.img)

        # self.setWindowTitle("DockerV")
        # self.ui.commandLinkButton.setStyleSheet('border-color: rgb(0, 0, 127)')




    def open_widget1(self):
        self.Window = UIWindow(self)
        self.setWindowTitle("UIWindow")

        self.setCentralWidget(self.Window)
        self.show()

    def check(self):
        print("Hello World")










if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())