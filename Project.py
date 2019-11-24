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
        self.room1s = 0
        self.room2s = 0
        self.room3s = 0
        self.room4s = 0

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
        self.room1in = QtWidgets.QTextEdit(self.centralwidget)
        self.room1in.setGeometry(QtCore.QRect(10, 50, 104, 41))
        self.room1in.setAccessibleName("")
        self.room1in.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.room1in.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.room1in.setDocumentTitle("")
        self.room1in.setOverwriteMode(False)
        self.room1in.setTabStopWidth(200)
        self.room1in.setPlaceholderText("")
        self.room1in.setObjectName("room1in")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 100, 104, 41))
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setObjectName("textEdit_2")
        self.room1in_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.room1in_2.setGeometry(QtCore.QRect(240, 100, 91, 41))
        self.room1in_2.setAccessibleName("")
        self.room1in_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.room1in_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.room1in_2.setDocumentTitle("")
        self.room1in_2.setOverwriteMode(False)
        self.room1in_2.setTabStopWidth(200)
        self.room1in_2.setPlaceholderText("")
        self.room1in_2.setObjectName("room1in_2")
        self.room1in_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.room1in_3.setGeometry(QtCore.QRect(240, 50, 91, 41))
        self.room1in_3.setAccessibleName("")
        self.room1in_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.room1in_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.room1in_3.setDocumentTitle("")
        self.room1in_3.setOverwriteMode(False)
        self.room1in_3.setTabStopWidth(200)
        self.room1in_3.setPlaceholderText("")
        self.room1in_3.setObjectName("room1in_3")
        self.Adultmany = QtWidgets.QSpinBox(self.centralwidget)
        self.Adultmany.setGeometry(QtCore.QRect(340, 50, 61, 21))
        self.Adultmany.setMaximum(2)
        self.Adultmany.setObjectName("Adultmany")
        self.Kidmany = QtWidgets.QSpinBox(self.centralwidget)
        self.Kidmany.setGeometry(QtCore.QRect(340, 100, 61, 21))
        self.Kidmany.setMaximum(2)
        self.Kidmany.setObjectName("Kidmany")
        self.room1in_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.room1in_4.setGeometry(QtCore.QRect(10, 0, 101, 41))
        self.room1in_4.setAccessibleName("")
        self.room1in_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.room1in_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.room1in_4.setDocumentTitle("")
        self.room1in_4.setOverwriteMode(False)
        self.room1in_4.setTabStopWidth(200)
        self.room1in_4.setPlaceholderText("")
        self.room1in_4.setObjectName("room1in_4")
        self.type = QtWidgets.QTextEdit(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(240, 0, 151, 41))
        self.type.setObjectName("type")
        self.creditcard = QtWidgets.QTextEdit(self.centralwidget)
        self.creditcard.setGeometry(QtCore.QRect(10, 200, 221, 41))
        self.creditcard.setObjectName("creditcard")

        self.pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton.setGeometry(QtCore.QRect(240, 200, 61, 41))
        self.pushbutton.setObjectName("pushbutton")
        self.pushbutton.clicked.connect(self.standard_room)

        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(120, 0, 41, 21))
        self.spinBox_3.setMaximum(4)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.valueChanged.connect(self.standard_room)

        self.status = QtWidgets.QTextEdit(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(170, 0, 61, 41))
        self.status.setObjectName("status")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(10, 150, 104, 41))
        self.textEdit_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_5.setObjectName("textEdit_5")
        self.room1in_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.room1in_5.setGeometry(QtCore.QRect(240, 150, 91, 41))
        self.room1in_5.setAccessibleName("")
        self.room1in_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.room1in_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.room1in_5.setDocumentTitle("")
        self.room1in_5.setOverwriteMode(False)
        self.room1in_5.setTabStopWidth(200)
        self.room1in_5.setPlaceholderText("")
        self.room1in_5.setObjectName("room1in_5")
        self.pay = QtWidgets.QTextEdit(self.centralwidget)
        self.pay.setGeometry(QtCore.QRect(340, 150, 61, 41))
        self.pay.setObjectName("pay")
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
    def standard_room(self):
        check = self.spinBox_3.value()
        if check == 1:
            self.room1
        print(check)
    def room1(self):
        if self.room1s == 0:
            pass
    def room2(self):
        pass
    def room3(self):
        pass
    def room4(self):
        pass
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkin.setDisplayFormat(_translate("MainWindow", "dd/M/yyyy"))
        self.checkout.setDisplayFormat(_translate("MainWindow", "dd/M/yyyy"))
        self.room1in.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Check-In</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Check-Out</span></p></body></html>"))
        self.room1in_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Kid</span></p></body></html>"))
        self.room1in_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Adult</span></p></body></html>"))
        self.room1in_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">Room</span></p></body></html>"))
        self.pushbutton.setText(_translate("MainWindow", "Booking"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Credit card</span></p></body></html>"))
        self.room1in_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Cost</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
