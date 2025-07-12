from domain.ports.provider import IMergeRequestProvider
from domain.ports.presenter import IPresenter
from domain.usecases.list_merge_requests import ListMergeRequests


class MergeRequestController:
    def __init__(self, provider: IMergeRequestProvider, presenter: IPresenter):
        self.use_case = ListMergeRequests(provider, presenter)

    def run(self, username=None):
        self.use_case.execute(username=username)
