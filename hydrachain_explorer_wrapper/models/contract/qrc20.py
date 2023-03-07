from dataclasses import dataclass


@dataclass
class Qrc20:
    name: str = None
    symbol: str = None
    decimals : int = None
    total_supply: int = None
    version: str = None
    holders: int = None
    transactions: int = None