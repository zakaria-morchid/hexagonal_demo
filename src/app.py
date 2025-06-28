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
            
            
            
            
def get_user_merge_requests(username: str, gitlab):
    mrs_by_user = []

    for project in gitlab.projects.list():
        for mr in project.mergerequests.list():
            is_author = mr._reviewers[0].user.username == username
            is_reviewer = any(r.user.username == username for r in mr._reviewers)
            if is_author or is_reviewer:
                mrs_by_user.append({
                    "project": project.name,
                    "title": mr.title,
                    "state": mr.state,
                    "author": mr._reviewers[0].user.username,
                    "as_author": is_author,
                    "as_reviewer": is_reviewer
                })
    return mrs_by_user

print(get_user_merge_requests("zmorchid", gl))