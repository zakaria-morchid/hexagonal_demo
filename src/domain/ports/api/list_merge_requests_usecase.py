"""
Module principal pour les ports de l'API.
"""

# pylint: disable=too-few-public-methods
from abc import ABC, abstractmethod


class IListMergeRequestsUseCase(ABC):
    """
    API : Interface exposée pour lister les merge requests
    """

    @abstractmethod
    def execute(self, username=None):
        """
        Exécute le cas d’usage de listing des merge requests,
        avec un filtrage optionnel par username.
        """
