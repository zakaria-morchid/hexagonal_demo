"""
Module principal pour l'API.
"""

from typing import Optional
from fastapi import FastAPI, Query
from mocks.gitlab import gl
from mocks.github import gh
from infrastructure.providers.gitlab import GitLabProvider
from infrastructure.providers.github import GitHubProvider
from infrastructure.presenters.json_presenter import JsonPresenter
from interfaces.cli.merge_request_controller import MergeRequestController

app = FastAPI()


@app.get("/merge-requests")
def list_merge_requests(username: Optional[str] = Query(default=None)):
    """
    Liste les merge requests.
    """
    results = []

    for provider in [GitLabProvider(gl), GitHubProvider(gh)]:
        presenter = JsonPresenter()
        controller = MergeRequestController(provider, presenter)
        controller.run(username=username)
        results.extend(presenter.result)

    return results
