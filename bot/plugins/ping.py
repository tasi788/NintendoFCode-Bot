from pyrogram import Client, Message, Filters


@Client.on_message(Filters.command('ping'))
def ping(client: Client, message: Message):
    message.reply_text('pong')
