from pyrogram import Client, Filters, InlineQuery

from bot.functions import inlinekeyboard


def check_func(_, inline_query: InlineQuery):
    """@NintendoFCode_bot bindgame"""
    data = inline_query.query.split()
    if data[0] == 'bindgame':
        return True


@Client.on_inline_query(Filters.create(check_func))
def bindgame(client: Client, inline_query: InlineQuery):
    keyboard = inlinekeyboard.bindgame()
    inline_query.answer(keyboard, cache_time=0)
