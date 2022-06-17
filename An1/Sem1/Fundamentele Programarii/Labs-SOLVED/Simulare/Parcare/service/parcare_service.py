from repository.parcare_repo import InMemoryRepo
from repository.parcare_repo import InFileRepo

class ParcariService:
    def __init__(self,repo):
        self.__parcari_repo = repo

    def get_all(self):
        return self.__parcari_repo.get_all()
    def search_strada(self,strada):
        return self.__parcari_repo.search_strada(strada)

