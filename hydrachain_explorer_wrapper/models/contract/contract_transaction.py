from dataclasses import dataclass
from datetime import datetime
from typing import List

from hydrachain_explorer_wrapper.models.contract.evm_log import EvmLog


@dataclass
class ContractTransaction:
    transaction_id: str = None
    output_index: int = None
    block_height: int = None
    block_hash: str = None
    timestamp: datetime = None
    confirmations: int = None
    type: str = None
    gas_limit: int = None
    gas_price: int = None
    byte_code: str = None
    output_value: str = None
    sender: str = None
    gas_used: int = None
    contract_address: str = None
    contract_address_hex: str = None
    excepted: str = None
    excepted_message: str = None
    evm_logs: List[EvmLog] = None

    def __post_init__(self):
        if self.evm_logs is None:
            self.evm_logs = []