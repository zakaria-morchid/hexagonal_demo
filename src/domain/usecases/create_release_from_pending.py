"""
Module principal pour le cas d’usage de création d’une release à partir des changements en attente.
"""

from domain.ports.api.create_release_usecase import ICreateReleaseUseCase
from domain.ports.spi.pending_changes_provider import IPendingChangesProvider
from domain.models.release import Release

# pylint: disable=too-few-public-methods


class CreateReleaseFromPendingChanges(ICreateReleaseUseCase):
    """
    Classe pour le cas d’usage de création d’une release à partir des changements en attente.
    """

    def __init__(self, provider: IPendingChangesProvider):
        self.provider = provider

    def execute(
        self, since_version: str, target_version: str, created_by: str
    ) -> Release:
        """
        Crée une release à partir des changements en attente.
        """
        changes = self.provider.create_release(
            since_version, target_version, created_by
        )
        return changes
