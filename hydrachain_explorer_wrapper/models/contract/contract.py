from dataclasses import dataclass
from typing import List

from hydrachain_explorer_wrapper.models.contract.qrc20 import Qrc20
from hydrachain_explorer_wrapper.models.qrc20.qrc_20_token import QRC20Token


@dataclass
class Contract:
    address: str = None
    address_hex: str = None
    vm: str = None
    type: str = None
    qrc20: Qrc20 = None
    balance: int = None
    total_received: int = None
    total_sent: int = None
    unconfirmed: int = None
    qrc_20_balances: List[QRC20Token] = None
    transaction_count: int = None

    def __post_init__(self):
        if self.qrc_20_balances is None:
            self.qrc_20_balances = []
