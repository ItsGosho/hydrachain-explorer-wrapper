from dataclasses import dataclass
from typing import List

from hydrachain_explorer_wrapper.models.transaction.transaction_input import TransactionInput
from hydrachain_explorer_wrapper.models.transaction.transaction_output import TransactionOutput


@dataclass
class TransactionContractSpend:
    inputs: List[TransactionInput] = None
    outputs: List[TransactionOutput] = None

    def __post_init__(self):
        if self.inputs is None:
            self.inputs = []
        if self.outputs is None:
            self.outputs = []
