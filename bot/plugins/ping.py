from pyrogram import Client, Filters, Message


@Client.on_message(Filters.command('ping') & ~(Filters.forwarded) & ~(Filters.edited))
def ping(client: Client, message: Message):
    message.reply_text('pong')
