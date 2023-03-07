from dataclasses import dataclass
from typing import List

from hydrachain_explorer_wrapper.models.transaction.transaction_script_sig import TransactionScriptSig


@dataclass
class TransactionInput:
    prev_tx_id: str = None
    output_index: int = None
    value: str = None
    address: str = None
    script_sig: List[TransactionScriptSig] = None
    sequence: int = None
    witness: List[str] = None

    def __post_init__(self):
        if self.script_sig is None:
            self.script_sig = []
        if self.witness is None:
            self.witness = []
