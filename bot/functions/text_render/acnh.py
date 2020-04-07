from dacite import from_dict

from ...functions import db_tools
from ...types import user as users


def acnh(user: users):
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
    return text
