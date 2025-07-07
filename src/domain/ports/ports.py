from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.model import MergeRequest

class IMergeRequestProvider(ABC):
    @abstractmethod
    def list_merge_requests(self, username: Optional[str] = None) -> List[MergeRequest]:
        """
        Retourne une liste de merge requests filtrées par username si fourni.
        """
        pass
