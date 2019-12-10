# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admin\Desktop\Reset controler.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Resetcontrol(object):
    def setupUi(self, Resetcontrol):
        """show reset window"""
        self.conn = sqlite3.connect('test.db')
        self.cur = self.conn.cursor()

        Resetcontrol.setObjectName("Resetcontrol")
        Resetcontrol.resize(493, 414)
        self.centralwidget = QtWidgets.QWidget(Resetcontrol)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 60, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 200, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 120, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 260, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 260, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(290, 120, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 140, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentTextChanged.connect(self.checkstandard)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 280, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.currentTextChanged.connect(self.checksuperior)

        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(360, 140, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.currentTextChanged.connect(self.checkdeluxe)

        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(360, 280, 69, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.currentTextChanged.connect(self.checksuite)

        Resetcontrol.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Resetcontrol)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 21))
        self.menubar.setObjectName("menubar")
        Resetcontrol.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Resetcontrol)
        self.statusbar.setObjectName("statusbar")
        Resetcontrol.setStatusBar(self.statusbar)

        self.retranslateUi(Resetcontrol)
        QtCore.QMetaObject.connectSlotsByName(Resetcontrol)

    def retranslateUi(self, Resetcontrol):
        """settext in reset window"""
        _translate = QtCore.QCoreApplication.translate
        Resetcontrol.setWindowTitle(_translate("Resetcontrol", "Reset Controler"))
        self.label.setText(_translate("Resetcontrol", "Reset Controler"))
        self.label_2.setText(_translate("Resetcontrol", "Standard Room"))
        self.label_3.setText(_translate("Resetcontrol", "Deluxe Room"))
        self.label_4.setText(_translate("Resetcontrol", "Superior Room"))
        self.label_5.setText(_translate("Resetcontrol", "Suite Room"))
        self.label_6.setText(_translate("Resetcontrol", "Room"))
        self.label_7.setText(_translate("Resetcontrol", "Room"))
        self.label_8.setText(_translate("Resetcontrol", "Room"))
        self.label_9.setText(_translate("Resetcontrol", "Room"))

        self.comboBox.setItemText(0, _translate("Resetcontrol", "-"))
        self.comboBox.setItemText(1, _translate("Resetcontrol", "1"))
        self.comboBox.setItemText(2, _translate("Resetcontrol", "2"))
        self.comboBox.setItemText(3, _translate("Resetcontrol", "3"))
        self.comboBox.setItemText(4, _translate("Resetcontrol", "4"))

        self.comboBox_2.setItemText(0, _translate("Resetcontrol", "-"))
        self.comboBox_2.setItemText(1, _translate("Resetcontrol", "1"))
        self.comboBox_2.setItemText(2, _translate("Resetcontrol", "2"))
        self.comboBox_2.setItemText(3, _translate("Resetcontrol", "3"))
        self.comboBox_2.setItemText(4, _translate("Resetcontrol", "4"))

        self.comboBox_3.setItemText(0, _translate("Resetcontrol", "-"))
        self.comboBox_3.setItemText(1, _translate("Resetcontrol", "1"))
        self.comboBox_3.setItemText(2, _translate("Resetcontrol", "2"))
        self.comboBox_3.setItemText(3, _translate("Resetcontrol", "3"))
        self.comboBox_3.setItemText(4, _translate("Resetcontrol", "4"))

        self.comboBox_4.setItemText(0, _translate("Resetcontrol", "-"))
        self.comboBox_4.setItemText(1, _translate("Resetcontrol", "1"))
        self.comboBox_4.setItemText(2, _translate("Resetcontrol", "2"))
        self.comboBox_4.setItemText(3, _translate("Resetcontrol", "3"))
        self.comboBox_4.setItemText(4, _translate("Resetcontrol", "4"))

    def checkstandard(self):
        """reset standard room to empty"""
        a = self.comboBox.currentText()
        if a != "-":
            msg = QMessageBox()
            msg.setWindowTitle("Are You Sure")
            msg.setText("Are You Sure?")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            y = msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            x = msg.exec()
            if x == QMessageBox.Yes:
                self.cur.execute("""Update standard set status = 1 where rowid=(?)""", (a, ))
                self.conn.commit()

    def checksuperior(self):
        """reset superiorroom to empty"""
        a = self.comboBox_2.currentText()
        if a != "-":
            msg = QMessageBox()
            msg.setWindowTitle("Are You Sure")
            msg.setText("Are You Sure?")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            y = msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            x = msg.exec()
            if x == QMessageBox.Yes:
                self.cur.execute("""Update superior set status = 1 where rowid=(?)""", (a, ))
                self.conn.commit()            

    def checkdeluxe(self):
        """reset deluxe room to empty"""
        a = self.comboBox_3.currentText()
        if a != "-":
            msg = QMessageBox()
            msg.setWindowTitle("Are You Sure")
            msg.setText("Are You Sure?")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            y = msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            x = msg.exec()
            if x == QMessageBox.Yes:
                self.cur.execute("""Update deluxe set status = 1 where rowid=(?)""", (a, ))
                self.conn.commit()


    def checksuite(self):
        """reset suite room to empty"""
        a = self.comboBox_4.currentText()
        if a != "-":
            msg = QMessageBox()
            msg.setWindowTitle("Are You Sure")
            msg.setText("Are You Sure?")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            y = msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            x = msg.exec()
            if x == QMessageBox.Yes:
                self.cur.execute("""Update suite set status = 1 where rowid=(?)""", (a, ))
                self.conn.commit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Resetcontrol = QtWidgets.QMainWindow()
    ui = Ui_Resetcontrol()
    ui.setupUi(Resetcontrol)
    Resetcontrol.show()
    sys.exit(app.exec_())
