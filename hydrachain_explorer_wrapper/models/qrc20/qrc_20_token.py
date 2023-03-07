from dataclasses import dataclass


@dataclass
class QRC20Token:
    address: str = None
    address_hex: str = None
    name: str = None
    symbol: str = None
    decimals: int = None
    total_supply: int = None
    version: str = None
    holders: int = None
    transactions: int = None