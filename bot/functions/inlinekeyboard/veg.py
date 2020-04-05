from .. import configure
from pyrogram import InlineQueryResultArticle, InputTextMessageContent


def veg(user_id: int = 0, price: int = 0):
    if price:
        text = InputTextMessageContent('/acnh veg {price}'.format(price=price))
        short = '更新大頭菜價格'
    else:
        text = InputTextMessageContent(
            '請先空格後再輸入正確的價格。\n例：`@NintendoFCode_bot acnh veg 153`')
        short = '請先空格後再輸入正確的價格。'

    money_icon = configure.get('ACNH', 'money')
    result = [
        InlineQueryResultArticle(
            input_message_content=text, title=short, thumb_url=money_icon)
    ]
    return result
