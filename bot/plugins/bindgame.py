from pyrogram import Client, Filters, Message

from ..functions import keyboard
from ..game import gamelist


def check_func(_, message: Message):
    if Filters.edited(message):
        return False
    if Filters.forwarded(message):
        return False
    if Filters.command('bindgame')(message):
        return True


@Client.on_message(Filters.command('bindgame') & ~(Filters.edited) & ~(Filters.forwarded))
def bindgame(client: Client, message: Message):
    message.command = message.text.split()
    if len(message.command) == 1:
        text = '請按下方來選擇想要綁定的遊戲。'
        message.reply_text(text, reply_markup=keyboard.bindgame())
        return
