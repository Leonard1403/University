from termcolor import colored

from domain.entities import Inchirieri
from domain.entities import Perioada
from domain.entities import Clienti
from domain.entities import Carti
from termcolor import colored
from repository.carti import CartiFileRepository
from repository.clienti import ClientiFileRepository
from domain.entities import Inchirieri

class InchirieriMemoryRepository:
    def __init__(self):
        self.__list_inchiriere = []

    def get_all(self):
        """
        Functie care obtine toate elementele din lista
        :return: returneaza elementele din lista
        """
        return self.__list_inchiriere

    def search_Nume_Titlu(self,nume,titlu):
        """
        Functie care cauta un element dupa numele si titlul dat
        :param nume: Numele clientului
        :param titlu: Titlul cartii
        :return: returneaza obiectul daca este gasit in lista
        """
        for obj in self.__list_inchiriere:
            client = obj.getClient()
            nume_din_lista = client.getNume()

            carte = obj.getCarte()
            titlu_din_lista = carte.getTitlu()

            if nume_din_lista == nume and titlu_din_lista == titlu:
                return obj
        return None

    def search_Nume_Titlu_rec(self,nume,titlu,poz):
        """
------------------------------------------------------------------------------------------------------------------------
                Functie care cauta un element dupa numele si titlul dat
                :param nume: Numele clientului
                :param titlu: Titlul cartii
                :return: returneaza obiectul daca este gasit in lista
                """
        if poz < len(self.__list_inchiriere):
            obj = self.__list_inchiriere[poz]

            client = obj.getClient()
            nume_din_lista = client.getNume()

            carte = obj.getCarte()
            titlu_din_lista = carte.getTitlu()

            if nume_din_lista == nume and titlu_din_lista == titlu:
                return obj
            else:
                poz = poz + 1
                return self.search_Nume_Titlu_rec(nume,titlu,poz)
        else:
            return None

    def store(self,inchiriere):
        """
        Functie de stocare a elementelor
        :param inchiriere: tipul de data care dorim sa fie stocat
        :return: returneaza clientul care a inchiriat cartea
        """
        client = inchiriere.getClient()
        carte = inchiriere.getCarte()
        nume = client.getNume()
        titlu = carte.getTitlu()
        # obj = self.search_Nume_Titlu(nume,titlu)
        poz = 0
        obj = self.search_Nume_Titlu_rec(nume,titlu,poz)
        if obj is None:
            return self.__list_inchiriere.append(inchiriere)
        else:
            raise ValueError("Exista deja chirie la aceasta carte cu acest client")

    def deleteInchiriere(self,nume,titlu):
        # obj = self.search_Nume_Titlu(nume,titlu)
        poz = 0
        obj = self.search_Nume_Titlu_rec(self,nume,titlu,poz)
        if obj is None:
            raise ValueError("Nu exista clientul sau cartea")
        self.__list_inchiriere.remove(obj)
        return obj

    def best_inchiriat(self):
        """
        Returneaza lista cu titlul cartilor si numarul de clienti care au inchiriat
        cartea repectiva
        :return:
        """
        lista_carti_inchiriate = [0]*1000
        id_maxim = 0
        nr_inchirieri = 0
        ls_inchiriate = self.get_all()
        for el in ls_inchiriate:
            carti = el.getCarte()
            id = int(carti.getId())
            if id > id_maxim:
                id_maxim = id
            lista_carti_inchiriate[id] = lista_carti_inchiriate[id] + 1
            if lista_carti_inchiriate[id] > nr_inchirieri:
                nr_inchirieri = lista_carti_inchiriate[id]
        return lista_carti_inchiriate , id_maxim , nr_inchirieri

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
#-----------------------------------------------------------------------------------------------------------------------

    def sorted_by_cr(self,lista):
        n = len(lista)
        for el1 in range(0,n,+1):
            for el2 in range(0,n,+1):
                if lista[el1]['cr'] > lista[el2]['cr']:
                    aux = lista[el1]
                    lista[el1] = lista[el2]
                    lista[el2] = aux
        return lista

    def nr_apar(self,nume):
        brr = 0
        ls_inchiriate = self.get_all()
        for obj in ls_inchiriate:
            client = obj.getClient()
            nume1 = client.getNume()
            if nume == nume1:
                brr = brr + 1
        return brr

    def nr_apar_rec(self,ls_inchiriate,nume,poz):
        """
        ----------------------------------------------------------------------------------------------------------------
        :param ls_inchiriate:
        :param nume:
        :param poz:
        :return:
        """
        if poz < len(ls_inchiriate):
            client = ls_inchiriate[poz].getClient()
            nume1 = client.getNume()
            if nume == nume1:
                return 1 + self.nr_apar_rec(ls_inchiriate,nume,poz+1)
            else:
                return self.nr_apar_rec(ls_inchiriate, nume, poz + 1)
        else:
            return 0

    def create_cv(self,nume,cr):
        """
        Functi care creeaza dictionarul
        :param nume:
        :param cr:
        :return:
        """
        return {'nume': nume , 'cr': cr}

    def exist(self,lista,nume):
        """
        Functie care verifica daca intr-o lista de dictionar exista
        un element cu numele cautat
        :param lista:
        :param nume:
        :return:
        """
        for el in lista:
            if el['nume'] == nume:
                return True
        return False

    def client_nrinc(self):
        """
        Functi care returneaza in functie de numarul de carti inchiriate dupa client
        :return:
        """
        ls_da = []
        n = 0
        ls_inchiriate = self.get_all()
        for obj in ls_inchiriate:
            client = obj.getClient()
            nume = client.getNume()
            if self.exist(ls_da,nume) == False:
                # ls_da.append(self.create_cv(nume,self.nr_apar(nume)))
                # print("Intrat: " + str(self.nr_apar_rec(self.get_all(),nume,0)))
                ls_da.append(self.create_cv(nume,self.nr_apar_rec(self.get_all(),nume,0)))
        return ls_da
