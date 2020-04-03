from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup


def bindacnh(share=False):
    if share:
        text = '我也想綁定動森友資料！'
    else:
        text = '🔗 開始綁定'
    keyboard = [
        [
            InlineKeyboardButton(
                text, switch_inline_query_current_chat='bindgame acnh')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
