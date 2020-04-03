from dataclasses import dataclass, field

from .acnh import ACNH


@dataclass
class Chat:
    id: int = field(hash=False, repr=True, compare=False, default=None)


@dataclass
class User:
    chat: Chat = field(hash=False, repr=True, compare=False, default=None)
    fcode: str = field(hash=False, repr=True, compare=False, default=None)
    privacy: bool = field(hash=False, repr=True, compare=False, default=False)
    acnh: ACNH = field(hash=False, repr=True, compare=False, default=None)
