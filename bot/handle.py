import logging
import coloredlogs
from pyrogram import Client
from .functions import configure

logger = logging.getLogger(__name__)
level = configure.get('bot', 'logging')
coloredlogs.install(level=level, logger=logger)


def run(self):
    app = Client("nintendo", config_file='pyrogram.ini',
                 plugins=dict(root='./bot/plugins'), workers=128)
    app.start()
    myself = app.get_me()
    name = myself.first_name + ' ' + myself.username
    logger.info(name)
