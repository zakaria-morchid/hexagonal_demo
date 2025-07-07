from mocks.gitlab import gl
from mocks.github import gh
import argparse
from domain.usecases.list_merge_requests import ListMergeRequests
from providers.gitlab_provider import GitLabProvider
from providers.github_provider import GitHubProvider

         
def parse_args():
    parser = argparse.ArgumentParser(description="Lister les merge requests GitLab/GitHub")
    parser.add_argument("-u", "--username", help="Filtrer par auteur GitLab/GitHub")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    providers = [GitLabProvider(gl), GitHubProvider(gh)]
    ListMergeRequests(providers).execute(username=args.username)