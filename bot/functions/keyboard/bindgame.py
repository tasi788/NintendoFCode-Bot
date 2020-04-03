from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup


def bindgame():
    keyboard = [
        [
            InlineKeyboardButton(
                '🎮 選擇遊戲', switch_inline_query_current_chat='bindgame')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
