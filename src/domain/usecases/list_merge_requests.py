"""
Module principal pour le cas d’usage de listing des merge requests.
"""

# pylint: disable=too-few-public-methods
from abc import ABC, abstractmethod
from domain.ports.merge_request_provider import IMergeRequestProvider
from domain.ports.presenter import IMergeRequestPresenter


class IListMergeRequestsUseCase(ABC):
    """
    Interface pour le cas d’usage de listing des merge requests.
    """

    @abstractmethod
    def execute(self, username=None):
        """
        Exécute le cas d’usage de listing des merge requests,
        avec un filtrage optionnel par username.
        """


class ListMergeRequests(IListMergeRequestsUseCase):
    """
    Classe pour le cas d’usage de listing des merge requests.
    """

    def __init__(
        self, provider: IMergeRequestProvider, presenter: IMergeRequestPresenter
    ):
        self.provider = provider
        self.presenter = presenter

    def execute(self, username=None):
        """
        Exécute le cas d’usage de listing des merge requests.
        """
        merge_requests = list(self.provider.fetch_merge_requests(username=username))
        self.presenter.present_merge_requests(merge_requests)
