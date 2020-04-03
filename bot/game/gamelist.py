import json

from dacite import from_dict

from ..types import game


def gamelist():
    glist = list()
    file = open('./bot/game/gamelist.json', 'r').read()
    loads = json.loads(file)
    for g in loads:
        glist.append(from_dict(data_class=game.Game, data=g))
    return glist
