"""
Module principal pour le cas d’usage de listing des changements en attente.
"""

# pylint: disable=too-few-public-methods
from domain.ports.api.list_pending_changes_usecase import IListPendingChangesForRelease
from domain.ports.spi.pending_changes_provider import IPendingChangesProvider
from domain.models.release import PendingChanges


class ListPendingChangesForRelease(IListPendingChangesForRelease):
    """
    Classe pour le cas d’usage de listing des changements en attente.
    """

    def __init__(self, provider: IPendingChangesProvider):
        self.provider = provider

    def execute(self, since_version: str, target_version: str):
        """
        Exécute le cas d’usage de listing des changements en attente.
        """
        changes = self.provider.list_merged_changes_since(since_version)
        return PendingChanges(target_version=target_version, changes=changes)
