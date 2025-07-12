"""
Module principal pour les ports de fournisseur de changelog.
"""

# pylint: disable=too-few-public-methods
from abc import ABC, abstractmethod
from typing import List
from domain.models.release import Change


class IPendingChangesProvider(ABC):
    """
    Interface pour les fournisseurs de changelog.
    """

    @abstractmethod
    def list_merged_changes_since(self, version_tag: str) -> List[Change]:
        """
        Liste les changements fusionnés depuis une version spécifique.
        """
