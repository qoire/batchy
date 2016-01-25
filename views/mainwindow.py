# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Yao\Documents\GitHub\batchy\views\mainwindow.ui'
#
# Created: Sun Jan 24 21:08:50 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 348)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(310, 250, 41, 23))
        self.startButton.setObjectName("startButton")
        self.plusButton = QtGui.QPushButton(self.centralwidget)
        self.plusButton.setGeometry(QtCore.QRect(380, 210, 21, 23))
        self.plusButton.setObjectName("plusButton")
        self.minusButton = QtGui.QPushButton(self.centralwidget)
        self.minusButton.setGeometry(QtCore.QRect(350, 210, 21, 23))
        self.minusButton.setObjectName("minusButton")
        self.videoListWidget = QtGui.QListWidget(self.centralwidget)
        self.videoListWidget.setGeometry(QtCore.QRect(10, 10, 391, 192))
        self.videoListWidget.setObjectName("videoListWidget")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 250, 41, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 230, 291, 51))
        self.groupBox.setObjectName("groupBox")
        self.configComboBox = QtGui.QComboBox(self.groupBox)
        self.configComboBox.setGeometry(QtCore.QRect(10, 20, 171, 22))
        self.configComboBox.setObjectName("configComboBox")
        self.configNewBtn = QtGui.QPushButton(self.groupBox)
        self.configNewBtn.setGeometry(QtCore.QRect(190, 20, 41, 23))
        self.configNewBtn.setObjectName("configNewBtn")
        self.configEditBtn = QtGui.QPushButton(self.groupBox)
        self.configEditBtn.setGeometry(QtCore.QRect(240, 20, 41, 23))
        self.configEditBtn.setObjectName("configEditBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRemoveAll = QtGui.QAction(MainWindow)
        self.actionRemoveAll.setObjectName("actionRemoveAll")
        self.actionCredits = QtGui.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionRemoveAll)
        self.menuAbout.addAction(self.actionCredits)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.plusButton.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.minusButton.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Config", None, QtGui.QApplication.UnicodeUTF8))
        self.configNewBtn.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.configEditBtn.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveAll.setText(QtGui.QApplication.translate("MainWindow", "Remove All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCredits.setText(QtGui.QApplication.translate("MainWindow", "Credits", None, QtGui.QApplication.UnicodeUTF8))

