"""
Module principal pour les ports de présentation.
"""

# pylint: disable=too-few-public-methods
from abc import ABC, abstractmethod
from typing import List
from domain.models.model import MergeRequest
from domain.models.release import PendingChanges


class IMergeRequestPresenter(ABC):
    """
    Interface pour les présentateurs de merge requests.
    """

    @abstractmethod
    def present_merge_requests(self, merge_requests: List[MergeRequest]) -> None:
        """
        Présente les merge requests.
        """

class IPendingChangesPresenter(ABC):
    """
    Interface pour les présentateurs de changements en attente.
    """

    @abstractmethod
    def present_pending_changes(self, pending_changes: PendingChanges) -> None:
        """
        Présente les changements en attente.
        """