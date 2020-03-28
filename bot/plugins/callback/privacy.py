import copy
from time import sleep
from pyrogram import Client, Filters, CallbackQuery
from pyrogram.errors import FloodWait

from bot.functions import db_tools, keyboard


def check_func(_, query: CallbackQuery):
    splitter = query.data.split()
    if not len(splitter) == 3:
        return False
    if ['set', 'privacy'] == splitter[0:2]:
        return True


@Client.on_callback_query(Filters.create(check_func))
def privacy(client: Client, message: CallbackQuery):
    action = message.data.split()[-1]
    if action == 'on':
        privacy = True
    else:
        privacy = False

    mongo = db_tools.use_mongo()
    query = {'chat.id': message.from_user.id}
    query_result = mongo.nintendo.find_one(query)

    if not isinstance(query_result, dict):
        text = '發生不明錯誤，無法查詢到該筆資料.'
        message.answer(text, show_alert=True)
        return

    if 'privacy' not in query_result.keys():
        current = False
    else:
        current = query_result['privacy']

    if current == privacy:
        message.answer("你已經設定好了啦 ヾ(⌒(ﾉｼ'ω')ﾉｼ", show_alert=True)
        return

    # update settings.
    # 忍術拖延戰術！
    message.answer('已更新設定', show_alert=True)
    query_ = copy.copy(query)
    query_.update({'privacy': privacy})
    update = {'$set': query_}
    mongo.nintendo.update_one(query, update)

    text = '目前你的隱私狀態為 `{status}`\n' \
           '意思是任何人都 `{visble}` 利用 `/findfc` 指令找到你喔！'.format(
               status='開啟' if privacy else '關閉',
               visble='不可以' if privacy else '可以'
           )
    while True:
        try:
            message.edit_message_text(text, parse_mode='markdown',
                                      reply_markup=keyboard.privacy())
        except FloodWait as wait:
            sleep(wait.x)
        else:
            break
