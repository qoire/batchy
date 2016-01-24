import sys, os
sys.path.append(os.path.abs('..'))
from models.ProgModel import ProgModel

class ProgController(object):
    
    def __init__(self, db):
        # defaults
        self._os_ver = ''
        self._os_64 = ''
        self._x264_location = ''
        self._x264_64_location = ''
        self._avs4x264mod_location = ''
        self._mp4box_location = ''
        self._mkvmerge_location = ''
        self._avisynth_location = ''

        this._db = db

    def setDefault(self):
        