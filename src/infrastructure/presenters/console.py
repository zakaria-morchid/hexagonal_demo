from domain.ports.presenter import IPresenter
from domain.models.model import MergeRequest
from typing import List

class ConsolePresenter(IPresenter):
    def present(self, merge_requests: List[MergeRequest]) -> None:
        for mr in merge_requests:
            print(f"🛠️  [{mr.platform}]")
            print(f"  ▪ {mr.project}")
            print(f"  ▪ {mr.title} ({mr.state})")
            print(f"    Auteur : {mr.author}")
            for approval in mr.approvals:
                print(f"     - {'OK' if approval.approved else '  '} {approval.name}")
