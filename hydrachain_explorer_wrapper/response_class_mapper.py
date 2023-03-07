from datetime import datetime
from typing import Callable
from decimal import Decimal

from hydrachain_explorer_wrapper.models.biggest_miner import BiggestMiner
from hydrachain_explorer_wrapper.models.block_interval import BlockInterval
from hydrachain_explorer_wrapper.models.daily_transaction import DailyTransaction
from hydrachain_explorer_wrapper.models.rich_list import RichList
from hydrachain_explorer_wrapper.models.search import Search, Type

class ResponseClassMapper:

    def __init__(self):
        pass


    def map_search_response(self, response: dict) -> Search:
        return Search(
            type=next((x for x in Type if x.value[0] == response['type']), None),
            address=response.get('address', None),
            address_hex=response.get('addressHex', None)
        )

    def map_biggest_miner_response(self, response: dict) -> BiggestMiner:
        return BiggestMiner(
            address=response.get('address', None),
            blocks=int(response.get('blocks', '0')),
            balance=int(response.get('balance', '0'))
        )

    def map_rich_list_response(self, response: dict) -> RichList:
        return RichList(
            address=response.get('address', None),
            balance=int(response.get('balance', 0))
        )

    def map_daily_transaction_response(self, response: dict) -> DailyTransaction:

        return DailyTransaction(
            time=datetime.strptime(response['time'], '%Y-%m-%dT%H:%M:%S.%fZ'),
            transaction_count=int(response.get('transactionCount', 0)),
            contract_transaction_count=int(response.get('contractTransactionCount', 0))
        )

    def map_block_interval_response(self, response: dict) -> BlockInterval:
        return BlockInterval(
            interval=int(response.get('interval', 0)),
            count=int(response.get('count', 0)),
            percentage=Decimal(response.get('percentage', 0))
        )

    def map_responses(self, responses: dict, mapper_function: Callable):
        return [mapper_function(response) for response in responses]