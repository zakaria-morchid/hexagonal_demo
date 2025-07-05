from abc import ABC, abstractmethod

class MergeRequestProvider(ABC):
    @abstractmethod
    def list_merge_requests(self, username=None):
        """
        Retourne une liste de merge requests filtrées par username si fourni.
        """
        pass
