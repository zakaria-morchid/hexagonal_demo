"""
Module principal pour les mocks GitHub.
"""

# pylint: disable=too-few-public-methods
from typing import Iterable, Optional, List
from domain.ports.merge_request_provider import IMergeRequestProvider
from domain.models.model import MergeRequest
from domain.models.release import Change
from mocks.models.datamodels import MergeRequestState, Tag, Source


class GitHubProvider(IMergeRequestProvider):
    """
    Classe pour les mocks de GitHubProvider.
    """

    def __init__(self, client):
        self.client = client
        self.name = "GitHub"

    def fetch_merge_requests(
        self, username: Optional[str] = None
    ) -> Iterable[MergeRequest]:
        """
        Récupère les merge requests GitHub pour un utilisateur spécifique.
        """
        for repo in self.client.get_user().get_repos():
            for pr in repo.get_pulls():
                if username is None or pr.author.username == username:
                    yield MergeRequest(
                        platform="GitHub",
                        project=repo.name,
                        title=pr.title,
                        state=pr.state,
                        author=pr.author.username,
                        approvals=[],  # GitHub n’a pas toujours de règles d’approbation accessibles
                    )

    def list_merged_changes_since(self, version_tag: str) -> List[Change]:
        changes: List[Change] = []

        for repo in self.client.get_user().get_repos():
            tag = self._find_tag(repo.get_tags(), version_tag)
            if not tag:
                continue

            for pr in repo.get_pulls():
                if (
                    pr.state == MergeRequestState.MERGED
                    and pr.merged_at
                    and pr.merged_at > tag.committed_date
                ):
                    changes.append(
                        Change(
                            project=repo.name,
                            title=pr.title,
                            author=pr.author.username,
                            merged_at=pr.merged_at.isoformat(),
                            platform=Source.GITHUB,
                            commit_sha=pr.commit_sha,
                        )
                    )

        return changes

    def _find_tag(self, tags: List[Tag], version_tag: str) -> Optional[Tag]:
        for tag in tags:
            if tag.name == version_tag:
                return tag
        return None
