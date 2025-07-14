"""
Module principal pour les ports secondaires.
"""

# pylint: disable=too-few-public-methods
from abc import ABC, abstractmethod
from domain.models.release import Release


class IReleaseProvider(ABC):
    """
    Interface pour les fournisseurs de release.
    """

    @abstractmethod
    def create_release(
        self, since_version: str, target_version: str, created_by: str
    ) -> Release:
        """
        Crée une release.
        """
