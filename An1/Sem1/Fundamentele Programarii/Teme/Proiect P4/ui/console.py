# from service.clienti_service import *
from service.carti_service import CartiService
# from service.inchirieri import InchirieriService

from repository.Sort import sort

from domain.entities import Perioada

from termcolor import colored

def num_there(s):
    return any(i.isdigit() for i in s)

class Console:
    """
    Clasa consola controleaza aplicatia in forma citire/scriere
    sub forma de Aplicatie in consola
    """
    def __init__(self,carti,clienti,inchirieri):

        self.__carti = carti
        self.__clienti = clienti
        self.__inchirieri = inchirieri

    def __add_carti(self):
        try:
            id = int(input("Introduceti ID: "))

        except ValueError:
            print(colored("ID-ul trebuie sa fie numar", 'red'))
            return
        titlu = input("Introduceti titlu: ")
        descriere = input("Introduceti descriere: ")
        autor = input("Introduceti autor: ")
        try:
            added_carti = self.__carti.add_carti(id,titlu,descriere,autor)
            print("Cartea: " + colored(titlu,'cyan') + ' cu titlul: ' + colored(autor,'cyan') + ' a fost adaugata cu succes')
        except ValueError as ve:
            print(colored(str(ve),'red'))

    def __add_clienti(self):
        errors = []

        try:
            id = int(input("Introduceti ID: "))
        except ValueError:
            print(colored("ID-ul trebuie sa fie numar",'red'))
            return
        nume = input("Introduceti nume: ")
        CNP = input("Introduceti CNP: ")

        try:
            added_clienti = self.__clienti.add_clienti(id,nume,CNP)
            print("Clientul: " + colored(nume,'cyan') + " a fost adaugat cu succes")
        except ValueError as ve:
            print(colored(ve,'red'))

    def __add_inchiriere(self):
        start = 0
        stop = 0
        try:
            start = int(input("Perioada de inceput: "))
            stop = int(input("Perioada de returnare:"))
        except ValueError:
            print(colored("Valoarea trebuie sa fie de tip int",'red'))
            return
        period = Perioada(start,stop)

        try:
            id_client = int(input("Id-ul clinetului: "))
            id_carte = int(input("Id-ul cartii: "))
        except ValueError:
            print(colored("Id invalid",'red'))
            return
        try:
            added_inchiriere = self.__inchirieri.add_inchirieri(id_client, id_carte , period)
            print(added_inchiriere)
        except ValueError as ve:
            print(colored(ve,'red'))

    def __add_random_client(self):
        repeta = int(input("De cate ori doriti sa se execute?: "))
        while repeta != 0:
            try:
                id = int(input("Introduceti ID-ul pe care doriti sa se afle clientul generat: "))
            except ValueError:
                print(colored("ID-ul trebuie sa fie numar", 'red'))
                return
            client = self.__clienti.gen_random_clienti(id)
            id = client.getId()
            nume = client.getNume()
            CNP = client.getCNP()
            try:
                added_clienti = self.__clienti.add_clienti(id, nume, CNP)
                print("Clientul: " + colored(nume, 'cyan') + " a fost adaugat cu succes")
            except ValueError as ve:
                print(colored(ve, 'red'))
            repeta = repeta - 1


    def __show_carti(self):
        ls_carti = self.__carti.show_carti()
        if len(ls_carti) == 0:
            print(colored("Nu sunt elemente",'red'))
        else:
            for carti in ls_carti:
                print(carti)

    def __show_clienti(self):
        ls_clienti = self.__clienti.show_clienti()
        if len(ls_clienti) == 0:
            print(colored("Nu sunt elemente",'red'))
        else:
            for clienti in ls_clienti:
                print(clienti)

    def __show_inchiriere(self):
        ls_chirie = self.__inchirieri.show_inchirieri()
        if len(ls_chirie) == 0:
            print(colored("Nu sunt elemente",'red'))
        else:
            for chirie in ls_chirie:
                print(chirie)

    def __delete_carti(self):
        try:
            id = int(input("Introduceti ID-ul care doriti sa fie sters: "))
        except ValueError:
            print(colored("ID-ul trebuie sa fie numar",'red'))
            return
        try:
            elem = self.__carti.delete_carti_id(id)
            print("Cartea: " + colored(elem.getTitlu(),'cyan') + " s-a sters cu succes")
        except ValueError as ve:
            print(colored(ve, 'red'))

    def __delete_clienti(self):
        try:
            id = int(input("Introduceti ID-ul care doriti sa fie sters: "))
        except ValueError:
            print(colored("ID-ul trebuie sa fie numar", 'red'))
            return
        try:
            elem = self.__clienti.delete_clienti_id(id)
            print("Clientul: " + colored(elem.getNume(),'cyan')+" s-a sters cu succes")
        except ValueError as ve:
            print(colored(ve,'red'))

    def __delete_inchiriere(self):
        nume = input("Introduceti un nume: ")
        titlu = input("Introduceti un titlu: ")
        try:
            inchiriere = self.__inchirieri.delete_inchiriere(nume,titlu)
            print(inchiriere,end = "")
            print(colored(" s-a sters cu succes",'red'))
        except ValueError as ve:
            print(colored(ve,'red'))

    def __update_clienti(self):
        try:
            id = int(input("Introduceti ID: "))
        except ValueError:
            print(colored("ID-ul trebuie sa fie numar", 'red'))
            return
        nume = input("Introduceti nume: ")
        CNP = input("Introduceti CNP: ")

        try:
            update_client = self.__clienti.update_clienti_id(id, nume, CNP)
            print("Clientul: " + colored(nume, 'cyan') + " a fost modificat cu succes")
        except ValueError as ve:
            print(colored(ve, 'red'))

    def __update_carti(self):
        try:
            id = int(input("Introduceti ID: "))

        except ValueError:
            print(colored("ID-ul trebuie sa fie numar", 'red'))
            return
        titlu = input("Introduceti titlu: ")
        descriere = input("Introduceti descriere: ")
        autor = input("Introduceti autor: ")
        try:
            added_carti = self.__carti.update_carti_id(id, titlu, descriere, autor)
            print("Cartea: " + colored(titlu, 'cyan') + ' cu titlul: ' + colored(autor,
                                                                                 'cyan') + ' a fost modificat cu succes')
        except ValueError as ve:
            print(colored(str(ve), 'red'))
            return
        obiect = self.__carti.search_carti_id(id)
        print(obiect)

    def __search_carti(self):
        try:
            id = int(input("Introduceti ID: "))

        except ValueError:
            print(colored("ID-ul trebuie sa fie numar", 'red'))
            return
        try:
            obiect = self.__carti.search_carti_id(id)
            print(obiect)
        except ValueError as ve:
            print(colored(ve,'red'))

    def __search_clienti(self):
        try:
            id = int(input("Introduceti ID: "))

        except ValueError:
            print(colored("ID-ul trebuie sa fie numar", 'red'))
            return
        try:
            obiect = self.__clienti.search_clienti_id(id)
            print(obiect)
        except ValueError as ve:
            print(colored(ve,'red'))

    def __best_inchiriere(self):
        """
        Functia afiseaza in ordine crescatoare cele mai inchiriate carti
        :return:
        """
        lista , id_maxim , nr_inchirieri = self.__inchirieri.best_inchiriat()
        inchiriate_most = []
        for el in range(1,id_maxim+2,+1):
            if lista[el]!=0:
                obj = self.__carti.search_carti_id(el)
                print("Cartea: " + colored(obj.getTitlu(),'cyan') + " a fost inchiriata de: " + colored(str(lista[el]),'cyan') + " ori")
                if lista[el] == nr_inchirieri:
                    inchiriate_most.append(obj)
        print(colored("Cele mai inchiriate carti sunt: ",'green'), end = "")
        for el in inchiriate_most:
            print(colored(el.getTitlu(),'cyan'),end = " | ")
        print()

    def __sorted_nume(self):
        # lista_nume , id_maxim = self.__inchirieri.lista_nume()
        lista1 = self.__inchirieri.get_all()
        lista2 = self.__inchirieri.algh_sort_nume(lista1)
        for el in lista2:
            print(el)

    def __sorted_autor(self):
        """
        Top 3 cei mai inchiriati autori
        :return: NULL
        """
        lista1 = self.__inchirieri.autor_nrinc()
        lista_noua = self.__inchirieri.sorted_by_cr(lista1)
        n = len(lista_noua)
        for el in range(0,3,+1):
            print("Numele autor: " + colored(lista_noua[el]['nume'],'cyan') + " | Nr. de carti imprumutate: " + colored(str(lista_noua[el]['cr']),'cyan'))

    def __sorted_inchiriate(self):
        """
        Cartile inchiriate sortate dupa numarul de carti inchiriate de client
        :return:
        """
        lista = self.__inchirieri.client_nrinc()
        # print(lista[0] + " " + lista[1])
        lista_noua = self.__inchirieri.sorted_by_cr(lista)
        for el in lista_noua:
            print("Numele: " + colored(el['nume'],'cyan') + " | Nr. de carti imprumutate: " + colored(str(el['cr']),'cyan'))

    def __sorted_inchiriate_20(self):
        """
        Cartile inchiriate ortate dupa numarul e carti inchiriat e client
        si care afiseaza 20% din totalul de inchirieri
        :return:
        """
        lista = self.__inchirieri.client_nrinc()
        lista_noua = self.__inchirieri.sorted_by_cr(lista)
        n = len(lista_noua)
        n = int(n*(20/100))
        for el in range(0,n,+1):
            print("Numele: " + colored(lista_noua[el]['nume'], 'cyan') + " | Nr. de carti imprumutate: " + colored(str(lista_noua[el]['cr']),
                                                                                                       'cyan'))
    def __sortare(self):
        lista = self.__carti.show_carti()
        # lista = self.__carti.sorted(lista,reversed=True)
        # lista = self.__carti.sorted(lista,lambda x : x.getTitlu())
        for obj in lista:
            print(obj)
    def show_ui(self):
        self.__clienti.Default()
        self.__carti.Default()
        self.__inchirieri.Default()
        while True:
            print(colored("Comenzi disponibile",'cyan') + ": add_carti , add_clienti, add_inchiriere, \n"
                  "show_carti, show_clienti, show_inchiriere, delete_carti,"
                  "\ndelete_clienti, delete_inchiriere, update_carti, update_clienti, search_clienti, search_carti,\n"
                  "random_clienti, best_inchiriere, sorted_nume, sorted_inchiriate, sorted_autor, "
                  "\nsorted_inchiriate_20, sortare, exit")
            cmd = input("Comanda: ")
            cmd = cmd.lower().strip()
            if cmd == "add_carti":
                self.__add_carti()
            elif cmd == "add_clienti":
                self.__add_clienti()
            elif cmd == "add_inchiriere":
                self.__add_inchiriere()
            elif cmd == "show_carti":
                self.__show_carti()
            elif cmd == "show_clienti":
                self.__show_clienti()
            elif cmd == "show_inchiriere":
                self.__show_inchiriere()
            elif cmd == "delete_carti":
                self.__delete_carti()
            elif cmd == "delete_clienti":
                self.__delete_clienti()
            elif cmd == "delete_inchiriere":
                self.__delete_inchiriere()
            elif cmd == "update_carti":
                self.__update_carti()
            elif cmd == "update_clienti":
                self.__update_clienti()
            elif cmd == "search_clienti":
                self.__search_clienti()
            elif cmd == "search_carti":
                self.__search_carti()
            elif cmd == "random_clienti":
                self.__add_random_client()
            elif cmd == "best_inchiriere":
                self.__best_inchiriere()
            elif cmd == "sorted_nume":
                self.__sorted_nume()
            elif cmd == "sorted_inchiriate":
                self.__sorted_inchiriate()
            elif cmd == "sorted_autor":
                self.__sorted_autor()
            elif cmd == "sorted_inchiriate_20":
                self.__sorted_inchiriate_20()
            elif cmd == "sortare":
                self.__sortare()
            elif cmd == "exit":
                return
            else:
                print("Comanda invalida")