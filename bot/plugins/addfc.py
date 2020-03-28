import copy
import re

from pyrogram import Client, Filters, Message

from bot.functions import db_tools


@Client.on_message(Filters.command(['addfc', 'add']) & ~(Filters.forwarded) & ~(Filters.edited))
def addfc(client: Client, message: Message):
    # Failure
    if len(message.command) != 2:
        text = '請在 `/addfc` 後輸入自己的 `SW` 編號窩\n' \
            '例如：`/addfc SW-1234-2234-3234`'
        message.reply_text(text, parse_mode='markdown')
        return

    text = '請輸入正確的好友代碼'
    if message.command[1].lower()[:2] != 'sw':
        text += '，請輸入完整好友代碼（SW 開頭）'
        message.reply_text(text)
        return

    if len(message.command[1]) != 17:
        text += '，請輸入完整好友代碼，似乎有少打字？'
        message.reply_text(text)
        return

    pattern = 'SW-\d{4}-\d{4}-\d{4}'
    re_result = re.findall(pattern, message.command[1].upper())
    if not re_result:
        text += '無法正常解析好友代碼，似乎輸入錯了？\n' \
                '範例：`SW-1234-2234-3234`'
        message.reply_text(text, parse_mode='markdown')
        return

    # Success
    mongo = db_tools.use_mongo()
    query = {
        'chat': {
            'id': message.from_user.id
        }
    }
    # make update
    query_ = copy.copy(query)
    query_.update({'fcode': message.command[1].upper()})
    update = {'$set': query_}
    try:
        mongo.nintendo.update_one(query, update, upsert=True)
    except Exception:
        text = '不明原因的失敗惹！'
        message.reply_text(text)
    else:
        text = '更新好嚕！\n' \
               '你的好友代碼：`{fcode}`'.format(fcode=message.command[1].upper())
        message.reply_text(text, parse_mode='markdown')
