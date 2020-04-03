from pyrogram import Client, Filters, Message

from bot.functions import db_tools, keyboard


@Client.on_message(Filters.command('myfc') & ~(Filters.forwarded) & ~(Filters.edited))
def myfc(client: Client, message: Message):
    mongo = db_tools.use_mongo()
    query = {'chat.id': message.from_user.id}
    query_result = mongo.nintendo.find_one(query)
    if not isinstance(query_result, dict):
        text = '你沒有設定過好友代碼唷，請先使用 `/addfc` 來新增自己的好友代碼吧！\n'
        message.reply_text(text, parse_mode='markdown')
        return

    # found record
    text = '我的好友代碼是：`{fcode}`'.format(
        fcode=query_result['fcode']
    )

    message.reply_text(text, parse_mode='markdown',
                       reply_markup=keyboard.myfc())
