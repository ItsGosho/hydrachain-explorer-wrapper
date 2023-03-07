from dataclasses import dataclass
from decimal import Decimal


@dataclass
class BlockInterval:
    interval: int = None
    count: int = None
    percentage: Decimal = None
