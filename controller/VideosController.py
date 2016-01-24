import sys, os
sys.path.append(os.path.abspath('..'))

from models.ProgModel import ProgModel
from models.VideosModel import VideosModel

VID_READY = 'ready'
VID_PROCESSING = 'processing'
VID_DONE = 'done'
VID_ERR = 'err'

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

        for videopath in filteredVideoPaths:
            video, created = VideosModel.create_or_get(
                url=videopath,
                output_url=videopath,
                current_session=True,
                status=VID_READY)

            if video != False:
                video.update(current_session=True, status=VID_READY)