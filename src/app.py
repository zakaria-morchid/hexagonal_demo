from mocks.gitlab import gl
from mocks.github import gh
import argparse

def print_gitlab_mr_infos(mr):
    print(f"  ▪ {mr.title} ({mr.state})")
    print(f"    Auteur : {mr.author.username}")
    for rule in mr.approvals.get().approver_rules:
        for approver in rule["approved_by"]:
            print(f"     - {'OK' if rule['approved'] else '  '} {approver['user']['name']}")

def print_github_pr_infos(pr):
    print(f"  ▪ {pr.title} ({pr.state})")
    print(f"    Auteur : {pr.author.username}")
    for review in pr.get_reviews():
        print(f"     - {'OK' if review.state == 'APPROVED' else '  '} {review.user.login}")

def print_users_merge_requests_gitlab():
    for project in gl.projects.list():
        print(f"🦊 [GITLAB] {project.name}")
        for mr in project.mergerequests.list():
            print_gitlab_mr_infos(mr)



def print_user_merge_requests_gitlab(username):
    for project in gl.projects.list():
        print(f"🦊 [GITLAB] {project.name}")
        for mr in project.mergerequests.list():
            if mr.author.username == username:
                print_gitlab_mr_infos(mr)

def print_users_merge_requests_github():
    for repo in gh.get_user().get_repos():
        print(f"🐙 [GITHUB] {repo.name}")
        for pr in repo.get_pulls():
            print_github_pr_infos(pr)

def print_user_merge_requests_github(username):
    for repo in gh.get_user().get_repos():
        print(f"🐙 [GITHUB] {repo.name}")
        for pr in repo.get_pulls():
            if pr.author.username == username:
                print_github_pr_infos(pr)
            
            
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lister les merge requests GitLab")
    parser.add_argument("-u", "--username", help="Filtrer par auteur GitLab (username)")
    args = parser.parse_args()

    if args.username:
        print_user_merge_requests_gitlab(args.username)
    else:
        print_users_merge_requests_gitlab()

    if args.username:
        print_user_merge_requests_github(args.username)
    else:
        print_users_merge_requests_github()
         