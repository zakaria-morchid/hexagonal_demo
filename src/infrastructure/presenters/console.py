"""
Module principal pour le présentateur de Console.
"""

# pylint: disable=too-few-public-methods
from typing import List
from domain.ports.presenter import IPresenter
from domain.models.model import MergeRequest


class ConsolePresenter(IPresenter):
    """
    Classe pour le présentateur de Console.
    """

    def present(self, merge_requests: List[MergeRequest]) -> None:
        """
        Présente les merge requests.
        """
        for mr in merge_requests:
            print(f"🛠️  [{mr.platform}]")
            print(f"  ▪ {mr.project}")
            print(f"  ▪ {mr.title} ({mr.state})")
            print(f"    Auteur : {mr.author}")
            for approval in mr.approvals:
                print(f"     - {'OK' if approval.approved else '  '} {approval.name}")
