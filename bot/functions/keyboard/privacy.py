from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup


def privacy():
    keyboard = [
        [
            InlineKeyboardButton(
                '✅ 開啟', callback_data='set privacy on'),
            InlineKeyboardButton(
                '❌ 關閉', callback_data='set privacy off')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
