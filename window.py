# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admin\Desktop\ปกคลิป.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from standard import Standard
from suite import suite
from deluxe import deluxe
from Superior import superior
class Ui_MainWindows(object):
    def setupUi(self, MainWindow):
        """main window"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 300, 400, 300))
        self.pushButton_3.setIcon(QtGui.QIcon('Superior_room.jpg'))
        self.pushButton_3.setIconSize(QtCore.QSize(550,250))
        self.pushButton_3.setGeometry(QtCore.QRect(0,300,400,300))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.connecter_tosuperior)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 0, 400, 300))
        self.pushButton_4.setIcon(QtGui.QIcon('Deluxe_room.jpg'))
        self.pushButton_4.setIconSize(QtCore.QSize(550,250))
        self.pushButton_4.setGeometry(QtCore.QRect(400,0,400,300))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.connecter_todeluxe)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.pushButton_6.setIcon(QtGui.QIcon('Standard_room.jpg'))
        self.pushButton_6.setIconSize(QtCore.QSize(550,250))
        self.pushButton_6.setGeometry(QtCore.QRect(0,0,400,300))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.connecter_tostandard)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 300, 400, 300))
        self.pushButton_5.setIcon(QtGui.QIcon('Suite_room.jpg'))
        self.pushButton_5.setIconSize(QtCore.QSize(550,250))
        self.pushButton_5.setGeometry(QtCore.QRect(400, 300, 400, 300))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.connecter_tosuite)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def connecter_todeluxe(self):
        """connect to deluxe room menu"""
        self.window = QtWidgets.QMainWindow()
        self.Project = deluxe()
        self.Project.setupUi(self.window)
        self.window.show()

    def connecter_tosuperior(self):
        """connect to superior room menu"""
        self.window = QtWidgets.QMainWindow()
        self.Project = superior()
        self.Project.setupUi(self.window)
        self.window.show()


    def connecter_tostandard(self):
        """connect to standard room menu"""
        #print(self.pushButton_3.clicked())
        self.window = QtWidgets.QMainWindow()
        self.Project = Standard()
        self.Project.setupUi(self.window)
        self.window.show()

    def connecter_tosuite(self):
        """connect to suite room menu"""
        #print(self.pushButton_3.clicked())
        self.window = QtWidgets.QMainWindow()
        self.Project = suite()
        self.Project.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        """settext in main window"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main"))
        self.pushButton_3.setText(_translate("MainWindow", ""))
        self.pushButton_4.setText(_translate("MainWindow", ""))
        self.pushButton_6.setText(_translate("MainWindow", ""))
        self.pushButton_5.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindows()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
