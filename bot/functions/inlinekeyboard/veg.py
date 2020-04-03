from .. import configure
from pyrogram import InlineQueryResultArticle, InputTextMessageContent


def veg(user_id: int = 0, price: int = 0):
    if price:
        text = InputTextMessageContent('/acnh veg {price}'.format(price=price))
    else:
        text = InputTextMessageContent('婐 4 北七，我不知道甚麼 4 數字')
        keyboard = None

    money_icon = configure.get('ACNH', 'money')
    result = [
        InlineQueryResultArticle(
            input_message_content=text, title='更新大頭菜價格', thumb_url=money_icon)
    ]
    return result
