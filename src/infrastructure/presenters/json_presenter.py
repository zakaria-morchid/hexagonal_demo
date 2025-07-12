from domain.ports.presenter import IPresenter
from domain.models.model import MergeRequest
from typing import List


class JsonPresenter(IPresenter):
    def __init__(self):
        self.result = []

    def present(self, merge_requests: List[MergeRequest]):
        self.result = [
            {
                "platform": mr.platform,
                "project": mr.project,
                "title": mr.title,
                "state": mr.state,
                "author": mr.author,
                "approvals": [
                    {"name": a.name, "approved": a.approved}
                    for a in mr.approvals
                ],
            }
            for mr in merge_requests
        ]
