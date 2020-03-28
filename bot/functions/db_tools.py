import logging
from typing import Union

import coloredlogs

import pymongo
from pymongo.errors import ConnectionFailure

from . import configure

logger = logging.getLogger(__name__)
coloredlogs.install(level=configure.get('logging', 'status'), logger=logger)


def use_mongo(collection: Union[bool, str] = 'nintendo'):
    """use_mongo,
    快速ㄉ取用可愛ㄉ資料庫
    """
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
