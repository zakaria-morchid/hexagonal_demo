import pytest
from domain.ports.provider import IMergeRequestProvider
from domain.ports.presenter import IPresenter
from domain.models.model import MergeRequest, Approval
from typing import List, Optional


class FakeProvider(IMergeRequestProvider):
    def fetch_merge_requests(self, username: Optional[str] = None) -> List[MergeRequest]:
        return [
            MergeRequest(
                platform="GitLab",
                project="demo-project",
                title="Fix bug",
                state="opened",
                author="zmorchid",
                approvals=[
                    Approval(name="reviewer1", approved=True),
                    Approval(name="reviewer2", approved=False),
                ]
            )
        ]


class FakePresenter(IPresenter):
    def __init__(self):
        self.presented_data = None

    def present(self, merge_requests: List[MergeRequest]):
        self.presented_data = merge_requests


@pytest.fixture
def fake_provider():
    return FakeProvider()

@pytest.fixture
def fake_presenter():
    return FakePresenter()
