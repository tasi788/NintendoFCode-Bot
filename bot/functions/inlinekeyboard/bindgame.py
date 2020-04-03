from pyrogram import InlineQueryResultArticle, InputTextMessageContent

from ...game import gamelist


def bindgame():
    base_url = 'https://raw.githubusercontent.com/tasi788/NintendoFCode-Bot/%E5%A4%A7%E9%A0%AD%E8%8F%9C%E5%8A%9F%E8%83%BD/bot/statics/games/'
    result = list()

    for game in gamelist():
        text = InputTextMessageContent(
            '/bindgame {short}'.format(short=game.short))
        keyboard = InlineQueryResultArticle(
            input_message_content=text, title=game.name, thumb_url='{base_url}{pics}'.format(base_url=base_url, pics=game.pics))
        result.append(keyboard)
    return result
