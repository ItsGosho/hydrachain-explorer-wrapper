from dataclasses import dataclass


@dataclass
class ContractQRC20Token:
    address: str = None
    address_hex: str = None
    name: str = None
    symbol: str = None
    decimals: int = None
    balance: int = None