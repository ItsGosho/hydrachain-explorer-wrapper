from dataclasses import dataclass
from datetime import datetime


@dataclass
class DailyTransaction:

    time: datetime = None
    transaction_count: int = None
    contract_transaction_count: int = None
