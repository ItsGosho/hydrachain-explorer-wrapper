from dataclasses import dataclass
from datetime import datetime
from typing import List

from hydrachain_explorer_wrapper.models.transaction.transaction_contract_spend import TransactionContractSpend
from hydrachain_explorer_wrapper.models.transaction.transaction_hrc_20_token_transfer import TransactionHRC20TokenTransfer
from hydrachain_explorer_wrapper.models.transaction.transaction_input import TransactionInput
from hydrachain_explorer_wrapper.models.transaction.transaction_output import TransactionOutput


@dataclass
class RecentTransaction:
    id: str = None
    inputs: List[TransactionInput] = None
    outputs: List[TransactionOutput] = None
    is_coinbase: bool = False
    is_coinstake: bool = False
    block_height: int = None
    confirmations: int = None
    timestamp: datetime = None
    input_value: str = None
    output_value: str = None
    refund_value: str = None
    fees: int = None
    size: int = None
    weight: int = None
    contract_spends: List[TransactionContractSpend] = None
    qrc_20_token_transfers: List[TransactionHRC20TokenTransfer] = None

    def __post_init__(self):
        if self.inputs is None:
            self.inputs = []
        if self.outputs is None:
            self.outputs = []
        if self.contract_spends is None:
            self.contract_spends = []
        if self.qrc_20_token_transfers is None:
            self.qrc_20_token_transfers = []
