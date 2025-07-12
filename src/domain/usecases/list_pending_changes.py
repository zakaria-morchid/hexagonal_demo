"""
Module principal pour le cas d’usage de listing des changements en attente.
"""

# pylint: disable=too-few-public-methods
from abc import ABC, abstractmethod
from domain.ports.presenter import IPresenter
from domain.ports.pending_changes_provider import IPendingChangesProvider
from domain.models.release import PendingChanges


class IListPendingChangesForRelease(ABC):
    """
    Interface pour le cas d’usage de listing des changements en attente.
    """

    @abstractmethod
    def execute(self, since_version: str, target_version: str):
        """
        Liste les changements en attente pour une version spécifique.
        """


class ListPendingChangesForRelease(IListPendingChangesForRelease):
    """
    Classe pour le cas d’usage de listing des changements en attente.
    """

    def __init__(self, provider: IPendingChangesProvider, presenter: IPresenter):
        self.provider = provider
        self.presenter = presenter

    def execute(self, since_version: str, target_version: str):
        """
        Exécute le cas d’usage de listing des changements en attente.
        """
        changes = self.provider.list_merged_changes_since(since_version)
        self.presenter.present(changes)
        self.presenter.present(
            PendingChanges(target_version=target_version, changes=changes)
        )
