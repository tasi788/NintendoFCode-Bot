from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup


def veg():
    keyboard = [
        [
            InlineKeyboardButton(
                '我也要更新大頭菜價格！', switch_inline_query_current_chat='acnh veg')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
