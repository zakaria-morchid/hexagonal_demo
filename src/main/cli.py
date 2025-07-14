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
from interfaces.cli.pending_changes_controller import PendingChangesController
from interfaces.cli.release_controller import ReleaseController


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
    gitlab_provider = GitLabProvider(gl)
    github_provider = GitHubProvider(gh)

    MergeRequestController(gitlab_provider, presenter).run(username=args.username)
    MergeRequestController(github_provider, presenter).run(username=args.username)

    PendingChangesController(gitlab_provider, presenter).run(
        since_version="v1.0.0", target_version="v1.0.1"
    )
    PendingChangesController(github_provider, presenter).run(
        since_version="v1.0.0", target_version="v1.0.1"
    )

    ReleaseController(gitlab_provider, presenter).run(
        since_version="v1.0.0", target_version="v1.0.1", created_by="zmorchid"
    )
    ReleaseController(github_provider, presenter).run(
        since_version="v1.0.0", target_version="v1.0.1", created_by="zmorchid"
    )


if __name__ == "__main__":
    run_cli()
