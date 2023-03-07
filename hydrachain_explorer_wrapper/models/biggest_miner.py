from dataclasses import dataclass


@dataclass
class BiggestMiner:
    address: str = None
    blocks: int = None
    balance: int = None
