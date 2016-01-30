from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('data.db')

tuningParameters = [
        'None',
        'Film',
        'Animation',
        'Grain',
        'Still Image',
        'PSNR',
        'SSIM',
        'Fast Decode'
    ]

outputContainers = [
        'MP4',
        'MKV'
    ]

isProfileTemp = False
