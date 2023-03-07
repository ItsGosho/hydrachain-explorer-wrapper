from dataclasses import dataclass


@dataclass
class Token:
    address: str = None
    address_hex: str = None
    name: str = None
    symbol: str = None
    decimals: int = None
    total_supply: int = None
    version: int = None
    holders: int = None
    transactions: int = None
