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

    # add Video
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

    # delete Videos that are contained on list
    def deleteFromList(self, list):
        q = VideosModel.delete().where(VideosModel.url << list)
        q.execute()

    # get current
    def getCurrent(self):
        return VideosModel.select().where(VideosModel.current_session == True)

    # delete current videos
    def deleteCurrent(self):
        vid = VideosModel.select().where(VideosModel.current_session == True)
        vid.delete_instance()