#-----------------------------------------------------------------------------------------------------------------------
    def nr_apar_autor(self,nume):
        """
        Functie care determina numarul de aparitii intr-o lista de inchirieri petru un autor
        :param nume:
        :return:
        """
        brr = 0
        ls_inchiriate = self.get_all()
        for obj in ls_inchiriate:
            carte = obj.getCarte()
            autor = carte.getAutor()
            if nume == autor:
                brr = brr + 1
        return brr

    def autor_nrinc(self):
        """
        Functia calculeaza numarul de inchirieri pe care il are un autor din lista
        :return: returneaza lista de autori cu numarul de inchirieri sub forma de dictionar
        """
        ls_da = []
        n = 0
        ls_inchiriate = self.get_all()
        for obj in ls_inchiriate:
            carte = obj.getCarte()
            autor = carte.getAutor()
            if self.exist(ls_da,autor) == False:
                ls_da.append(self.create_cv(autor,self.nr_apar_autor(autor)))
        return ls_da

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

class InchirieriFileRepository:
    def __init__(self, filename1,filename2,filename3):
        self.__filename1 = filename1
        self.__filename2 = filename2 # clienti
        self.__filename3 = filename3 # carti

    def __load_from_file(self):

        try:
            f = open(self.__filename1, 'r')
        except ValueError as ve:
            print(colored(ve, 'red'))

        all_inchirieri = []
        lines = f.readlines()
        # client,carte,perioada
        for line in lines:
            client_id, carte_id , p_start , p_stop = [token.strip() for token in line.split(';')]
            client_id = int(client_id)
            carte_id = int(carte_id)
            p_start = int(p_start)
            p_stop = int(p_stop)
            # print(str(client_id),str(carte_id),str(p_start),str(p_stop))
            clienti_repo = ClientiFileRepository(self.__filename2)
            carti_repo =   CartiFileRepository(self.__filename3)
            clienti = clienti_repo.search(client_id)
            carti = carti_repo.search(carte_id)
            perioada = Perioada(p_start,p_stop)
            chirie = Inchirieri(clienti,carti,perioada)
            all_inchirieri.append(chirie)

        f.close()
        return all_inchirieri

    def __save_to_file(self, all_inchirieri):
        with open(self.__filename1, 'w') as f:
            for chirie in all_inchirieri:
                # def getClient(self):
                #     return self.__client
                #
                # def getCarte(self):
                #     return self.__carte
                #
                # def getPerioada(self):
                #     return self.__perioada

                # getStart() getstop()
                clienti = chirie.getClient()
                carti = chirie.getCarte()
                perioada = chirie.getPerioada()
                chirie_string = str(clienti.getId()) + ';' + str(carti.getId()) + ';' + str(perioada.getStart()) + ';' + str(perioada.getStop()) + '\n'
                f.write(chirie_string)

    def get_all(self):
        return self.__load_from_file()

    def delete_all(self):
        self.__save_to_file([])

    def search_Nume_Titlu(self,nume,titlu):
        """
        Functie care cauta un element dupa numele si titlul dat
        :param nume: Numele clientului
        :param titlu: Titlul cartii
        :return: returneaza obiectul daca este gasit in lista
        """
        for obj in self.__list_inchiriere:
            client = obj.getClient()
            nume_din_lista = client.getNume()

            carte = obj.getCarte()
            titlu_din_lista = carte.getTitlu()

            if nume_din_lista == nume and titlu_din_lista == titlu:
                return obj
        return None

    def store(self,inchiriere):
        """
        Functie de stocare a elementelor
        :param inchiriere: tipul de data care dorim sa fie stocat
        :return: returneaza clientul care a inchiriat cartea
        """
        all_inchirieri = self.__load_from_file()
        all_inchirieri.append(inchiriere)
        self.__save_to_file(all_inchirieri)
        # client = inchiriere.getClient()
        # carte = inchiriere.getCarte()
        # nume = client.getNume()
        # titlu = carte.getTitlu()
        # obj = self.search_Nume_Titlu(nume,titlu)
        # if obj is None:
        #     return self.__list_inchiriere.append(inchiriere)
        # else:
        #     raise ValueError("Exista deja chirie la aceasta carte cu acest client")

    def deleteInchiriere(self,nume,titlu):
        obj = self.search_Nume_Titlu(nume,titlu)
        if obj is None:
            raise ValueError("Nu exista clientul sau cartea")
        self.__list_inchiriere.remove(obj)
        return obj

    def best_inchiriat(self):
        """
        Returneaza lista cu titlul cartilor si numarul de clienti care au inchiriat
        cartea repectiva
        :return:
        """
        lista_carti_inchiriate = [0]*1000
        id_maxim = 0
        nr_inchirieri = 0
        ls_inchiriate = self.get_all()
        for el in ls_inchiriate:
            carti = el.getCarte()
            id = int(carti.getId())
            if id > id_maxim:
                id_maxim = id
            lista_carti_inchiriate[id] = lista_carti_inchiriate[id] + 1
            if lista_carti_inchiriate[id] > nr_inchirieri:
                nr_inchirieri = lista_carti_inchiriate[id]
        return lista_carti_inchiriate , id_maxim , nr_inchirieri

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
#-----------------------------------------------------------------------------------------------------------------------

    def sorted_by_cr(self,lista):
        n = len(lista)
        for el1 in range(0,n,+1):
            for el2 in range(0,n,+1):
                if lista[el1]['cr'] > lista[el2]['cr']:
                    aux = lista[el1]
                    lista[el1] = lista[el2]
                    lista[el2] = aux
        return lista

    def nr_apar(self,nume):
        brr = 0
        ls_inchiriate = self.get_all()
        for obj in ls_inchiriate:
            client = obj.getClient()
            nume1 = client.getNume()
            if nume == nume1:
                brr = brr + 1
        return brr

    def create_cv(self,nume,cr):
        """
        Functi care creeaza dictionarul
        :param nume:
        :param cr:
        :return:
        """
        return {'nume': nume , 'cr': cr}

    def exist(self,lista,nume):
        """
        Functie care verifica daca intr-o lista de dictionar exista
        un element cu numele cautat
        :param lista:
        :param nume:
        :return:
        """
        for el in lista:
            if el['nume'] == nume:
                return True
        return False

    def client_nrinc(self):
        """
        Functi care returneaza in functie de numarul de carti inchiriate dupa client
        :return:
        """
        ls_da = []
        n = 0
        ls_inchiriate = self.get_all()
        for obj in ls_inchiriate:
            client = obj.getClient()
            nume = client.getNume()
            if self.exist(ls_da,nume) == False:
                ls_da.append(self.create_cv(nume,self.nr_apar(nume)))
        return ls_da
#-----------------------------------------------------------------------------------------------------------------------
    def nr_apar_autor(self,nume):
        """
        Functie care determina numarul de aparitii intr-o lista de inchirieri petru un autor
        :param nume:
        :return:
        """
        brr = 0
        ls_inchiriate = self.get_all()
        for obj in ls_inchiriate:
            carte = obj.getCarte()
            autor = carte.getAutor()
            if nume == autor:
                brr = brr + 1
        return brr

    def autor_nrinc(self):
        """
        Functia calculeaza numarul de inchirieri pe care il are un autor din lista
        :return: returneaza lista de autori cu numarul de inchirieri sub forma de dictionar
        """
        ls_da = []
        n = 0
        ls_inchiriate = self.get_all()
        for obj in ls_inchiriate:
            carte = obj.getCarte()
            autor = carte.getAutor()
            if self.exist(ls_da,autor) == False:
                ls_da.append(self.create_cv(autor,self.nr_apar_autor(autor)))
        return ls_da
