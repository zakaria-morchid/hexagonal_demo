"""
Module principal pour le contrôleur de Release.
"""

# pylint: disable=too-few-public-methods
from domain.ports.spi.release_provider import IReleaseProvider
from domain.ports.spi.presenter import IReleasePresenter
from domain.usecases.create_release_from_pending import CreateReleaseFromPendingChanges


class ReleaseController:
    """
    Classe pour le contrôleur de Release.
    """

    def __init__(self, provider: IReleaseProvider, presenter: IReleasePresenter):
        self.use_case = CreateReleaseFromPendingChanges(provider)
        self.presenter = presenter

    def run(self, since_version: str, target_version: str, created_by: str):
        """
        Exécute le contrôleur de Release.
        """
        release = self.use_case.execute(
            since_version=since_version,
            target_version=target_version,
            created_by=created_by,
        )
        self.presenter.present_release(release)
