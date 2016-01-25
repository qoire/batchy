from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import DataModel
import datetime

class ConfigModel(DataModel.DataModel):
    encode = BooleanField()
    x264_quality = IntegerField()
    x264_tuning = CharField()
    output_container = CharField()