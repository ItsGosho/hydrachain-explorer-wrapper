from datetime import datetime
from typing import List

from hydrachain_explorer_requester.explorer_requester import ExplorerRequester

from hydrachain_explorer_wrapper.models.contract.contract import Contract
from hydrachain_explorer_wrapper.models.contract.contract_transaction import ContractTransaction
from hydrachain_explorer_wrapper.models.other.info import Info
from hydrachain_explorer_wrapper.models.stats.address_growth import AddressGrowth
from hydrachain_explorer_wrapper.models.stats.block_interval import BlockInterval
from hydrachain_explorer_wrapper.models.token import Token
from hydrachain_explorer_wrapper.models.transaction.recent_transaction import RecentTransaction
from hydrachain_explorer_wrapper.models.transaction.transaction import Transaction
from hydrachain_explorer_wrapper.response_class_mapper import ResponseClassMapper
from hydrachain_explorer_wrapper.models.misc.biggest_miner import BiggestMiner
from hydrachain_explorer_wrapper.models.stats.daily_transaction import DailyTransaction
from hydrachain_explorer_wrapper.models.misc.rich_list import RichList
from hydrachain_explorer_wrapper.models.other.search import Search


class ExplorerWrapper:

    def __init__(self,
                 explorer_requester: ExplorerRequester = None,
                 response_class_mapper: ResponseClassMapper = None
                 ):
        self.explorer_requester = explorer_requester or ExplorerRequester()
        self.response_class_mapper = response_class_mapper or ResponseClassMapper()

    TODO = int

    def search(self, value: str) -> Search:
        search_response = self.explorer_requester.search(
            value=value
        )

        return self.response_class_mapper.map_search_response(search_response)

    def get_biggest_miners(self, page_number: int = 0, page_size: int = 20) -> List[BiggestMiner]:
        biggest_miners_response = self.explorer_requester.get_biggest_miners(
            page_number=page_number,
            page_size=page_size
        )

        biggest_miners = biggest_miners_response["list"]
        return self.response_class_mapper.map_responses(
            biggest_miners,
            self.response_class_mapper.map_biggest_miner_response
        )

    def get_biggest_miners_iterator(self, request_portion: int = 20):
        biggest_miners_iterator = self.explorer_requester.get_biggest_miners_iterator(
            request_portion=request_portion
        )

        for biggest_miner_response in biggest_miners_iterator:
            yield self.response_class_mapper.map_biggest_miner_response(biggest_miner_response)

    def get_rich_list(self, page_number: int = 0, page_size: int = 20) -> List[RichList]:
        rich_lists_response = self.explorer_requester.get_rich_list(
            page_number=page_number,
            page_size=page_size
        )

        rich_lists = rich_lists_response["list"]
        return self.response_class_mapper.map_responses(
            rich_lists,
            self.response_class_mapper.map_rich_list_response
        )

    def get_rich_list_iterator(self, request_portion: int = 20):
        rich_lists_iterator = self.explorer_requester.get_rich_list_iterator(
            request_portion=request_portion
        )

        for rich_list_response in rich_lists_iterator:
            yield self.response_class_mapper.map_rich_list_response(rich_list_response)

    def get_daily_transactions(self) -> List[DailyTransaction]:
        daily_transactions_response = self.explorer_requester.get_daily_transactions()

        return self.response_class_mapper.map_responses(daily_transactions_response,
                                                        self.response_class_mapper.map_daily_transaction_response
                                                        )

    def get_block_interval(self) -> List[BlockInterval]:
        block_interval_response = self.explorer_requester.get_block_interval()
        pass

    def get_address_growth(self) -> List[AddressGrowth]:
        address_growth_response = self.explorer_requester.get_address_growth()
        pass

    def get_recent_blocks(self) -> List[TODO]:
        recent_blocks_response = self.explorer_requester.get_recent_blocks()
        pass

    def get_recent_txs(self) -> List[RecentTransaction]:
        recent_txs_response = self.explorer_requester.get_recent_txs()
        pass

    def get_info(self) -> Info:
        info_response = self.explorer_requester.get_info()
        pass

    def get_block(self, number: int) -> TODO:
        block_response = self.explorer_requester.get_block(
            number=number
        )
        pass

    def get_blocks(self, date: datetime) -> List[TODO]:
        blocks_response = self.explorer_requester.get_blocks(
            date=date
        )
        pass

    def get_tokens(self, page_number: int = 0, page_size: int = 20) -> List[QRC20Token]:
        tokens_response = self.explorer_requester.get_tokens(
            page_number=page_number,
            page_size=page_size
        )
        pass

    def get_tokens_iterator(self, request_portion: int = 20):
        tokens_iterator = self.explorer_requester.get_tokens_iterator(
            request_portion=request_portion
        )

        for token_response in tokens_iterator:
            yield  # TODO MAP

    def get_contract(self, contract: str) -> Contract:
        contract_response = self.explorer_requester.get_contract(
            contract=contract
        )
        pass

    def get_contract_transactions(self, contract: str, page_number: int = 0, page_size: int = 20) -> List[ContractTransaction]:
        contract_transactions_response = self.explorer_requester.get_contract_transactions(
            contract=contract,
            page_number=page_number,
            page_size=page_size
        )
        pass

    def get_contract_transactions_iterator(self, contract: str, request_portion: int = 20):
        contract_transactions_iterator = self.explorer_requester.get_contract_transactions_iterator(
            contract=contract,
            request_portion=request_portion
        )

        for contract_transaction_response in contract_transactions_iterator:
            yield  # TODO MAP

    def get_address(self, address: str) -> TODO:
        address_response = self.explorer_requester.get_address(
            address=address
        )
        pass

    def get_address_transactions(self, address: str, page_number: int = 0, page_size: int = 20) -> List[TODO]:
        address_transactions_response = self.explorer_requester.get_address_transactions(
            address=address,
            page_number=page_number,
            page_size=page_size
        )
        pass

    def get_address_transactions_iterator(self, address: str, request_portion: int = 20):
        address_transactions_iterator = self.explorer_requester.get_address_transactions_iterator(
            address=address,
            request_portion=request_portion
        )

        for address_transaction_response in address_transactions_iterator:
            yield  # TODO MAP

    def get_transaction(self, transaction: str) -> Transaction:
        transaction_response = self.explorer_requester.get_transaction(
            transaction=transaction
        )
        pass

    def get_transactions(self, transactions: List[str]) -> List[Transaction]:
        transactions_response = self.explorer_requester.get_transactions(
            transactions=transactions
        )
        pass
