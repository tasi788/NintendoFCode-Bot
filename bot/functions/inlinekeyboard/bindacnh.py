from pyrogram import InlineQueryResultArticle, InputTextMessageContent, CallbackQuery


def get_hint(length):
    if length == 2:
        short = '請空格後輸入你的島名'
        long = '格式錯誤，' + short + '，例如\n`@NintendoFCode_bot bindgame acnh 卡加布列`'
    if length == 3:
        short = '請先空格後輸入島上特產水果'
        long = '格式錯誤，' + short + '，例如\n`@NintendoFCode_bot bindgame acnh 卡加布列 蘋果`'
    return long, short


def bindacnh(callback_query: CallbackQuery):
    data = callback_query.query.split()
    hint = len(data)
    result = list()

    if hint <= 3:
        long, short = get_hint(hint)
    else:
        island = data[2]
        fruit = data[3]
        long = '/bindgame acnh -n {name} -f {fruit}'.format(
            name=island, fruit=fruit)
        short = '輸入好的話就點我吧狸！'

    text = InputTextMessageContent(long)
    keyboard = InlineQueryResultArticle(
        input_message_content=text, title=short)
    result.append(keyboard)
    return result
