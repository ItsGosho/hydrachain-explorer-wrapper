from dataclasses import dataclass
from typing import List

from hydrachain_explorer_wrapper.models.contract_qrc20 import ContractQrc20
from hydrachain_explorer_wrapper.models.contract_qrc20token import ContractQRC20Token


@dataclass
class Contract:
    address: str = None
    address_hex: str = None
    vm: str = None
    type: str = None
    qrc20: ContractQrc20 = None
    balance: int = None
    total_received: int = None
    total_sent: int = None
    unconfirmed: int = None
    qrc_20_balances: List[ContractQRC20Token] = None
    transaction_count: int = None
