from types import SimpleNamespace
from ..models.datamodels import Source

class FakeGithubReview:
    def __init__(self, reviewer):
        self.user = SimpleNamespace(login=reviewer.user.username)
        self.state = "APPROVED" if reviewer.approved else "COMMENTED"


class FakeGithubPR:
    def __init__(self, mr):
        self.title = mr.title
        self.state = mr.state
        self.author = mr.author
        self._reviews = [FakeGithubReview(r) for r in mr.reviewers]

    def get_reviews(self):
        return self._reviews


class FakeGithubRepo:
    def __init__(self, project):
        self.name = project.name
        self._pulls = [FakeGithubPR(mr) for mr in project.mergerequests]

    def get_pulls(self, state="open"):
        return self._pulls


class FakeGithubUser:
    def __init__(self, repos):
        self._repos = repos

    def get_repos(self):
        return self._repos


class FakeGithub:
    def __init__(self, all_projects):
        # Ne prendre que ceux dont le source est GITHUB
        github_projects = [p for p in all_projects if p.source == Source.GITHUB]
        repos = [FakeGithubRepo(p) for p in github_projects]
        self._user = FakeGithubUser(repos)

    def get_user(self):
        return self._user
