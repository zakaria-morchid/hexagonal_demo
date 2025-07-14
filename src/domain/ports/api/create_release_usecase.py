"""
Module principal pour les ports de l'API.
"""

# pylint: disable=too-few-public-methods

from abc import ABC, abstractmethod
from domain.models.release import Release


class ICreateReleaseUseCase(ABC):
    """
    Interface pour le cas d’usage de création d’une release.
    """

    @abstractmethod
    def execute(
        self, since_version: str, target_version: str, created_by: str
    ) -> Release:
        """
        Crée une release entre deux versions spécifiques.
        """
