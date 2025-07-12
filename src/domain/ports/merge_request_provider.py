"""
Module principal pour les ports de fournisseur.
"""

# pylint: disable=too-few-public-methods
from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.model import MergeRequest


class IMergeRequestProvider(ABC):
    """
    Interface pour les fournisseurs de merge requests.
    """

    @abstractmethod
    def fetch_merge_requests(
        self, username: Optional[str] = None
    ) -> List[MergeRequest]:
        """
        Retourne une liste de merge requests filtrées par username si fourni.
        """
