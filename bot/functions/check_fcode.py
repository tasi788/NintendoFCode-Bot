from typing import Union

from pyrogram import User

from ..types import user as users
from .db_tools import use_mongo


def chcek_fcode(user_id: Union(int, User)):
    if isinstance(user_id, User):
        user_id = user_id.id

    mongo = use_mongo()
    mongo_query = {'chat.id': user_id}
    mongo_result = mongo.nintendo.find_one(mongo_query)

    if not isinstance(mongo_result, dict):
        return False
