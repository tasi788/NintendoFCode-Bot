from pyrogram import InlineQueryResultArticle, InputTextMessageContent

from ...functions import configure
from ...game import gamelist


def bindgame():
    base_url = configure.get('statics', 'base_url')
    result = list()

    for game in gamelist():
        text = InputTextMessageContent(
            '/bindgame {short}'.format(short=game.short))
        keyboard = InlineQueryResultArticle(
            input_message_content=text, title=game.name, thumb_url='{base_url}{pics}'.format(base_url=base_url, pics=game.pics))
        result.append(keyboard)
    return result
