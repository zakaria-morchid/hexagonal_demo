from unittest.mock import MagicMock
from ..models.datamodels import Project, MergeRequest


class FakeMergeRequestManager:
    def __init__(self, merge_requests: list[MergeRequest]):
        self._mrs = merge_requests

    def list(self):
        return self._mrs

    def get(self, mr_id: int):
        return next((mr for mr in self._mrs if mr.id == mr_id), None)

    def get_reviewers(self, mr_id: int):
        mr = self.get(mr_id)
        return mr.reviewers if mr else []


class FakeProjectManager:
    def __init__(self, projects: list[Project]):
        self._projects = projects

    def list(self):
        return self._projects

    def get(self, project_id: int):
        return next((p for p in self._projects if p.id == project_id), None)

    def get_merge_requests(self, project_id: int):
        project = self.get(project_id)
        return FakeMergeRequestManager(project.mergerequests) if project else None


class FakeGitlab:
    def __init__(self, projects: list[Project]):
        self.projects = FakeProjectManager(projects)
