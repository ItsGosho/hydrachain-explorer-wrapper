from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List


@dataclass
class Block:
    bits: str = None
    chainwork: str = None
    confirmations: int = None
    difficulty: Decimal = None
    flags: str = None
    hash: str = None
    hash_state_root: str = None
    hash_utxo_root: str = None
    height: int = None
    interval: int = None
    merkle_root: str = None
    miner: str = None
    next_hash: str = None
    nonce: int = None
    prev_hash: str = None
    prev_out_stake_hash: str = None
    prev_out_stake_n: int = None
    reward: int = None
    signature: str = None
    size: int = None
    timestamp: datetime = None
    transactions: List[str] = None
    version: int = None
    weight: int = None


    def __post_init__(self):
        if self.transactions is None:
            self.transactions = []