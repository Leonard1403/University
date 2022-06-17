from domain.entities import Carti
from domain.entities import Clienti
from repository.library_repo import InMemoryRepository

class LibraryService:
    def __init__(self,repo,validator):

        self.__repo = repo
        self.__validator = validator

    def add_carti(self,id, titlu, descriere, autor):

        o = Carti(id,titlu,descriere,autor)

        self.__validator.validate_carti(o)
        self.__repo.store_carti(o)
        return o

    def add_clienti(self,id, nume, CNP):

        o = Clienti(id,nume,CNP)

        self.__validator.validate_clienti(o)
        self.__repo.store_clienti(o)
        return o

    def get_all_carti(self):
        return self.__repo.get_all_carti()

    def get_all_clienti(self):
        return self.__repo.get_all_clienti()

def Default():
    client1 = Clienti(1,'Leonard','1234567891123')
    client2 = Clienti(1,'Leonard','1234567891123')
    client3 = Clienti(1,'Leonard','1234567891123')
    client4 = Clienti(1,'Leonard','1234567891123')
    client5 = Clienti(1,'Leonard','1234567891123')
    client6 = Clienti(1,'Leonard','1234567891123')
