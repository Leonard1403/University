from domain.entities import Clienti
from repository.library_repo import InMemoryRepository
# from repository.clienti import ClientiMemoryRepository
from domain.validators import ClientiValidator

class ClientiService:
    """
    Clasa ClientiService contine toate functiile utile
    pentru a gestiona lista de clienti
    """
    def __init__(self,repo,validator):
        self.__repo = repo
        self.__validator = validator

    def get_all_clienti(self):
        return self.__repo.get_all()

    def add_clienti(self,id,nume,CNP):
        """
        Functia de add_clienti adauga clienti in lista dupa id, nume si CNP
        :param id: Id-ul clientului pe care doriti sa-l introduceti
        :param nume: Numele clientului
        :param CNP: CNP-ul clientului
        :return:
        """
        client = Clienti(id,nume,CNP)
        self.__validator.validate(client)
        self.__repo.store(client)
        return client

    def gen_random_clienti(self,id):
        # numar = self.__repo.randomint(5,10)
        # # id = self.__repo.randomint(100,200)
        # nume = self.__repo.randomword(numar)
        # CNP = self.__repo.CNP_Generator()
        client = self.__repo.generate_client(id)
        # self.__validator.validate_clienti(client)
        # self.__repo.store(client)
        return client

    def show_clienti(self):
        return self.__repo.get_all()

    def delete_clienti_id(self, id):
        return self.__repo.deleteId(id)

    def update_clienti_id(self,id,nume,CNP):
        client1 = Clienti(id,nume,CNP)
        self.__validator.validate(client1)
        return self.__repo.update_clienti(id,client1)

    def search_clienti_id(self,id):
        return self.__repo.search(id)

    def algh_sort_nume(self,lista):
        """
        Algoritm de sortare lista dupa nume
        :param lista:
        :return:
        """
        n = len(lista)
        for el1 in range(0,n,+1):
            for el2 in range(0,n,+1):
                client1 = lista[el1].getClient()
                nume1 = client1.getNume()

                client2 = lista[el2].getClient()
                nume2 = client2.getNume()

                if nume1 < nume2:
                    aux = lista[el1]
                    lista[el1] = lista[el2]
                    lista[el2] = aux
        return lista

    def Default(self):
        client1 = Clienti(1,    'Leonard',      '1234567891126')
        self.__validator.validate(client1)
        self.__repo.store(client1)

        client2 = Clienti(2,    'Dorel',        '1298567891126')
        self.__validator.validate(client2)
        self.__repo.store(client2)

        client3 = Clienti(3,    'Marin',        '6834567891126')
        self.__validator.validate(client3)
        self.__repo.store(client3)

        client4 = Clienti(4,    'Adi Despot',   '3334567891126')
        self.__validator.validate(client4)
        self.__repo.store(client4)

        client5 = Clienti(5,    'Marian',       '0734567891126')
        self.__validator.validate(client5)
        self.__repo.store(client5)


        client6 = Clienti(6,    'Miruna',       '1298479182726')
        self.__validator.validate(client6)
        self.__repo.store(client6)
        return self.__repo