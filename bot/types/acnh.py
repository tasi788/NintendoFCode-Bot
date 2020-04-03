from typing import List, Union
from dataclasses import dataclass, field, asdict
from dacite import from_dict

"""acnh = {
    'fruit': 'apple',
    'name': '國民黨不',
    'invite': {
        'password': 'asd123',
        'expire': '2020-02-02T02:20:02'
    },
    'veg': [{
            'date': '2020-02-02T02:20:02',
            'price': 12
            }, {
            'date': '2020-02-02T09:20:02',
            'price': 24
            },
            {
            'date': '2020-02-02T02:20:02',
            'price': 12
            }, {
            'date': '2020-02-02T09:20:02',
            'price': 24
            }
            ]
}"""


@dataclass
class Invite:
    password: str = field(hash=False, repr=True, compare=False, default=None)


@dataclass
class VegData:
    date: str = field(hash=False, repr=True, compare=False, default=None)
    price: int = field(hash=False, repr=True, compare=False, default=None)


@dataclass
class ACNH:
    fruit: str = field(hash=False, repr=True, compare=False, default=None)
    name: str = field(hash=False, repr=True, compare=False, default=None)
    invite: Invite = field(hash=False, repr=True, compare=False, default=None)
    veg: List[VegData] = field(
        hash=False, repr=True, compare=False, default=None)


# result = from_dict(data_class=ACNH, data=acnh)
# print(result.veg[1])
