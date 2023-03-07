from dataclasses import dataclass
from typing import List


@dataclass
class TransactionReceiptLog:
    address: str = None
    address_hex: str = None
    topics: List[str] = None
    data: str = None

    def __post_init__(self):
        if self.topics is None:
            self.topics = []
