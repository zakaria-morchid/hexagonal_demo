"""
Module principal pour le présentateur de Console.
"""

# pylint: disable=too-few-public-methods
from datetime import datetime
from typing import List
from domain.ports.spi.presenter import IMergeRequestPresenter, IPendingChangesPresenter
from domain.models.model import MergeRequest
from domain.models.release import PendingChanges


class ConsolePresenter(IMergeRequestPresenter, IPendingChangesPresenter):
    """
    Classe pour le présentateur de Console.
    """

    def present_merge_requests(self, merge_requests: List[MergeRequest]) -> None:
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

    def present_pending_changes(self, pending_changes: PendingChanges) -> None:
        """
        Présente les changements en attente.
        """
        print(f"📦 Version cible : {pending_changes.target_version}")
        print("📝 Changements depuis le dernier tag :")
        for change in pending_changes.changes:
            merged_at_str = change.merged_at or "inconnue"
            elapsed = ""
            if change.merged_at:
                merged_at = datetime.fromisoformat(change.merged_at)
                delta = datetime.now() - merged_at
                elapsed = f"il y a {delta.days} jours"
            print(
                f"▪ [{change.platform.value}] {change.project} - {change.title} ({change.author})"
            )
            print(f"   🕒 fusionné le {merged_at_str} ({elapsed})")
            print(f"   🔗 {change.commit_sha}")
            print()
