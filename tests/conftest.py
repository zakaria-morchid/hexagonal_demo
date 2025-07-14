from datetime import datetime
import pytest
from src.domain.ports.spi.merge_request_provider import IMergeRequestProvider
from src.domain.ports.spi.pending_changes_provider import IPendingChangesProvider
from src.domain.ports.spi.presenter import IMergeRequestPresenter, IPendingChangesPresenter
from src.domain.models.model import MergeRequest, Approval
from src.domain.models.release import PendingChanges, Change, Platform
from typing import List, Optional


class FakeProvider(IMergeRequestProvider, IPendingChangesProvider):
    def fetch_merge_requests(
        self, username: Optional[str] = None
    ) -> List[MergeRequest]:
        return [
            MergeRequest(
                platform=Platform.GITLAB,
                project="demo-project",
                title="Fix bug",
                state="opened",
                author="zmorchid",
                approvals=[
                    Approval(name="reviewer1", approved=True),
                    Approval(name="reviewer2", approved=False),
                ],
            )
        ]

    def list_merged_changes_since(self, version_tag: str) -> List[Change]:
        return [
            Change(
                project="demo-project",
                title="Fix login",
                author="zmorchid",
                merged_at=datetime.now().isoformat(),
                platform=Platform.GITLAB,
                commit_sha="1234567890",
            )
        ]


class FakeMergeRequestPresenter(IMergeRequestPresenter):
    def __init__(self):
        self.presented_data = None

    def present_merge_requests(self, merge_requests: List[MergeRequest]):
        self.presented_data = merge_requests


class FakePendingChangesPresenter(IPendingChangesPresenter):
    def __init__(self):
        self.presented_data = None

    def present_pending_changes(self, pending_changes: PendingChanges):
        self.presented_data = pending_changes


@pytest.fixture
def fake_provider():
    return FakeProvider()


@pytest.fixture
def fake_merge_request_presenter():
    return FakeMergeRequestPresenter()


@pytest.fixture
def fake_pending_changes_presenter():
    return FakePendingChangesPresenter()
