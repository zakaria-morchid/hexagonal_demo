from typing import List, Optional
from ..models.datamodels import Project, MergeRequest, Reviewer


class FakeGithub:
    def __init__(self, projects: List[Project]):
        self.projects = projects

    def list_all_projects(self) -> List[Project]:
        return self.projects

    def get_project_by_id(self, project_id: int) -> Optional[Project]:
        return next((p for p in self.projects if p.id == project_id), None)

    def list_merge_requests(self, project_id: int) -> List[MergeRequest]:
        project = self.get_project_by_id(project_id)
        return project.mergerequests if project else []

    def get_merge_request_by_id(self, project_id: int, mr_id: int) -> Optional[MergeRequest]:
        mrs = self.list_merge_requests(project_id)
        return next((mr for mr in mrs if mr.id == mr_id), None)

    def list_reviewers_for_merge_request(self, project_id: int, mr_id: int) -> List[Reviewer]:
        mr = self.get_merge_request_by_id(project_id, mr_id)
        return mr.reviewers if mr else []
