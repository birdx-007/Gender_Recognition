
# D:\MyClasses\Freshman_Summer\python\big_homework\QtApp_GenderRecog>python D:\Anaconda3\Anaconda3\Library\bin\pyside2-uic window.ui
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sun Aug 15 23:25:46 2021
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 960)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(720, 960))
        Form.setMaximumSize(QtCore.QSize(720, 960))
        Form.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 248, 255);\n"
"font: 10pt \"Leelawadee UI\";")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(230, 790, 256, 91))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(253, 811, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Leelawadee UI\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.PredictButton = QtWidgets.QPushButton(Form)
        self.PredictButton.setGeometry(QtCore.QRect(270, 710, 175, 45))
        self.PredictButton.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.PredictButton.setObjectName("PredictButton")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(110, 100, 500, 500))
        self.graphicsView.setMinimumSize(QtCore.QSize(500, 500))
        self.graphicsView.setMaximumSize(QtCore.QSize(500, 500))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.RandomButton = QtWidgets.QPushButton(Form)
        self.RandomButton.setGeometry(QtCore.QRect(258, 640, 200, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RandomButton.sizePolicy().hasHeightForWidth())
        self.RandomButton.setSizePolicy(sizePolicy)
        self.RandomButton.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.RandomButton.setObjectName("RandomButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Gender Recognition", None, -1))
        self.PredictButton.setText(QtWidgets.QApplication.translate("Form", "Predict", None, -1))
        self.RandomButton.setText(QtWidgets.QApplication.translate("Form", "Random Photo", None, -1))

