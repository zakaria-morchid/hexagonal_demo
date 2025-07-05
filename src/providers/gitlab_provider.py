
from interfaces import MergeRequestProvider

class GitLabProvider(MergeRequestProvider):
    def __init__(self, client):
        self.client = client
        self.name = "GitLab"
        
    def list_merge_requests(self, username=None):
        for project in self.client.projects.list():
            for mr in project.mergerequests.list():
                if username is None or mr.author.username == username:
                    yield {
                        "platform": "GitLab",
                        "project": project.name,
                        "title": mr.title,
                        "state": mr.state,
                        "author": mr.author.username,
                        "approvals": [
                            {
                                "name": approver["user"]["name"],
                                "approved": rule["approved"]
                            }
                            for rule in mr.approvals.get().approver_rules
                            for approver in rule["approved_by"]
                        ]
                    }
