import json

from dacite import from_dict

from ..types import game


def gamelist(game_name: str = None):
    file = open('./bot/game/gamelist.json', 'r').read()
    loads = json.loads(file)
    if game_name:
        for g in loads:
            if game_name == g['short']:
                glist = from_dict(data_class=game.Game, data=g)
            else:
                glist = None
    else:
        glist = list()
        for g in loads:
            glist.append(from_dict(data_class=game.Game, data=g))
    return glist
