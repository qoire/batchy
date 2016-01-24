import sys, os
sys.path.append(os.path.abspath('..'))
import globvar
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

class DataModel(Model):
    class Meta:
        database = globvar.db