from dataclasses import dataclass


@dataclass
class TransactionScriptSig:
    type: str = None
    hex: str = None
    asm: str = None
