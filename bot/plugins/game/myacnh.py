from html import escape

from pyrogram import Client, Filters, Message

from dacite import from_dict

from ...functions import db_tools
from ...types import user as users


@Client.on_message(Filters.command('myacnh') & ~(Filters.edited) & ~(Filters.forwarded))
def myacnh(client: Client, message: Message):
    mongo = db_tools.use_mongo()
    mongo_query = {'chat.id': message.from_user.id}
    mongo_result = mongo.nintendo.find_one(mongo_query)

    if not isinstance(mongo_result, dict):
        message.reply_text('請先使用 `/addfc` 新增自己的好友代碼吧')
        return

    user = from_dict(data_class=users, data=mongo_result)
    if not user.acnh:
        message.reply_text('請先使用 `/bindgame` 來綁定遊戲')
        return

    text = '#動物森友 #AnimalCrossing\n' \
        '島名：<code>{island}</code>\n' \
        '特產：#{fruit}\n'.format(
            island=escape(user.acnh.name),
            fruit=user.acnh.fruit
        )
    if not user.privacy:
        text += '好友代碼：<code>{fcode}</code>'.format(fcode=user.fcode)
    else:
        text += '因為[隱私設定]({url})因此不顯示好友代碼。'.format(
            url='t.me/NintendoFCode_bot?start=privacy')

    message.reply_text(text)
