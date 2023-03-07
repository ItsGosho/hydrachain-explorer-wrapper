from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Info:
    height: int = None
    supply: Decimal = None
    net_stake_weight: int = None
    fee_rate: float = None
    gas_price: float = None
    circulating_supply: Decimal = None
    apr: float = None