from html import escape
from pyrogram import InlineQueryResultArticle, InputTextMessageContent

from ...functions import configure, db_tools, keyboard
from ...game import gamelist
from ...types import user as users


def myacnh(user: users):
    pics = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/237/rightwards-arrow-with-hook_21aa.png'
    result = list()

    # 文字拼拼
    text = '#動物森友 #AnimalCrossing\n' \
        '島名：<code>{island}</code>\n' \
        '特產：#{fruit}\n'.format(
            island=escape(user.acnh.name),
            fruit=user.acnh.fruit
        )
    if user.acnh.veg:
        text += '大頭菜價格：<code>{price}</code> 鈴錢\n'.format(
            price=user.acnh.veg[-1].price)
    if user.privacy:
        text += '好友代碼：<code>{fcode}</code>'.format(fcode=user.fcode)
    else:
        text += '因為[隱私設定]({url})因此不顯示好友代碼。'.format(
            url='t.me/NintendoFCode_bot?start=privacy')
    text = InputTextMessageContent(text)

    result.append(
        InlineQueryResultArticle(
            input_message_content=text, title='分享我的動物森友會資訊', thumb_url='{pics}'.format(pics=pics), reply_markup=keyboard.bindacnh(visble=True))
    )
    return result
