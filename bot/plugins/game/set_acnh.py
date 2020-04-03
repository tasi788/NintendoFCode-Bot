from pyrogram import Client, CallbackQuery, Filters
from ...functions import inlinekeyboard
# bindgame acnh


def check_func(_, inline_query: CallbackQuery):
    # /bindgame acnh
    data = inline_query.query.split()
    if data[0:2] == ['bindgame', 'acnh']:
        return True


@Client.on_inline_query(Filters.create(check_func))
def acnh(client: Client, inline_query: CallbackQuery):
    data = inline_query.query.split()

    keyboard = inlinekeyboard.bindacnh(inline_query)

    inline_query.answer(keyboard, cache_time=0)
