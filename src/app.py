from mocks.gitlab import gl
from mocks.github import gh

# GitLab-like
for project in gl.projects.list():
    print(f"🦊 {project.name}")
    for mr in project.mergerequests.list():
        print(f"  ▪ {mr.title} ({mr.state})")
        for rule in mr.approvals.get().approver_rules:
            for approver in rule["approved_by"]:
                print(f"     - {'OK' if rule['approved'] else '  '} {approver['user']['name']}")

    

# GitHub-like
for repo in gh.get_user().get_repos():
    print(f"🐙 {repo.name}")
    for pr in repo.get_pulls():
        print(f"  ▪ {pr.title} ({pr.state})")
        for review in pr.get_reviews():
            print(f"     - {'OK' if review.state == 'APPROVED' else '  '} {review.user.login}")