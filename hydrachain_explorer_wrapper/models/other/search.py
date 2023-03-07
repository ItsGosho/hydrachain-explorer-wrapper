import enum
from dataclasses import dataclass


class Type(enum.Enum):
    BLOCK = 'block',
    TRANSACTION = 'transaction',
    ADDRESS = 'address',
    CONTRACT = 'contract',


@dataclass
class Search:
    type: Type = None
    address: str = None
    address_hex: str = None

    def has_found(self) -> bool:
        return self.type is not None
