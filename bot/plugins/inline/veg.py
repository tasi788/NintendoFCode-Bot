from pyrogram import Client, Filters, InlineQuery

from bot.functions import inlinekeyboard


def check_func(_, inline_query: InlineQuery):
    # @NintendoFCode_bot acnh veg 547
    data = inline_query.query.split()
    if len(data) != 3:
        return False
    if data[0:2] == ['acnh', 'veg']:
        return True


@Client.on_inline_query(Filters.create(check_func))
def veg(client: Client, inline_query: InlineQuery):
    data = inline_query.query.split()
    price = data[-1]
    if price.isdigit():
        price = int(price)
    else:
        price = 0

    keyboard = inlinekeyboard.veg(inline_query.from_user.id, int(price))
    inline_query.answer(keyboard, cache_time=0)
