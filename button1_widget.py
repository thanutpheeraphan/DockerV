import sys

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtUiTools
from ui_mainwindow import Ui_MainWindow

class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.ToolsBTN = QPushButton('text', self)
        self.ToolsBTN.move(50, 350)
