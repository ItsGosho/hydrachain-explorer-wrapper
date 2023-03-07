from dataclasses import dataclass


@dataclass
class TransactionScriptPubKey:
    type: str = None
    hex: str = None
    asm: str = None
