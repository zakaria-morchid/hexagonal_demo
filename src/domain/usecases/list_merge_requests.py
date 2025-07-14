"""
Module principal pour le cas d’usage de listing des merge requests.
"""

# pylint: disable=too-few-public-methods
from domain.ports.api.list_merge_requests_usecase import IListMergeRequestsUseCase
from domain.ports.spi.merge_request_provider import IMergeRequestProvider
from domain.ports.spi.presenter import IMergeRequestPresenter


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
