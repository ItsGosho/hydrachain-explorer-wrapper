from dataclasses import dataclass
from datetime import datetime


@dataclass
class AddressGrowth:
    time: datetime = None
    addresses: int = None
