from collections import namedtuple
from time import sleep

from pyrogram import Client, Filters, Message
from pyrogram.errors import BadRequest, FloodWait

from bot.functions import db_tools


class Find:
    USERNOTFOUND = '找不到 {username}'
    NOTEXIST = '找不到好友代碼或對方未開放搜尋喔~'
    NOTVISBLE = NOTEXIST
    FOUND = '{username} 的好友代碼是 `{fcode}`'


@Client.on_message(Filters.command(['findfc']) & ~(Filters.forwarded) & ~(Filters.edited))
def findfc(client: Client, message: Message):
    find_result = Find()
    mongo = db_tools.use_mongo()

    # fetch id from username
    if not Filters.reply(message):
        username = message.command[1]

        # check failure.
        if username[0] != '@':
            text = '你輸入的 {input_} 應該不是正確的 username 格式，應該是 `@` 開頭'.format(
                input_=username)
            message.reply_text(text, parse_mode='markdown')
            return

        # ready to go.
        user_id = None
        while True:
            try:
                user_id = client.get_users(username).id
            except BadRequest:
                text = find_result.USERNOTFOUND.format(username=username)
                break
            except FloodWait as wait:
                sleep(wait.x)
            else:
                break
    else:
        # fetch id from reply message
        # prevent ?_?
        if message.reply_to_message.from_user.is_self:
            text = '你找一個別人回覆啊，我是機器人啊，難不成我要用腦波跟你玩？'
            message.reply_text(text)
            return
        user_id = message.reply_to_message.from_user.id
        username = '@{username}'.format(
            username=message.reply_to_message.from_user.username) if message.reply_to_message.from_user.username else ''
    if user_id:
        # make query to get ready.
        query = {'chat.id': user_id}
        query_result = mongo.nintendo.find_one(query)
        if not isinstance(query_result, dict):
            text = find_result.NOTEXIST
        else:
            # remove failed keys()
            query_result.pop('_id')

            # make it to an obkect.
            user = namedtuple("User", query_result.keys())(
                *query_result.values())

            # privacy is basic human right hex project.
            if 'privacy' in query_result.keys():
                if user.privacy:
                    text = find_result.NOTVISBLE
                else:
                    text = find_result.FOUND.format(
                        username=username, fcode=user.fcode)
            else:
                text = find_result.FOUND.format(
                    username=username, fcode=user.fcode)
    message.reply_text(text, parse_mode='markdown')
