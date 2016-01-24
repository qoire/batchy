from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import DataModel
import datetime

class ProgModel(DataModel.DataModel):
    times_opened = CharField(unique=True)
    x264_location = CharField(unique=True)
    x264_64_location = CharField(unique=True)
    mp4box_location = CharField(unique=True)
    mkvmerge_location = CharField(unique=True)
    mkvextract_location = CharField(unique=True)
