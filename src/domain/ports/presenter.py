from abc import ABC, abstractmethod
from typing import List
from domain.models.model import MergeRequest

class IPresenter(ABC):
    @abstractmethod
    def present(self, merge_requests: List[MergeRequest]) -> None:
        """Present the merge requests in a specific format."""
        pass