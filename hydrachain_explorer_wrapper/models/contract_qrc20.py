from dataclasses import dataclass


@dataclass
class ContractQrc20:
    name: str = None
    symbol: str = None
    decimals : int = None
    total_supply: int = None
    version: int = None
    holders: int = None
    transactions: int = None