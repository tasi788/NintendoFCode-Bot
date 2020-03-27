import logging
from typing import Union

import coloredlogs

import pymongo
from pymongo import ReadPreference
from pymongo.errors import ConnectionFailure

from . import configure

logger = logging.getLogger(__name__)
coloredlogs.install(level=configure.get('logging', 'status'), logger=logger)


def use_mongo(collection: Union[bool, str] = 'hexlightning', read_only: bool = False, read_nearest: bool = True):
    """
    use_mongo 快速ㄉ取用可愛ㄉ資料庫。
    """
    # read_preference how to talk with mongo
    if read_nearest:
        read_preference = ReadPreference.NEAREST
    elif read_only:
        read_preference = ReadPreference.SECONDARY_PREFERRED

    # make client
    try:
        mongo_url = configure.get('database', 'mongo')
        client = pymongo.MongoClient(mongo_url)
    except ConnectionFailure:
        logger.critical('MongoDB Connect Error')
    else:
        if collection:
            return client[collection]
        else:
            return client
