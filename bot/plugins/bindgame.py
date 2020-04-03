from pyrogram import Client, Filters, Message
from ..functions import keyboard


@Client.on_message(Filters.command('bindgame') & ~(Filters.edited) & ~(Filters.forwarded))
def bindgame(client: Client, message: Message):
    if len(message.command) == 1:
        text = '請按下方來選擇想要綁定的遊戲。'
        message.reply_text(text, reply_markup=keyboard.bindgame())
        return
