from abc import ABC, abstractmethod

class IListMergeRequestsUseCase(ABC):
    @abstractmethod
    def execute(self, username=None):
        """
        Exécute le cas d’usage de listing des merge requests,
        avec un filtrage optionnel par username.
        """
        pass


class ListMergeRequests(IListMergeRequestsUseCase):
    def __init__(self, providers):
        self.providers = providers

    def execute(self, username=None):
        for provider in self.providers:
            self._display_merge_requests(provider, username=username)
        
    def _display_merge_requests(self, provider, username=None):
        print(f"🛠️  [{provider.name}]")
        for mr in provider.list_merge_requests(username=username):
            print(f"  ▪ {mr['project']}")
            print(f"  ▪ {mr['title']} ({mr['state']})")
            print(f"    Auteur : {mr['author']}")
            for approval in mr["approvals"]:
                print(f"     - {'OK' if approval['approved'] else '  '} {approval['name']}")
