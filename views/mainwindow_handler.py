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
from models.ConfigModel import ConfigModel
from views.mainwindow import Ui_MainWindow
from controller.VideosController import *
from controller.ConfigController import *

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

        # Class parameters
        self.profile_str = "* Temp Profile *"

        # connect database!
        globvar.db.connect()

        # setup tables
        ConfigModel.create_table(True)
        VideosModel.create_table(True)
        ProgModel.create_table(True)

        ProgModel.create_or_get(
            times_opened = '0',
            x264_location = self._x264_location,
            x264_64_location = self._x264_64_location,
            mp4box_location = self._mp4box_location,
            mkvmerge_location = self._mkvmerge_location,
            mkvextract_location = self._mkvextract_location)

        # set up controllers
        self._videosController = VideosController()
        self._configController = ConfigController()

        self._configController.createInitial()
        self._configController.createTempProfile()

        self.setupInitialConfigView()


    def setupInitialConfigView(self):
        # setup listview
        videoPaths = self._videosController.getCurrent()
        for p in videoPaths:
            self.ui.videoListWidget.addItem(p.url)

        # config_page combo boxes
        self.ui.comboBoxTuning.clear()
        for i in globvar.tuningParameters:
            self.ui.comboBoxTuning.addItem(i)

        self.ui.comboBoxOutputContainer.clear()
        for i in globvar.outputContainers:
            self.ui.comboBoxOutputContainer.addItem(i)

        # Setup Views based on database
        self.ui.configComboBox.clear()
        config_query = ConfigModel.select(ConfigModel)
        for config in config_query:
            if config.name != 'TempProfile':
                self.ui.configComboBox.addItem(config.name)

        config_amt = 0
        for config in config_query:
            config_amt = config_amt + 1

        if config_amt == 1:
            # This means only profile available is TempProfile
            self.ui.configComboBox.addItem(self.profile_str)
        elif config_amt == 0:
            # Something is horribly wrong
            resetConfigState()

        # We load initial based on the [0] entry of the config table
        self.setCheckBoxEncodex264State(config_query[0])

        # Slider
        self.setSliderx264Quality(config_query[0])

        # Output Tuning
        self.setComboBoxTuningParameter(config_query[0])

        # Connections
        # page UI elements
        self.ui.startButton.clicked.connect(self.__startButton)

        # menu UI elements
        self.ui.actionOpen.triggered.connect(self.__actionOpen)
        self.ui.actionRemoveAll.triggered.connect(self.__actionRemoveAll)
        self.ui.comboBoxTuning.currentIndexChanged.connect(
            self.__comboBoxTuningCurrentIndexChanged)
        self.ui.comboBoxOutputContainer.currentIndexChanged.connect(
            self.__comboBoxOutputContainerCurrentIndexChanged)
        self.ui.configComboBox.currentIndexChanged.connect(
            self.__comboBoxConfigCurrentIndexChanged)

        # config_page elements
        self.ui.sliderx264Quality.setMinimum(0)
        self.ui.sliderx264Quality.setMaximum(30)
        self.ui.sliderx264Quality.setTickInterval(1);
        self.ui.sliderx264Quality.valueChanged.connect(
            self.__sliderx264Quality)

        self.ui.checkBoxEncodex264.stateChanged.connect(
            self.__checkBoxEncodex264)

    def resetConfigState(self):
        pass

    # Setters for manipulating the view
    # Try to uniformly define the input parameter for any of these functions
    # As a single query row
    def setSliderx264Quality(self, q):
        self.ui.sliderx264Quality.setValue(q.x264_quality)

    def setCheckBoxEncodex264State(self, q):
        if q.encode == True:
            self.ui.checkBoxEncodex264.setCheckState(Qt.checked)
        else:
            self.ui.checkBoxEncodex264.setCheckState(Qt.Unchecked)

    def setComboBoxTuningParameter(self, q):
        tuning = q.x264_tuning

        if tuning == globvar.tuningParameters[0]:
            self.ui.comboBoxTuning.setCurrentIndex(0)
        elif tuning == globvar.tuningParameters[1]:
            self.ui.comboBoxTuning.setCurrentIndex(1)
        elif tuning == globvar.tuningParameters[2]:
            self.ui.comboBoxTuning.setCurrentIndex(2)
        elif tuning == globvar.tuningParameters[3]:
            self.ui.comboBoxTuning.setCurrentIndex(3)
        elif tuning == globvar.tuningParameters[4]:
            self.ui.comboBoxTuning.setCurrentIndex(4)
        elif tuning == globvar.tuningParameters[5]:
            self.ui.comboBoxTuning.setCurrentIndex(5)
        elif tuning == globvar.tuningParameters[6]:
            self.ui.comboBoxTuning.setCurrentIndex(6)
        elif tuning == globvar.tuningParameters[7]:
            self.ui.comboBoxTuning.setCurrentIndex(7)
        else:
            # This shouldnt happen (but just in case)
            self.ui.comboBoxTuning.setCurrentIndex(0)

    def setConfigBoxToTemp(self):
        if globvar.isProfileTempDisplayed == False:
            self.ui.configComboBox.addItem(self.profile_str)
            index = self.ui.configComboBox.findText(self.profile_str)
            self.ui.configComboBox.setCurrentIndex(index)
            globvar.isProfileTempDisplayed = True
        else:
            index = self.ui.configComboBox.findText(self.profile_str)
            self.ui.configComboBox.setCurrentIndex(index)

    def setTempProfileIfRequired(self):
        if globvar.isProfileTemp == False:
            config_index, config_q = self.getCurrentConfig()
            self._configController.copySelectedConfigToTemp(config_index)
            self.setConfigBoxToTemp()
        globvar.isProfileTemp = True


    # Getters
    # Do not modify the model from here, add such functions
    # To respective controller

    def getCurrentConfig(self):
        config_index = self.ui.configComboBox.currentIndex()
        return config_index, (ConfigModel.select(ConfigModel))[config_index]

    # Signal Handlers

    # View utility functions

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

    def __sliderx264Quality(self):
        output_str = str(self.ui.sliderx264Quality.value()) + ' '
        s_val = self.ui.sliderx264Quality.value()

        if (s_val == 0):
            output_str = output_str + 'Lossless'
        elif (s_val > 0 and s_val <= 17):
            output_str = output_str + 'High Quality - Large Filesize'
        elif (s_val > 17 and s_val <= 23):
            output_str = output_str + 'Recommended Quality - Medium Filesize'
        elif (s_val > 23):
            output_str = output_str + 'Yuck'

        self.setTempProfileIfRequired()
        self.ui.labelx264Recommendation.setText(output_str)

    def __comboBoxTuningCurrentIndexChanged(self, i):
        self.setTempProfileIfRequired()

    def __comboBoxOutputContainerCurrentIndexChanged(self, i):
        self.setTempProfileIfRequired()

    def __comboBoxConfigCurrentIndexChanged(self, i):
        if self.ui.configComboBox.currentText != self.profile_str:
            globvar.isProfileTemp = False

    def __checkBoxEncodex264(self, i):
        self.setTempProfileIfRequired()


    # Keyboard handler
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            deleteList = []
            for item in self.ui.videoListWidget.selectedItems():
                deleteList.append(item.text())
                self.ui.videoListWidget.takeItem(self.ui.videoListWidget.row(item))

            # delete from database
            self._videosController.deleteFromList(deleteList)
