from os import listdir
from os.path import isfile, join
import sys
import os
import peewee
from pymediainfo import MediaInfo
from PyQt4 import QtCore, QtGui, uic

# user defined
import globvar
from models.ProgModel import ProgModel
from models.VideosModel import VideosModel
from controller.VideosController import *

VID_READY = 'ready'
VID_PROCESSING = 'processing'
VID_DONE = 'done'
VID_ERR = 'err'

form_class = uic.loadUiType(os.path.join("views", "mainwindow.ui"))[0]

class MainWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self._x264_location = os.path.join("tools", "x264", "x264.exe")
        self._x264_64_location = os.path.join("tools", "x264", "x264_64.exe")
        self._mp4box_location = os.path.join("tools", "mp4box", "mp4box.exe")
        self._mkvmerge_location = os.path.join("tools", "mkvmerge", "mkvmerge.exe")
        self._mkvextract_location = os.path.join("tools", "mkvmerge", "mkvextract.exe")
        self._avisynth_location = ''

        self.isWindowFullScreen = False
        self.setFixedSize(410, 280)
        self.setupUi(self)

        # connect database!
        globvar.db.connect()

        # setup UI elements
        self.minusButton.clicked.connect(self.__minusButton)
        self.plusButton.clicked.connect(self.__plusButton)
        self.startButton.clicked.connect(self.__startButton)


        # Somewhat of a hack since QStringListModel can be edited regardless
        # Fix later
        self.listViewModel = QtGui.QStringListModel()
        self.listViewModel.setStringList(["Hello"])
        self.videoListView.setModel(self.listViewModel)
        self.videoListView.setWindowTitle("QListView")
        self.videoListView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

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

    # UI
    def __minusButton(self):
        pass

    def __plusButton(self):
        title = self.plusButton.text()
        videoPaths = []
        for path in QtGui.QFileDialog.getOpenFileNames(self, title):
            videoPaths.append(str(path))
        self._videosController.addVideo(videoPaths)

        # Display data to user
        videoPathsTotal = VideosModel.select().where(VideosModel.current_session == True)
        
        plist = []
        for p in videoPathsTotal:
            plist.append(p.url)

        # set the view based on model (MVC!)
        self.listViewModel.setStringList(plist)

    def __startButton(self):
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindowClass()
    mainWindow.show()
    app.exec_()