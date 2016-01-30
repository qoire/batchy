import sys, os
sys.path.append(os.path.abspath('..'))

from models.ConfigModel import ConfigModel
import globvar


class ConfigController(object):
    def __init__(self):
        pass

    def createInitial(self):
        # Create some initial models for the user to access
        ConfigModel.create_or_get(
            name='Basic',
            encode=False,
            x264_quality=21,
            x264_tuning=globvar.tuningParameters[0],
            output_container=globvar.outputContainers[0],
            available=True)

        ConfigModel.create_or_get(
            name='Basic Transcode',
            encode=True,
            x264_quality=21,
            x264_tuning=globvar.tuningParameters[0],
            output_container=globvar.outputContainers[0],
            available=True)

    def createTempProfile(self):
        ConfigModel.create_or_get(
            name='TempProfile',
            encode=True,
            x264_quality=21,
            x264_tuning=globvar.tuningParameters[0],
            output_container=globvar.outputContainers[0],
            available=False)

    def copySelectedConfigToTemp(self, i):
        q = ConfigModel.select(ConfigModel)
        temp_query = ConfigModel.update(
            encode = q[i].encode,
            x264_quality = q[i].x264_quality,
            x264_tuning = q[i].x264_tuning,
            output_container = q[i].output_container).where(
                ConfigModel.name == 'TempProfile'
                )
        temp_query.execute()
