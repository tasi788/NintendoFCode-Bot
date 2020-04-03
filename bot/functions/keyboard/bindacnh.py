from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup


def bindacnh():
    keyboard = [
        [
            InlineKeyboardButton(
                '🔗 開始綁定', switch_inline_query_current_chat='bindgame acnh')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
