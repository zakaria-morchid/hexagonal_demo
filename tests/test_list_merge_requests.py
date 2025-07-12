from domain.usecases.list_merge_requests import ListMergeRequests
from domain.models.model import MergeRequest, Approval
from domain.ports.provider import IMergeRequestProvider
from domain.ports.presenter import IPresenter
from typing import List, Optional





def test_list_merge_requests_sends_data_to_presenter(fake_provider, fake_presenter):
    # Arrange
    use_case = ListMergeRequests(fake_provider, fake_presenter)

    # Act
    use_case.execute(username="zmorchid")

    # Assert
    assert fake_presenter.presented_data is not None
    assert len(fake_presenter.presented_data) == 1
    assert fake_presenter.presented_data[0].author == "zmorchid"
    assert fake_presenter.presented_data[0].project == "demo-project"
    assert fake_presenter.presented_data[0].approvals[0].approved is True
