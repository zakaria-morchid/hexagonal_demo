"""
Module principal pour l'API.
"""

from typing import Optional, List
from fastapi import FastAPI, Query
from mocks.gitlab import gl
from mocks.github import gh
from infrastructure.providers.gitlab import GitLabProvider
from infrastructure.providers.github import GitHubProvider
from infrastructure.presenters.json_presenter import JsonPresenter
from interfaces.cli.merge_request_controller import MergeRequestController
from domain.models.model import MergeRequest

app = FastAPI()


@app.get("/merge-requests", response_model=List[MergeRequest])
def list_merge_requests(
    username: Optional[str] = Query(default=None),
) -> List[MergeRequest]:
    """
    Liste les merge requests.
    """
    results: List[MergeRequest] = []

    for provider in [GitLabProvider(gl), GitHubProvider(gh)]:
        presenter = JsonPresenter()
        controller = MergeRequestController(provider, presenter)
        controller.run(username=username)
        results.extend(presenter.result)

    return results
