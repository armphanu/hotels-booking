# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admin\Desktop\Project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(407, 288)
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
        self.Kidmany = QtWidgets.QSpinBox(self.centralwidget)
        self.Kidmany.setGeometry(QtCore.QRect(340, 100, 61, 21))
        self.Kidmany.setMaximum(2)
        self.Kidmany.setObjectName("Kidmany")
        self.creditcard = QtWidgets.QTextEdit(self.centralwidget)
        self.creditcard.setGeometry(QtCore.QRect(10, 200, 221, 41))
        self.creditcard.setObjectName("creditcard")
        self.pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton.setGeometry(QtCore.QRect(240, 200, 61, 41))
        self.pushbutton.setObjectName("pushbutton")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(120, 10, 41, 21))
        self.spinBox_3.setMaximum(4)
        self.spinBox_3.setObjectName("spinBox_3")
        self.pay = QtWidgets.QTextEdit(self.centralwidget)
        self.pay.setGeometry(QtCore.QRect(340, 150, 61, 31))
        self.pay.setObjectName("pay")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pay_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.pay_2.setGeometry(QtCore.QRect(170, 10, 61, 31))
        self.pay_2.setObjectName("pay_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 407, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
