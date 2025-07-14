"""
Module principal pour le cas d’usage de listing des merge requests.
"""

# pylint: disable=too-few-public-methods
from domain.ports.api.list_merge_requests_usecase import IListMergeRequestsUseCase
from domain.ports.spi.merge_request_provider import IMergeRequestProvider


class ListMergeRequests(IListMergeRequestsUseCase):
    """
    Classe pour le cas d’usage de listing des merge requests.
    """

    def __init__(self, provider: IMergeRequestProvider):
        self.provider = provider

    def execute(self, username=None):
        """
        Exécute le cas d’usage de listing des merge requests.
        """
        merge_requests = list(self.provider.fetch_merge_requests(username=username))
        return merge_requests
