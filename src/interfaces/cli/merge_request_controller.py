"""
Module principal pour le contrôleur de MergeRequest.
"""

# pylint: disable=too-few-public-methods
from domain.ports.provider import IMergeRequestProvider
from domain.ports.presenter import IPresenter
from domain.usecases.list_merge_requests import ListMergeRequests


class MergeRequestController:
    """
    Classe pour le contrôleur de MergeRequest.
    """

    def __init__(self, provider: IMergeRequestProvider, presenter: IPresenter):
        self.use_case = ListMergeRequests(provider, presenter)

    def run(self, username=None):
        """
        Exécute le contrôleur de MergeRequest.
        """
        self.use_case.execute(username=username)
