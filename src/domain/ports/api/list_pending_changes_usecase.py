"""
Module principal pour les ports de l'API.
"""

# pylint: disable=too-few-public-methods
from abc import ABC, abstractmethod


class IListPendingChangesForRelease(ABC):
    """
    API : Interface exposée pour lister les changements en attente
    """

    @abstractmethod
    def execute(self, since_version: str, target_version: str):
        """
        Liste les changements en attente pour une version spécifique.
        """
