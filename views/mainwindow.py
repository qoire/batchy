# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Yao\Documents\GitHub\batchy\views\mainwindow.ui'
#
# Created: Mon Jan 25 17:05:41 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(482, 0))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.videoListTab = QtGui.QWidget()
        self.videoListTab.setObjectName("videoListTab")
        self.gridLayout_3 = QtGui.QGridLayout(self.videoListTab)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.videoListWidget = QtGui.QListWidget(self.videoListTab)
        self.videoListWidget.setObjectName("videoListWidget")
        self.gridLayout_3.addWidget(self.videoListWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.videoListTab, "")
        self.configSettingsTab = QtGui.QWidget()
        self.configSettingsTab.setObjectName("configSettingsTab")
        self.gridLayout_4 = QtGui.QGridLayout(self.configSettingsTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBoxEncodex264 = QtGui.QCheckBox(self.configSettingsTab)
        self.checkBoxEncodex264.setEnabled(True)
        self.checkBoxEncodex264.setObjectName("checkBoxEncodex264")
        self.gridLayout_4.addWidget(self.checkBoxEncodex264, 2, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.configSettingsTab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelx264Quality = QtGui.QLabel(self.groupBox_2)
        self.labelx264Quality.setMaximumSize(QtCore.QSize(40, 20))
        self.labelx264Quality.setObjectName("labelx264Quality")
        self.horizontalLayout.addWidget(self.labelx264Quality)
        self.labelx264Recommendation = QtGui.QLabel(self.groupBox_2)
        self.labelx264Recommendation.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelx264Recommendation.setObjectName("labelx264Recommendation")
        self.horizontalLayout.addWidget(self.labelx264Recommendation)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sliderx264Quality = QtGui.QSlider(self.groupBox_2)
        self.sliderx264Quality.setOrientation(QtCore.Qt.Horizontal)
        self.sliderx264Quality.setObjectName("sliderx264Quality")
        self.verticalLayout.addWidget(self.sliderx264Quality)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelx264Tuning = QtGui.QLabel(self.groupBox_2)
        self.labelx264Tuning.setObjectName("labelx264Tuning")
        self.horizontalLayout_2.addWidget(self.labelx264Tuning)
        self.comboBoxTuning = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxTuning.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBoxTuning.setObjectName("comboBoxTuning")
        self.horizontalLayout_2.addWidget(self.comboBoxTuning)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelOutputContainer = QtGui.QLabel(self.configSettingsTab)
        self.labelOutputContainer.setMaximumSize(QtCore.QSize(100, 16777215))
        self.labelOutputContainer.setObjectName("labelOutputContainer")
        self.horizontalLayout_3.addWidget(self.labelOutputContainer)
        self.comboBoxOutputContainer = QtGui.QComboBox(self.configSettingsTab)
        self.comboBoxOutputContainer.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBoxOutputContainer.setObjectName("comboBoxOutputContainer")
        self.horizontalLayout_3.addWidget(self.comboBoxOutputContainer)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 4, 0, 1, 1)
        self.tabWidget.addTab(self.configSettingsTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setMaximumSize(QtCore.QSize(80, 50))
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 4, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.configComboBox = QtGui.QComboBox(self.groupBox)
        self.configComboBox.setObjectName("configComboBox")
        self.gridLayout_2.addWidget(self.configComboBox, 1, 0, 1, 1)
        self.startButton_2 = QtGui.QPushButton(self.groupBox)
        self.startButton_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.startButton_2.setObjectName("startButton_2")
        self.gridLayout_2.addWidget(self.startButton_2, 1, 2, 1, 1)
        self.configNewBtn = QtGui.QPushButton(self.groupBox)
        self.configNewBtn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.configNewBtn.setObjectName("configNewBtn")
        self.gridLayout_2.addWidget(self.configNewBtn, 1, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
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
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.videoListTab), QtGui.QApplication.translate("MainWindow", "Inputs", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxEncodex264.setText(QtGui.QApplication.translate("MainWindow", "Encode x264", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "x264 Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.labelx264Quality.setText(QtGui.QApplication.translate("MainWindow", "Quality", None, QtGui.QApplication.UnicodeUTF8))
        self.labelx264Recommendation.setText(QtGui.QApplication.translate("MainWindow", "Recommended", None, QtGui.QApplication.UnicodeUTF8))
        self.labelx264Tuning.setText(QtGui.QApplication.translate("MainWindow", "Tuning", None, QtGui.QApplication.UnicodeUTF8))
        self.labelOutputContainer.setText(QtGui.QApplication.translate("MainWindow", "Output Container", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.configSettingsTab), QtGui.QApplication.translate("MainWindow", "Config Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Config", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton_2.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.configNewBtn.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveAll.setText(QtGui.QApplication.translate("MainWindow", "Remove All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCredits.setText(QtGui.QApplication.translate("MainWindow", "Credits", None, QtGui.QApplication.UnicodeUTF8))

