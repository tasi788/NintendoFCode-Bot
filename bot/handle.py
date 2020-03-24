import logging
import coloredlogs
from pyrogram import Client


class handle:
    def __init__(self):
        pass

    def run(self):
        app = Client("anonymous_sumbit", config_file='pyrogram.ini',
                     plugins=dict(root='./sumbitbot/plugins'), workers=128)
        app.start()
        myself = app.get_me()
        name = myself.first_name + ' ' + myself.username
        logger.info(name)
