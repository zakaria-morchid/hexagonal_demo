from domain.ports.ports import IMergeRequestProvider
from typing import Iterable, Optional
from domain.models.model import MergeRequest

class GitHubProvider(IMergeRequestProvider):
    def __init__(self, client):
        self.client = client
        self.name = "GitHub"

    def list_merge_requests(self, username: Optional[str] = None) -> Iterable[MergeRequest]:
        for repo in self.client.get_user().get_repos():
            for pr in repo.get_pulls():
                if username is None or pr.author.username == username:
                    yield MergeRequest(
                        platform="GitHub",
                        project=repo.name,
                        title=pr.title,
                        state=pr.state,
                        author=pr.author.username,
                        approvals=[]  # GitHub n’a pas toujours de règles d’approbation accessibles
                    )
