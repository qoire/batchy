from os import listdir
from os.path import isfile, join
import sys
import os
import peewee
from PySide import QtCore, QtGui
from PySide.QtCore import Qt

# user defined
import globvar
from models.ProgModel import ProgModel
from models.VideosModel import VideosModel
from views.mainwindow import Ui_MainWindow
from controller.VideosController import *

VID_READY = 'ready'
VID_PROCESSING = 'processing'
VID_DONE = 'done'
VID_ERR = 'err'

form_class = QtCore.QFile(os.path.join("views", "mainwindow.ui"))

class MainWindowClass(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._x264_location = os.path.join("tools", "x264", "x264.exe")
        self._x264_64_location = os.path.join("tools", "x264", "x264_64.exe")
        self._mp4box_location = os.path.join("tools", "mp4box", "mp4box.exe")
        self._mkvmerge_location = os.path.join("tools", "mkvmerge", "mkvmerge.exe")
        self._mkvextract_location = os.path.join("tools", "mkvmerge", "mkvextract.exe")
        self._avisynth_location = ''

        self.isWindowFullScreen = False
        self.setFixedSize(410, 322)

        # page UI elements
        self.ui.minusButton.clicked.connect(self.__minusButton)
        self.ui.plusButton.clicked.connect(self.__plusButton)
        self.ui.startButton.clicked.connect(self.__startButton)

        # menu UI elements
        self.ui.actionOpen.triggered.connect(self.__actionOpen)
        self.ui.actionRemoveAll.triggered.connect(self.__actionRemoveAll)

        # connect database!
        globvar.db.connect()

        # setup database
        try:
            globvar.db.create_tables([VideosModel, ProgModel])

            ProgModel.create(
                times_opened = '0',
                x264_location = self._x264_location,
                x264_64_location = self._x264_64_location,
                mp4box_location = self._mp4box_location,
                mkvmerge_location = self._mkvmerge_location,
                mkvextract_location = self._mkvextract_location)

        except peewee.OperationalError:
            pass

        # set up controllers
        self._videosController = VideosController()

        # setup listview
        videoPaths = self._videosController.getCurrent()
        for p in videoPaths:
            self.ui.videoListWidget.addItem(p.url)

    # base handler
    def __minusButton(self):
        pass

    def __plusButton(self):
        title = self.ui.plusButton.text()
        videoPaths = []
        for path in QtGui.QFileDialog.getOpenFileNames(self, title):
            videoPaths.append(path)

        self._videosController.addVideo(videoPaths[0])

        # Display data to user
        videoPathsTotal = self._videosController.getCurrent()
        
        plist = []
        for p in videoPathsTotal:
            self.ui.videoListWidget.addItem(p.url)

    def __startButton(self):
        pass

    # menu handler
    def __actionOpen(self):
        title = self.ui.actionOpen.text()
        videoPaths = []

        for path in QtGui.QFileDialog.getOpenFileNames(self, title):
            videoPaths.append(path)
        self._videosController.addVideo(videoPaths[0])

        # Retrieve from model and display
        videoPathsTotal = self._videosController.getCurrent()
        plist = []
        for p in videoPathsTotal:
            self.ui.videoListWidget.addItem(p.url)

    def __actionRemoveAll(self):
        self._videosController.deleteCurrent()
        videoPathsTotal = self._videosController.getCurrent()
        plist = []
        for p in videoPathsTotal:
            self.ui.videoListWidget.addItem(p.url)


    # Keyboard handler
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            deleteList = []
            for item in self.ui.videoListWidget.selectedItems():
                deleteList.append(item.text())
                self.ui.videoListWidget.takeItem(self.ui.videoListWidget.row(item))

            # delete from database
            self._videosController.deleteFromList(deleteList)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindowClass()
    mainWindow.show()
    app.exec_()