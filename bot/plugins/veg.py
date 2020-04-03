from dataclasses import asdict
from datetime import datetime

from dacite import from_dict
from dateutil import tz
from pyrogram import Client, Filters, Message

from ..functions import check_fcode, db_tools
from ..types import user as users
from ..types import acnh

timezone = tz.gettz('Asia/Taipei')


@Client.on_message(Filters.command('acnh') & ~(Filters.edited) & ~(Filters.forwarded))
def veg(client: Client, message: Message):
    """ /acnh veg 123 """
    if len(message.command) < 2:
        return
    if len(message.command) < 3:
        message.reply_text('請輸入價格，或使用 `inline` 自動輸入。')
        return

    if not check_fcode(message.from_user):
        text = '請先使用 `/addfc` 來新增自己的好友代碼吧！\n'
        message.reply_text(text, parse_mode='markdown')
        return

    # 卡崩價錢
    price = int(message.command[-1])

    mongo = db_tools.use_mongo()
    mongo_query = {'chat.id': message.from_user.id}
    mongo_result = mongo.nintendo.find_one(mongo_query)
    user = from_dict(data_class=users, data=mongo_result)

    # 整理時間
    now = datetime.now(tz=timezone)
    hour = 8
    if now.hour > 12:
        # 下午惹
        hour = 12
    now = now.replace(hour=hour, minute=0, second=0)
    if not hasattr(user, 'acnh'):
        message.reply_text('請先使用 /bindgame 來綁定動物森友會吧！')
        return
    if user.acnh.veg:
        for vegs in len(user.acnh.veg):
            if user.acnh.veg[vegs].date == now:
                user.acnh.veg.pop(vegs)
        if len(user.acnh.veg) >= 14:
            user.acnh.veg.pop(-1)

    new_veg_data = asdict(acnh.VegData(date=now, price=price))
