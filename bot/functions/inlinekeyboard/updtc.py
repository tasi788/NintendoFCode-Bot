from typing import Union
from pyrogram import InlineQueryResultArticle, InputMessageContent
from ..keyboard import updtc


def updtc(price: str):
    if price.isdigit():
        text = InputMessageContent('我的大頭菜價格是：{price}'.format(price=price))
        keyboard = updtc(int(price))
    else:
        text = InputMessageContent('婐 4 北七，我不知道甚麼 4 數字')
        keyboard = None

    result = [
        InlineQueryResultArticle(
            text=text, description='更新大頭菜價格', reply_markup=keyboard)
    ]
    return result
