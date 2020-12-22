# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchfacebook.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #MainMenu Windows
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtLink = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLink.setGeometry(QtCore.QRect(100, 80, 300, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        #Textbox
        self.txtLink.setFont(font)
        self.txtLink.setObjectName("txtLink")
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        #Button
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(405, 80, 80, 25))
        self.btnSearch.setFont(font)
        self.btnSearch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSearch.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnSearch.setObjectName("btnSearch")

        self.btnSearch.clicked.connect(self.on_click_search)

        #Label
        self.lbApplication = QtWidgets.QLabel(self.centralwidget)
        self.lbApplication.setGeometry(QtCore.QRect(70, 20, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbApplication.setFont(font)
        self.lbApplication.setObjectName("lbApplication")
        self.txtResult = QtWidgets.QTextEdit(self.centralwidget)
        self.txtResult.setGeometry(QtCore.QRect(60, 120, 480, 150))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        #TextArea Result
        self.txtResult.setFont(font)
        self.txtResult.setObjectName("txtResult")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Search Facebook"))
        self.btnSearch.setText(_translate("MainWindow", "Search"))
        self.lbApplication.setText(_translate("MainWindow", "TÌM KIẾM THÔNG TIN TÀI KHOẢN FACEBOOK"))

    def on_click_search(self):
        txtLink = self.txtLink.text()
        if txtLink != "":
            message = "This is my link: " + txtLink
        else:
            message = "Oh No. This is empty!"
        QMessageBox.question(QWidget, "Message", message, QMessageBox.StandardButton(QMessageBox.Ok), defaultButton=QMessageBox.Ok)
        self.txtLink.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


