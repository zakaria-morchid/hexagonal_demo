from abc import ABC, abstractmethod
from typing import List
from domain.models.model import MergeRequest

class IListMergeRequestsUseCase(ABC):
    @abstractmethod
    def execute(self, username=None):
        """
        Exécute le cas d’usage de listing des merge requests,
        avec un filtrage optionnel par username.
        """
        pass


class ListMergeRequests(IListMergeRequestsUseCase):
    def __init__(self, mr: List[MergeRequest]):
        self.mr = mr

    def execute(self):
        self._display_merge_requests()
        
    def _display_merge_requests(self):
        for mr in self.mr:
            print(f"🛠️  [{mr.platform}]")
            print(f"  ▪ {mr.project}")
            print(f"  ▪ {mr.title} ({mr.state})")
            print(f"    Auteur : {mr.author}")
            for approval in mr.approvals:
                print(f"     - {'OK' if approval.approved else '  '} {approval.name}")
