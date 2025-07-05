from mocks.gitlab import gl
from mocks.github import gh
import argparse
from usecases.list_merge_requests import display_merge_requests
from providers.gitlab_provider import GitLabProvider
from providers.github_provider import GitHubProvider

         
def parse_args():
    parser = argparse.ArgumentParser(description="Lister les merge requests GitLab/GitHub")
    parser.add_argument("-u", "--username", help="Filtrer par auteur GitLab/GitHub")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    providers = [GitLabProvider(gl), GitHubProvider(gh)]
    for provider in providers:
        display_merge_requests(provider, username=args.username)