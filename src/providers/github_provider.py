from interfaces import MergeRequestProvider

class GitHubProvider(MergeRequestProvider):
    def __init__(self, client):
        self.client = client
        self.name = "GitHub"

    def list_merge_requests(self, username=None):
        for repo in self.client.get_user().get_repos():
            for pr in repo.get_pulls():
                if username is None or pr.author.username == username:
                    yield {
                        "platform": "GitHub",
                        "project": repo.name,
                        "title": pr.title,
                        "state": pr.state,
                        "author": pr.author.username,
                        "approvals": []  # GitHub n’a pas toujours de règles d’approbation accessibles
                    }
