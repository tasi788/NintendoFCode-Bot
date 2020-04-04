import json

from dacite import from_dict

from ..types import game


def gamelist(game: str):
    file = open('./bot/game/gamelist.json', 'r').read()
    loads = json.loads(file)
    if game:
        for g in loads:
            if game == g['short']:
                glist = from_dict(data_class=game.Game, data=g)
            else:
                glist = None
    else:
        glist = list()
        for g in loads:
            glist.append(from_dict(data_class=game.Game, data=g))
    return glist
