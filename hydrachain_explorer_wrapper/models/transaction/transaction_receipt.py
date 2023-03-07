from dataclasses import dataclass
from typing import List

from hydrachain_explorer_wrapper.models.transaction.transaction_receipt_log import TransactionReceiptLog


@dataclass
class TransactionReceipt:
    sender: str = None
    receipt: str = None
    gas_used: int = None
    contract_address: str = None
    contract_address_hex: str = None
    excepted: str = None
    excepted_message: str = None
    logs: List[TransactionReceiptLog] = None

    def __post_init__(self):
        if self.logs is None:
            self.topics = []
