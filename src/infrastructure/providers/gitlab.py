"""
Module principal pour les mocks GitLab.
"""

# pylint: disable=too-few-public-methods
from typing import Iterable, Optional, List
from domain.ports.merge_request_provider import IMergeRequestProvider
from domain.models.model import MergeRequest, Approval
from domain.models.release import Change
from mocks.models.datamodels import MergeRequestState, Tag


class GitLabProvider(IMergeRequestProvider):
    """
    Classe pour les mocks de GitLabProvider.
    """

    def __init__(self, client):
        self.client = client
        self.name = "GitLab"

    def fetch_merge_requests(
        self, username: Optional[str] = None
    ) -> Iterable[MergeRequest]:
        """
        Récupère les merge requests GitLab pour un utilisateur spécifique.
        """
        for project in self.client.projects.list():
            for mr in project.mergerequests.list():
                if username is None or mr.author.username == username:
                    yield MergeRequest(
                        platform="GitLab",
                        project=project.name,
                        title=mr.title,
                        state=mr.state,
                        author=mr.author.username,
                        approvals=[
                            Approval(
                                name=approver["user"]["name"], approved=rule["approved"]
                            )
                            for rule in mr.approvals.get().approver_rules
                            for approver in rule["approved_by"]
                        ],
                    )

    def list_merged_changes_since(self, version_tag: str) -> List[Change]:
        """
        Liste les changements fusionnés depuis un tag donné.
        """
        changes: List[Change] = []

        for project in self.client.projects.list():
            tag = self._find_tag(project.tags, version_tag)
            if not tag:
                continue  # tag non trouvé pour ce projet

            for mr in project.mergerequests.list():
                if (
                    mr.state == MergeRequestState.MERGED
                    and mr.merged_at
                    and mr.merged_at > tag.committed_date
                ):
                    changes.append(
                        Change(
                            platform=project.source,
                            project=project.name,
                            title=mr.title,
                            author=mr.author.username,
                            merged_at=mr.merged_at.isoformat(),
                            commit_sha=mr.commit_sha,
                        )
                    )

        return changes

    def _find_tag(self, tags: Optional[List[Tag]], version_tag: str) -> Optional[Tag]:
        if not tags:
            return None
        for tag in tags:
            if tag.name == version_tag:
                return tag
        return None
