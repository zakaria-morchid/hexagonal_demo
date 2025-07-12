"""
Module principal pour la ligne de commande.
"""

import argparse
from mocks.gitlab import gl
from mocks.github import gh
from infrastructure.providers.gitlab import GitLabProvider
from infrastructure.providers.github import GitHubProvider
from infrastructure.presenters.console import ConsolePresenter
from interfaces.cli.merge_request_controller import MergeRequestController


def parse_args():
    """
    Parse les arguments de la ligne de commande.
    """
    parser = argparse.ArgumentParser(
        description="Lister les merge requests GitLab/GitHub"
    )
    parser.add_argument("-u", "--username", help="Filtrer par auteur GitLab/GitHub")
    return parser.parse_args()


def run_cli():
    """
    Exécute la ligne de commande.
    """
    args = parse_args()
    presenter = ConsolePresenter()

    MergeRequestController(GitLabProvider(gl), presenter).run(username=args.username)
    MergeRequestController(GitHubProvider(gh), presenter).run(username=args.username)


if __name__ == "__main__":
    run_cli()
