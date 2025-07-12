"""
Module principal pour les mocks GitLab.
"""

# pylint: disable=too-few-public-methods
from mocks.models.datamodels import Source


class FakeApprovalInfo:
    """
    Classe pour les mocks d'approbation.
    """

    def __init__(self, approver_rules):
        self.approver_rules = approver_rules

    def get(self):
        """
        Retourne les règles d'approbation.
        """
        return self


class FakeGitlabMergeRequest:
    """
    Classe pour les mocks de MergeRequest.
    """

    def __init__(self, mr):
        self.title = mr.title
        self.state = mr.state
        self.author = mr.author
        # On prépare les données dans le format attendu par python-gitlab
        self._reviewers = mr.reviewers

    @property
    def approvals(self):
        """
        Retourne les règles d'approbation.
        """
        return FakeApprovalInfo(
            [
                {
                    "approved": reviewer.approved,
                    "approved_by": [{"user": {"name": reviewer.user.name}}],
                }
                for reviewer in self._reviewers
            ]
        )


class FakeMergeRequestManager:
    """
    Classe pour les mocks de MergeRequestManager.
    """

    def __init__(self, merge_requests):
        self._mrs = merge_requests

    def list(self):
        """
        Retourne les merge requests.
        """
        return self._mrs


class FakeGitlabProject:
    """
    Classe pour les mocks de GitlabProject.
    """

    def __init__(self, project):
        self.name = project.name
        self.mergerequests = FakeMergeRequestManager(
            [FakeGitlabMergeRequest(mr) for mr in project.mergerequests]
        )


class FakeProjectManager:
    """
    Classe pour les mocks de ProjectManager.
    """

    def __init__(self, projects):
        self._projects = projects

    def list(self):
        """
        Retourne les projets.
        """
        return self._projects


class FakeGitlab:
    """
    Classe pour les mocks de Gitlab.
    """

    def __init__(self, all_projects):
        """
        Initialise les projets.
        """
        gitlab_projects = [p for p in all_projects if p.source == Source.GITLAB]
        self.projects = FakeProjectManager(
            [FakeGitlabProject(p) for p in gitlab_projects]
        )
