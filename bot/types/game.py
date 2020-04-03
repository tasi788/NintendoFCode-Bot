from dataclasses import field, dataclass


@dataclass
class Game:
    name: str = field(hash=False, repr=True, compare=False, default=None)
    pics: str = field(hash=False, repr=True, compare=False, default=None)
    short: str = field(hash=False, repr=True, compare=False, default=None)
