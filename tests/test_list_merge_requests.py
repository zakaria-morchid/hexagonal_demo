from src.domain.usecases.list_merge_requests import ListMergeRequests
from src.domain.usecases.list_pending_changes import ListPendingChangesForRelease
from src.domain.models.release import Platform


def test_list_merge_requests_sends_data_to_presenter(fake_provider):
    # Arrange
    use_case = ListMergeRequests(fake_provider)

    # Act
    data = use_case.execute(username="zmorchid")

    # Assert
    assert data is not None
    assert len(data) == 1
    assert data[0].author == "zmorchid"
    assert data[0].project == "demo-project"
    assert data[0].approvals[0].approved is True


def test_list_pending_changes_sends_data_to_presenter(
    fake_provider
):
    # Arrange
    use_case = ListPendingChangesForRelease(
        fake_provider
    )

    # Act
    data = use_case.execute(since_version="v1.0.0", target_version="v1.0.1")

    # Assert
    assert data is not None
    assert data.target_version == "v1.0.1"
    assert len(data.changes) == 1
    assert data.changes[0].project == "demo-project"
    assert data.changes[0].title == "Fix login"
    assert data.changes[0].platform == Platform.GITLAB
    assert data.changes[0].commit_sha == "1234567890"
