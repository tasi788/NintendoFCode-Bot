from pyrogram import Client, Message, Filters
from pyrogram.errors import FloodWait
from bot.functions import db_tools


def check_func(_, message: Message):
    if Filters.forwarded(message):
        return False
    if Filters.command('start')(message):
        if len(message.command) <= 1:
            return False
        if message.command[1].lower() == 'addfc':
            return True


@Client.on_message(Filters.create(check_func))
def start_addfc(client: Client, message: Message):
    mongo = db_tools.use_mongo()
    query = {'chat.id': message.from_user.id}
    query_result = mongo.nintendo.find_one(query)
    if isinstance(query_result, dict):
        # found record
        text = '我的好友代碼是：`{fcode}`\n' \
               '如果需要更新好友代碼請使用 `/addfc`'.format(
                   fcode=query_result['fcode']
               )

        message.reply_text(text, parse_mode='markdown')
