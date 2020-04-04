from dacite import from_dict
from pyrogram import Client, Filters, InlineQuery

from ...functions import inlinekeyboard, db_tools
from ...types import user as users


def check_func(_, inline_query: InlineQuery):
    data = inline_query.query.split()
    if len(data) != 1:
        return False
    if data[0] == 'myacnh':
        return True


@Client.on_inline_query(Filters.create(check_func))
def myacnh(client: Client, inline_query: InlineQuery):
    mongo = db_tools.use_mongo()
    mongo_query = {'chat.id': inline_query.from_user.id}
    mongo_result = mongo.nintendo.find_one(mongo_query)

    if not isinstance(mongo_result, dict):
        return
    user = from_dict(data_class=users, data=mongo_result)
    keyboard = inlinekeyboard.myacnh(user)
    inline_query.answer(keyboard, cache_time=0)
