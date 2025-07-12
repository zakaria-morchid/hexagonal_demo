"""
Module principal pour les ports de présentation.
"""

# pylint: disable=too-few-public-methods
from abc import ABC, abstractmethod
from typing import List
from domain.models.model import MergeRequest


class IPresenter(ABC):
    """
    Interface pour les présentateurs.
    """

    @abstractmethod
    def present(self, merge_requests: List[MergeRequest]) -> None:
        """
        Présente les merge requests.
        """
