from time import sleep
from pyrogram import Client, Message, Filters
from pyrogram.errors import FloodWait


@Client.on_message(Filters.command('addfc'))
def addfc(client: Client, message: Message):
    message.reply_text('pong')
