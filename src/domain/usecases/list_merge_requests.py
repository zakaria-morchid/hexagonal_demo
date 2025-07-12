from abc import ABC, abstractmethod
from typing import List
from domain.models.model import MergeRequest
from domain.ports.provider import IMergeRequestProvider
from domain.ports.presenter import IPresenter

class IListMergeRequestsUseCase(ABC):
    @abstractmethod
    def execute(self, username=None):
        """
        Exécute le cas d’usage de listing des merge requests,
        avec un filtrage optionnel par username.
        """
        pass


class ListMergeRequests(IListMergeRequestsUseCase):
    def __init__(self, provider: IMergeRequestProvider, presenter: IPresenter):
        self.provider = provider
        self.presenter = presenter

    def execute(self, username=None):
        merge_requests = self.provider.fetch_merge_requests(username=username)
        self.presenter.present(list(merge_requests))

