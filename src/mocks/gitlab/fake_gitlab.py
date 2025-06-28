from ..models.datamodels import Source

class FakeApprovalInfo:
    def __init__(self, approver_rules):
        self.approver_rules = approver_rules

    def get(self):
        return self


class FakeGitlabMergeRequest:
    def __init__(self, mr):
        self.title = mr.title
        self.state = mr.state
        # On prépare les données dans le format attendu par python-gitlab
        self._reviewers = mr.reviewers

    @property
    def approvals(self):
        return FakeApprovalInfo([
            {
                "approved": reviewer.approved,
                "approved_by": [{"user": {"name": reviewer.user.name}}]
            }
            for reviewer in self._reviewers
        ])


class FakeMergeRequestManager:
    def __init__(self, merge_requests):
        self._mrs = merge_requests

    def list(self):
        return self._mrs


class FakeGitlabProject:
    def __init__(self, project):
        self.name = project.name
        self.mergerequests = FakeMergeRequestManager([
            FakeGitlabMergeRequest(mr) for mr in project.mergerequests
        ])


class FakeProjectManager:
    def __init__(self, projects):
        self._projects = projects

    def list(self, owned=False, all=False):
        return self._projects


class FakeGitlab:
    def __init__(self, all_projects):
        gitlab_projects = [p for p in all_projects if p.source == Source.GITLAB]
        self.projects = FakeProjectManager([FakeGitlabProject(p) for p in gitlab_projects])


class FakeProjectManager:
    def __init__(self, projects):
        self._projects = projects

    def list(self, owned=False, all=False):
        return self._projects
