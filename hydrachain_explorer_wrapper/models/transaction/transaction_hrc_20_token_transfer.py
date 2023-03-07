from dataclasses import dataclass


@dataclass
class TransactionHRC20TokenTransfer:
    address: str = None
    address_hex: str = None
    name: str = None
    symbol: str = None
    decimals: int = None
    from_: str = None
    to: str = None
    value: str = None
