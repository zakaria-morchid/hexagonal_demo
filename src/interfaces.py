from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import List, Optional

class Approval(BaseModel):
    name: str
    approved: bool
class MergeRequest(BaseModel):
    platform: str
    project: str
    title: str
    state: str
    author: str
    approvals: List[Approval]
class MergeRequestProvider(ABC):
    @abstractmethod
    def list_merge_requests(self, username: Optional[str] = None) -> List[MergeRequest]:
        """
        Retourne une liste de merge requests filtrées par username si fourni.
        """
        pass
