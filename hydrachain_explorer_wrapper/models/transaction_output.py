from dataclasses import dataclass

from hydrachain_explorer_wrapper.models.transaction_receipt import TransactionReceipt
from hydrachain_explorer_wrapper.models.transaction_script_pub_key import TransactionScriptPubKey


@dataclass
class TransactionOutput:
    value: str = None
    address: str = None
    transaction_script_pub_key: TransactionScriptPubKey = None
    spent_tx_id: str = None
    spent_index: int = None
    address_hex: str = None
    receipt: TransactionReceipt = None
