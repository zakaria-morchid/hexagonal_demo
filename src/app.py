from mocks.gitlab import gl
from mocks.github import gh
import argparse
from domain.usecases.list_merge_requests import ListMergeRequests
from infrastructure.providers.gitlab import GitLabProvider
from infrastructure.providers.github import GitHubProvider
from infrastructure.presenters.console import ConsolePresenter
         
def parse_args():
    parser = argparse.ArgumentParser(description="Lister les merge requests GitLab/GitHub")
    parser.add_argument("-u", "--username", help="Filtrer par auteur GitLab/GitHub")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    
    presenter = ConsolePresenter()

    provider_gitlab = GitLabProvider(gl)
    use_case_gitlab = ListMergeRequests(provider_gitlab, presenter)
    use_case_gitlab.execute(username=args.username)

    provider_github = GitHubProvider(gh)
    use_case_github = ListMergeRequests(provider_github, presenter)
    use_case_github.execute(username=args.username)
    