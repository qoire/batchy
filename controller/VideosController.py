import sys, os
sys.path.append(os.path.abspath('..'))

from models.ProgModel import ProgModel
from models.VideosModel import VideosModel

class VideosController(object):
    def __init__(self):
        pass

    def checkList(self, videoPaths):
        videoList = []
        for video in videoPaths:
            fn, fn_ext = os.path.splitext(video)
            if (fn_ext == '.mkv'):
                videoList.append(video)
        return videoList

    # VideosModel Controller
    def addVideo(self, videoPaths):
        filteredVideoPaths = self.checkList(videoPaths)
        print filteredVideoPaths

        for videopath in filteredVideoPaths:
            video, created = VideosModel.create_or_get(
                url=videopath,
                output_url=videopath,
                status=VID_READY)

            if video != False:
                print video