from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import DataModel
import datetime

class VideosModel(DataModel.DataModel):
    url = CharField(unique = True)
    output_url = CharField(unique = True)
    status = CharField()
    current_session = BooleanField()
    created_date = DateTimeField(default=datetime.datetime.now)