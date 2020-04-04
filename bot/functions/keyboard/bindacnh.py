from pyrogram import InlineKeyboardButton, InlineKeyboardMarkup


def bindacnh(share=False, visble=False):
    keyboard = list()
    if share:
        text = '分享到群組'
        keyboard.append(
            [InlineKeyboardButton(
                text, switch_inline_query='myacnh')]
        )
    if visble:
        text = '我也要綁定動物森友會資料！'
        keyboard.append(
            [InlineKeyboardButton(
                text, url='t.me/NintendoFCode_bot?start=help')]
        )
    if not share and not visble:
        text = '🔗 開始綁定'
        keyboard.append(
            [InlineKeyboardButton(
                text, switch_inline_query_current_chat='bindgame acnh')]
        )

    return InlineKeyboardMarkup(keyboard)
