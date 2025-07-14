"""
Module principal pour le présentateur JSON.
"""

# pylint: disable=too-few-public-methods
from typing import List
from domain.ports.presenter import IMergeRequestPresenter
from domain.models.model import MergeRequest
from domain.models.release import PendingChanges


class JsonPresenter(IMergeRequestPresenter):
    """
    Classe pour le présentateur JSON.
    """

    def __init__(self):
        """
        Initialise le présentateur JSON.
        """
        self.result = []

    def present_merge_requests(self, merge_requests: List[MergeRequest]):
        """
        Présente les merge requests.
        """
        self.result = [
            {
                "platform": mr.platform,
                "project": mr.project,
                "title": mr.title,
                "state": mr.state,
                "author": mr.author,
                "approvals": [
                    {"name": a.name, "approved": a.approved} for a in mr.approvals
                ],
            }
            for mr in merge_requests
        ]


    def present_pending_changes(self, pending_changes: PendingChanges):
        """
        Présente les changements en attente.
        """
        self.result = [
            {
                "project": c.project,
                "title": c.title,
                "author": c.author,
                "merged_at": c.merged_at,
                "platform": c.platform,
                "commit_sha": getattr(c, "commit_sha", None),
            }
            for c in pending_changes.changes
        ]