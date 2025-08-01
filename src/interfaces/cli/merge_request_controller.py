"""
Module principal pour le contrôleur de MergeRequest.
"""

# pylint: disable=too-few-public-methods
from domain.ports.spi.merge_request_provider import IMergeRequestProvider
from domain.ports.spi.presenter import IMergeRequestPresenter
from domain.usecases.list_merge_requests import ListMergeRequests


class MergeRequestController:
    """
    Classe pour le contrôleur de MergeRequest.
    """

    def __init__(
        self, provider: IMergeRequestProvider, presenter: IMergeRequestPresenter
    ):
        self.use_case = ListMergeRequests(provider)
        self.presenter = presenter

    def run(self, username=None):
        """
        Exécute le contrôleur de MergeRequest.
        """
        merge_requests = self.use_case.execute(username=username)
        self.presenter.present_merge_requests(merge_requests)
