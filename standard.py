# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PSIT\test\Project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from successpopup import Popup
from failpopup import failpopup


class Standard(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(407, 288)

        self.room1s = 0
        self.room2s = 0
        self.room3s = 0
        self.room4s = 0

        self.conn = sqlite3.connect('test.db')
        self.cur = self.conn.cursor()
        # self.cur.execute("select * from deluxe where status = (?)", (0, ))
        # print(self.cur.fetchall())

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.checkin = QtWidgets.QDateEdit(self.centralwidget)
        self.checkin.setGeometry(QtCore.QRect(120, 50, 110, 21))
        self.checkin.setCalendarPopup(True)
        self.checkin.setObjectName("checkin")

        self.checkout = QtWidgets.QDateEdit(self.centralwidget)
        self.checkout.setGeometry(QtCore.QRect(120, 100, 110, 22))
        self.checkout.setCalendarPopup(True)
        self.checkout.setObjectName("checkout")

        self.Adultmany = QtWidgets.QSpinBox(self.centralwidget)
        self.Adultmany.setGeometry(QtCore.QRect(340, 50, 61, 21))
        self.Adultmany.setMaximum(2)
        self.Adultmany.setObjectName("Adultmany")
        self.Adultmany.valueChanged.connect(self.calculate)

        self.Kidmany = QtWidgets.QSpinBox(self.centralwidget)
        self.Kidmany.setGeometry(QtCore.QRect(340, 100, 61, 21))
        self.Kidmany.setMaximum(2)
        self.Kidmany.setObjectName("Kidmany")
        self.Kidmany.valueChanged.connect(self.calculate)

        self.creditcard = QtWidgets.QTextEdit(self.centralwidget)
        self.creditcard.setGeometry(QtCore.QRect(10, 200, 221, 31))
        self.creditcard.setObjectName("creditcard")

        self.pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton.setGeometry(QtCore.QRect(240, 190, 61, 41))
        self.pushbutton.setObjectName("pushbutton")
        self.pushbutton.clicked.connect(self.connecter)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 7, 41, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("-")
        self.comboBox.addItem("1")
        self.comboBox.addItem("2")
        self.comboBox.addItem("3")
        self.comboBox.addItem("4")
        self.comboBox.currentTextChanged.connect(self.test)

        self.pay = QtWidgets.QTextEdit(self.centralwidget)
        self.pay.setGeometry(QtCore.QRect(340, 150, 61, 31))
        self.pay.setObjectName("pay")
        self.pay.setReadOnly(True)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.pay_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.pay_2.setGeometry(QtCore.QRect(170, 10, 61, 31))
        self.pay_2.setObjectName("pay_2")
        self.pay_2.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 407, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def test(self):
        a = self.comboBox.currentText()
        self.cur.execute("select status from standard where rowid=(?)", (a, ))
        c = self.cur.fetchall()[0][0]
        if a == '1' and c == 1:
            self.pay_2.setText("EMPTY")
        elif a == '1' and c == 0:
            self.pay_2.setText("FULL")
        elif a == '2' and c == 1:
            self.pay_2.setText("EMPTY")
        elif a == '2' and c == 0:
            self.pay_2.setText("FULL")
        elif a == '3' and c == 1:
            self.pay_2.setText("EMPTY")
        elif a == '3' and c == 0:
            self.pay_2.setText("FULL")
        elif a == '4' and c == 1:
            self.pay_2.setText("EMPTY")
        elif a == '4' and c == 0:
            self.pay_2.setText("FULL")

    def changedb(self):
        a = self.comboBox.currentText()
        self.cur.execute("""Update standard set status = 0 where rowid=(?)""", (a, ))
        self.conn.commit()
        self.pay_2.setText("FULL")

    def calculate(self):
        a = self.Adultmany.value()
        b = self.Kidmany.value()
        self.pay.setText(str((a * 2000)+(b * 1000)))

    def connecter(self):
        a = self.comboBox.currentText()
        self.cur.execute("select status from standard where rowid=(?)", (a, ))
        c = self.cur.fetchall()[0][0]
        if c == 1:
            self.window = QtWidgets.QMainWindow()
            self.Project = Popup()
            self.Project.setupUi(self.window)
            self.window.show()
            self.cur.execute("""Update standard set status = 0 where rowid=(?)""", (a, ))
            self.conn.commit()
            self.pay_2.setText("FULL")
        else:
            self.window = QtWidgets.QMainWindow()
            self.Project = failpopup()
            self.Project.setupUi(self.window)
            self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Booking"))
        self.checkin.setDisplayFormat(_translate("MainWindow", "dd/M/yyyy"))
        self.checkout.setDisplayFormat(_translate("MainWindow", "dd/M/yyyy"))
        self.pushbutton.setText(_translate("MainWindow", "Booking"))
        self.label.setText(_translate("MainWindow", "Room Number"))
        self.label_2.setText(_translate("MainWindow", "Check-In"))
        self.label_3.setText(_translate("MainWindow", "Check-Out"))
        self.label_4.setText(_translate("MainWindow", "Credit Card"))
        self.label_5.setText(_translate("MainWindow", "Adult"))
        self.label_6.setText(_translate("MainWindow", "Kid"))
        self.label_7.setText(_translate("MainWindow", "Cost"))
        self.label_8.setText(_translate("MainWindow", "Standard Room"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Standard()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
