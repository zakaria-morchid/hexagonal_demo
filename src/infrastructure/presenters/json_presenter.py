"""
Module principal pour le présentateur JSON.
"""

# pylint: disable=too-few-public-methods
from typing import List
from domain.ports.presenter import IPresenter
from domain.models.model import MergeRequest


class JsonPresenter(IPresenter):
    """
    Classe pour le présentateur JSON.
    """

    def __init__(self):
        """
        Initialise le présentateur JSON.
        """
        self.result = []

    def present(self, merge_requests: List[MergeRequest]):
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
