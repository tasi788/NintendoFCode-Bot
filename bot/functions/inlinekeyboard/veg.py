from pyrogram import (InlineKeyboardButton, InlineKeyboardMarkup,
                      InlineQueryResultArticle, InputTextMessageContent)

from .. import configure


def inline_keyboard(user_id: int, price: int):
    keyboard = [
        [
            InlineKeyboardButton(
                '✅ 確定', callback_data='set acnh veg {price} {user_id}'.format(price=price, user_id=user_id))
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def veg(user_id: int = 0, price: int = 0):
    if price:
        text = InputTextMessageContent(
            '我的大頭菜價格是：`{price}`'.format(price=price), parse_mode='markdown')
        keyboard = inline_keyboard(user_id, price)
    else:
        text = InputTextMessageContent('婐 4 北七，我不知道甚麼 4 數字')
        keyboard = None

    money_icon = configure.get('ACNH', 'money')
    result = [
        InlineQueryResultArticle(
            input_message_content=text, title='更新大頭菜價格', reply_markup=keyboard, thumb_url=money_icon)
    ]
    return result
