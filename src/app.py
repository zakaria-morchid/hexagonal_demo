from mocks.gitlab import gl
from mocks.github import gh
import argparse
from infrastructure.providers.gitlab import GitLabProvider
from infrastructure.providers.github import GitHubProvider
from infrastructure.presenters.console import ConsolePresenter
from interfaces.cli.merge_request_controller import MergeRequestController
         
def parse_args():
    parser = argparse.ArgumentParser(description="Lister les merge requests GitLab/GitHub")
    parser.add_argument("-u", "--username", help="Filtrer par auteur GitLab/GitHub")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    
    presenter = ConsolePresenter()

    MergeRequestController(GitLabProvider(gl), presenter).run(username=args.username)
    MergeRequestController(GitHubProvider(gh), presenter).run(username=args.username)
    