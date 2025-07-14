"""
Module principal pour les mocks GitHub.
"""

# pylint: disable=too-few-public-methods
from types import SimpleNamespace
from mocks.models.datamodels import Source


class FakeGithubReview:
    """
    Classe pour les mocks de Review.
    """

    def __init__(self, reviewer):
        self.user = SimpleNamespace(login=reviewer.user.username)
        self.state = "APPROVED" if reviewer.approved else "COMMENTED"


class FakeGithubPR:
    """
    Classe pour les mocks de PR.
    """

    def __init__(self, mr):
        self.title = mr.title
        self.state = mr.state
        self.author = mr.author
        self.merged_at = mr.merged_at
        self.commit_sha = mr.commit_sha
        self._reviews = [FakeGithubReview(r) for r in mr.reviewers]

    def get_reviews(self):
        """
        Retourne les reviews.
        """
        return self._reviews


class FakeGithubRepo:
    """
    Classe pour les mocks de Repo.
    """

    def __init__(self, project):
        self.name = project.name
        self._pulls = [FakeGithubPR(mr) for mr in project.mergerequests]
        self.tags = project.tags or []
        self.source = project.source

    def get_pulls(self):
        """
        Retourne les pulls.
        """
        return self._pulls
    
    def get_tags(self):
        """
        Retourne les tags.
        """
        return self.tags


class FakeGithubUser:
    """
    Classe pour les mocks de User.
    """

    def __init__(self, repos):
        self._repos = repos

    def get_repos(self):
        """
        Retourne les repos.
        """
        return self._repos


class FakeGithub:
    """
    Classe pour les mocks de Github.
    """

    def __init__(self, all_projects):
        # Ne prendre que ceux dont le source est GITHUB
        github_projects = [p for p in all_projects if p.source == Source.GITHUB]
        repos = [FakeGithubRepo(p) for p in github_projects]
        self._user = FakeGithubUser(repos)

    def get_user(self):
        """
        Retourne l'utilisateur.
        """
        return self._user
