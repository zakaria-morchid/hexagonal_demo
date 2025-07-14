"""
Module principal pour le contrôleur de PendingChanges.
"""

# pylint: disable=too-few-public-methods
from domain.ports.spi.pending_changes_provider import IPendingChangesProvider
from domain.ports.spi.presenter import IPendingChangesPresenter
from domain.usecases.list_pending_changes import ListPendingChangesForRelease


class PendingChangesController:
    """
    Classe pour le contrôleur de PendingChanges.
    """

    def __init__(
        self, provider: IPendingChangesProvider, presenter: IPendingChangesPresenter
    ):
        self.use_case = ListPendingChangesForRelease(provider)
        self.presenter = presenter

    def run(self, since_version: str, target_version: str):
        """
        Exécute le contrôleur de PendingChanges.
        """
        pending_changes = self.use_case.execute(
            since_version=since_version, target_version=target_version
        )
        self.presenter.present_pending_changes(pending_changes)
