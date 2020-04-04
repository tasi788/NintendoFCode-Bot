import argparse
from html import escape

from dacite import from_dict
from pyrogram import Client, Filters, Message
from pyrogram.errors import BadRequest, Forbidden

from ...functions import db_tools, keyboard
from ...types import user as users


def check_func(_, message: Message):
    # /bindgame acnh
    if Filters.command('bindgame')(message):
        message.command = message.text.split()
        if not len(message.command) > 1:
            return False
        if message.command[1] == 'acnh':
            return True


@Client.on_message(Filters.create(check_func), group=1)
def acnh(client: Client, message: Message):
    message.command = message.text.split()

    try:
        message.delete()
    except (BadRequest, Forbidden):
        pass

    if len(message.command) == 2:
        text = '那我們就快點開始吧狸！'
        message.reply_text(text, reply_markup=keyboard.bindacnh())
        return

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=str)
    parser.add_argument('-f', type=str)
    args = parser.parse_args(message.command[2:])

    # 二次檢查水果，我教官我機掰 耶
    if args.f not in ['梨子', '櫻桃', '蘋果', '桃子', '橘子']:
        text = '水果種類有誤，請檢查下狸！\n' \
            '每個人島上的水果特產種類應該是 「梨子、櫻桃、蘋果、桃子、橘子」 其中一種喔！'
        message.reply_text(text)
        return

    mongo = db_tools.use_mongo()
    mongo_query = {'chat.id': message.from_user.id}
    mongo_update = {'$set': {'acnh.name': args.n, 'acnh.fruit': args.f}}
    mongo.nintendo.update_one(mongo_query, mongo_update, upsert=True)

    # Success !
    mongo_result = mongo.nintendo.find_one(mongo_query)
    if not isinstance(mongo_result, dict):
        text = '發生了一點錯誤，請告知開發者。'
        message.reply_text(text)
        return

    user = from_dict(data_class=users, data=mongo_result)
    text = '#動森友 #AnimalCrossing\n' \
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

    message.reply_text(text, reply_markup=keyboard.bindacnh(
        share=True), disable_web_page_preview=True)
