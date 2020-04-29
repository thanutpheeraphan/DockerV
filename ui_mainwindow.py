# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1109, 714)
        icon = QIcon()
        icon.addFile(u"images/docker_pic2.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(20, 150, 222, 48))
        self.commandLinkButton.setStyleSheet(u"background-color: rgb(235, 247, 255);")
        self.commandLinkButton_2 = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")
        self.commandLinkButton_2.setGeometry(QRect(20, 230, 222, 48))
        self.commandLinkButton_2.setStyleSheet(u"background-color: rgb(235, 247, 255);")
        self.commandLinkButton_3 = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setObjectName(u"commandLinkButton_3")
        self.commandLinkButton_3.setGeometry(QRect(20, 310, 222, 48))
        self.commandLinkButton_3.setStyleSheet(u"background-color: rgb(235, 247, 255);")
        self.commandLinkButton_4 = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_4.setObjectName(u"commandLinkButton_4")
        self.commandLinkButton_4.setGeometry(QRect(20, 390, 222, 48))
        self.commandLinkButton_4.setStyleSheet(u"background-color: rgb(235, 247, 255);")
        self.commandLinkButton_5 = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_5.setObjectName(u"commandLinkButton_5")
        self.commandLinkButton_5.setGeometry(QRect(20, 470, 222, 48))
        self.commandLinkButton_5.setStyleSheet(u"background-color: rgb(235, 247, 255);")
        self.change_widget = QWidget(self.centralwidget)
        self.change_widget.setObjectName(u"change_widget")
        self.change_widget.setGeometry(QRect(260, 10, 831, 661))
        self.change_widget.setStyleSheet(u"background-color: rgb(235, 247, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 61, 61))
        self.label.setPixmap(QPixmap(u"images/docker_pic2.png"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 50, 81, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DockerV", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton_3.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton_4.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton_5.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">DockerV</span></p></body></html>", None))
    # retranslateUi

