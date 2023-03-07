from hydrachain_explorer_requester.explorer_requester import ExplorerRequester

from hydrachain_explorer_wrapper.response_class_mapper import ResponseClassMapper
from hydrachain_explorer_wrapper.models.biggest_miner import BiggestMiner
from hydrachain_explorer_wrapper.models.daily_transaction import DailyTransaction
from hydrachain_explorer_wrapper.models.rich_list import RichList
from hydrachain_explorer_wrapper.models.search import Search


class ExplorerWrapper:

    def __init__(self,
                 explorer_requester: ExplorerRequester = None,
                 response_class_mapper: ResponseClassMapper = None
                 ):
        self.explorer_requester = explorer_requester or ExplorerRequester()
        self.response_class_mapper = response_class_mapper or ResponseClassMapper()

    def search(self, value: str) -> Search:
        search_response = self.explorer_requester.search(
            value=value
        )

        return self.response_class_mapper.map_search_response(search_response)

    def get_biggest_miners(self, page_number: int = 0, page_size: int = 20) -> list[BiggestMiner]:
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

    def get_rich_list(self, page_number: int = 0, page_size: int = 20) -> list[RichList]:
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

    def get_daily_transactions(self) -> list[DailyTransaction]:
        daily_transactions_response = self.explorer_requester.get_daily_transactions()

        return self.response_class_mapper.map_responses(daily_transactions_response,
                                                        self.response_class_mapper.map_daily_transaction_response
                                                        )
