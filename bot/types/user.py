from dataclasses import dataclass, field, asdict

from .acnh import ACNH


@dataclass
class Chat:
    id: int = field(hash=False, repr=True, compare=False, default=None)


@dataclass
class User:
    chat: Chat = field(hash=False, repr=True, compare=False, default=None)


@dataclass
class Acnh:
    acnh: ACNH = field(hash=False, repr=True, compare=False, default=None)
