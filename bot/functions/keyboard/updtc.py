from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup


def updtc(price: int):
    keyboard = [
        [
            InlineKeyboardButton(
                '✅ 確定', callback_data='set updtc {price}'.format(price=price))
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
