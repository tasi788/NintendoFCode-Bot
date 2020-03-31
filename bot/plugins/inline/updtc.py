"""
更新大頭菜價格。
"""

from pyrogram import (InlineQuery, Client, Filters, InlineKeyboardButton,
                      InlineKeyboardMarkup)


def check_func(_, inline_query: InlineQuery):
    """@NintendoFCode_bot updtc 547"""
    data = inline_query.data.split()
    if len(data) != 2:
        return False
    if data[0] == 'updtc':
        return True


@Client.on_inline_query(Filters.create(check_func))
def updtc(client: Client, inline_query: InlineQuery):
    data = inline_query.data.split()
    price = data[1]
    # TODO: 檢測 reply_markup
