from src.domain.usecases.list_merge_requests import ListMergeRequests
from src.domain.usecases.list_pending_changes import ListPendingChangesForRelease
from src.domain.models.release import Platform


def test_list_merge_requests_sends_data_to_presenter(
    fake_provider, fake_merge_request_presenter
):
    # Arrange
    use_case = ListMergeRequests(fake_provider, fake_merge_request_presenter)

    # Act
    use_case.execute(username="zmorchid")

    # Assert
    assert fake_merge_request_presenter.presented_data is not None
    assert len(fake_merge_request_presenter.presented_data) == 1
    assert fake_merge_request_presenter.presented_data[0].author == "zmorchid"
    assert fake_merge_request_presenter.presented_data[0].project == "demo-project"
    assert fake_merge_request_presenter.presented_data[0].approvals[0].approved is True


def test_list_pending_changes_sends_data_to_presenter(
    fake_provider, fake_pending_changes_presenter
):
    # Arrange
    use_case = ListPendingChangesForRelease(
        fake_provider, fake_pending_changes_presenter
    )

    # Act
    use_case.execute(since_version="v1.0.0", target_version="v1.0.1")

    # Assert
    pending = fake_pending_changes_presenter.presented_data
    assert pending is not None
    assert pending.target_version == "v1.0.1"
    assert len(pending.changes) == 1
    assert pending.changes[0].project == "demo-project"
    assert pending.changes[0].title == "Fix login"
    assert pending.changes[0].platform == Platform.GITLAB
    assert pending.changes[0].commit_sha == "1234567890"
