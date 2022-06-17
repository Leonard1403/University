from repository.library_repo import InMemoryRepository

from domain.entities import Inchirieri
from domain.entities import Clienti
from domain.entities import Carti

# from service.carti_service import CartiService

from repository.inchirieri import InchirieriMemoryRepository
from domain.validators import InchiriereValidator, CartiValidator, ClientiValidator
from termcolor import colored

from domain.entities import Perioada
from service.carti_service import CartiService
from service.clienti_service import ClientiService


class InchirieriService:
    def __init__(self, inchirieri_repo , client_repo , carte_repo , inchirieri_vali):
        self.__inchirieri_repo = inchirieri_repo
        self.__client_repo = client_repo
        self.__carte_repo = carte_repo
        self.__inchirieri_vali = inchirieri_vali

    def add_inchirieri(self, client_id , carte_id , perioada):

        client = self.__client_repo.search(client_id)
        if client is None:
            print(colored("Nu exista acest client",'red'))
            return

        carte = self.__carte_repo.search(carte_id)

        if carte is None:
            print(colored("Nu exista aceasta carte",'red'))
            return

        inchirieri = Inchirieri(client,carte,perioada)
        self.__inchirieri_vali.validate(inchirieri)
        self.__inchirieri_repo.store(inchirieri)
        return inchirieri

    def show_inchirieri(self):
        return self.__inchirieri_repo.get_all()

    def get_all(self):
        return self.__inchirieri_repo.get_all()

    def algh_sort_nume(self,lista):
        """
        Algoritm de sortare lista dupa nume
        :param lista:
        :return:
        """
        return self.__inchirieri_repo.algh_sort_nume(lista)

    def delete_inchiriere(self, nume , titlu):
        return self.__inchirieri_repo.deleteInchiriere(nume,titlu)

    def __exist(self,lista,titlu):
        """
        Funtie care verifica daca in lista de inchiriate exista
        o carte cu un titlu dat
        :param lista:
        :param titlu:
        :return:
        """
        i = 0
        for obj in lista:
            carte_titlu = obj.getTitlu()
            if carte_titlu == titlu:
                return i
            i = i + 1
        return False

    def best_inchiriat(self):
        lista_carti_inchiriate , id_maxim , nr_inchirieri = self.__inchirieri_repo.best_inchiriat()
        return lista_carti_inchiriate , id_maxim , nr_inchirieri

#-----------------------------------------------------------------------------------------------------------------------

    def client_nrinc(self):
        """
        Functi care returneaza in functie de numarul de carti inchiriate dupa client
        :return:
        """
        return self.__inchirieri_repo.client_nrinc()

    def sorted_by_cr(self,lista):
        return self.__inchirieri_repo.sorted_by_cr(lista)

# ----------------------------------------------------------------------------------------------------------------------

    def nr_apar_autor(self,nume):
        """
        Functie care determina numarul de aparitii intr-o lista de inchirieri petru un autor dupa nume
        :param nume:
        :return:
        """
        return self.__inchirieri_repo.nr_apar_autor(nume)

    def autor_nrinc(self):
        """
        Functia calculeaza numarul de inchirieri pe care il are un autor din lista
        :return: returneaza lista de autori cu numarul de inchirieri sub forma de dictionar
        """
        return self.__inchirieri_repo.autor_nrinc()

# ----------------------------------------------------------------------------------------------------------------------

    # def lista_nume(self):
    #     lista_carti_inchiriate = [0]*1000
    #     id_maxim = 0
    #     ls_inchiriate = self.__inchirieri_repo.get_all()
    #     for el in ls_inchiriate:
    #         client = el.getClient()
    #         lista_carti_inchiriate.append(client)
    #         if int(client.getId()) > id_maxim:
    #             id_maxim = int(client.getId())
    #     return lista_carti_inchiriate , id_maxim

    def Default(self):
        start = 2000
        stop = 2010
        period = Perioada(start,stop)
        chirie1 = self.add_inchirieri(2,2,period)

        start = 2002
        stop = 2008
        period = Perioada(start, stop)
        chirie2 = self.add_inchirieri(4, 3, period)

        start = 2002
        stop = 2009
        period = Perioada(start, stop)
        chirie3 = self.add_inchirieri(1, 3, period)

        start = 2005
        stop = 2007
        period = Perioada(start, stop)
        chirie4 = self.add_inchirieri(2, 1, period)

        start = 2009
        stop = 2021
        period = Perioada(start, stop)
        chirie5 = self.add_inchirieri(3, 1, period)

        start = 2009
        stop = 2021
        period = Perioada(start, stop)
        chirie6 = self.add_inchirieri(5, 2, period)

        start = 2010
        stop = 2019
        period = Perioada(start,stop)
        chirie7 = self.add_inchirieri(4,4,period)
        return self.__inchirieri_repo
