
# D:\MyClasses\Freshman_Summer\python\big_homework\QtApp_GenderRecog>python D:\Anaconda3\Anaconda3\Library\bin\pyside2-uic traindlg.ui
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'traindlg.ui'
#
# Created: Sun Aug 15 23:26:18 2021
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_traindlg(object):
    def setupUi(self, traindlg):
        traindlg.setObjectName("traindlg")
        traindlg.resize(400, 200)
        traindlg.setMinimumSize(QtCore.QSize(400, 200))
        traindlg.setMaximumSize(QtCore.QSize(400, 200))
        self.progresslabel = QtWidgets.QLabel(traindlg)
        self.progresslabel.setGeometry(QtCore.QRect(98, 30, 200, 45))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.progresslabel.setFont(font)
        self.progresslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.progresslabel.setObjectName("progresslabel")
        self.BeginButton = QtWidgets.QPushButton(traindlg)
        self.BeginButton.setEnabled(True)
        self.BeginButton.setGeometry(QtCore.QRect(110, 110, 175, 45))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        self.BeginButton.setFont(font)
        self.BeginButton.setObjectName("BeginButton")

        self.retranslateUi(traindlg)
        QtCore.QMetaObject.connectSlotsByName(traindlg)

    def retranslateUi(self, traindlg):
        traindlg.setWindowTitle(QtWidgets.QApplication.translate("traindlg", "Train", None, -1))
        self.progresslabel.setText(QtWidgets.QApplication.translate("traindlg", "Prepare", None, -1))
        self.BeginButton.setText(QtWidgets.QApplication.translate("traindlg", "Get Model", None, -1))

