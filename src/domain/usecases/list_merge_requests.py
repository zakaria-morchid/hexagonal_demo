from abc import ABC, abstractmethod
from typing import List
from domain.models.model import MergeRequest
from domain.ports.presenter import IPresenter

class IListMergeRequestsUseCase(ABC):
    @abstractmethod
    def execute(self, username=None):
        """
        Exécute le cas d’usage de listing des merge requests,
        avec un filtrage optionnel par username.
        """
        pass


class ListMergeRequests(IListMergeRequestsUseCase):
    def __init__(self, merge_requests : List[MergeRequest], presenter: IPresenter):
        self.merge_requests  = merge_requests 
        self.presenter = presenter

    def execute(self):
        self.presenter.present(self.merge_requests)
    
