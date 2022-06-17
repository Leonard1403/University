import io

from termcolor import colored

from domain.entities import Carti

from domain.entities import Clienti
# from random import seed
from random import randint

import random, string

class CartiMemoryRepository:
    """
    In clasa Repo vom depozita toate datele pentru clienti si carti
    """
    def __init__(self):
        self.__list_library = []



    # def __find_copy_id(self,id):
    #     for obj in self.__list_library:
    #         if obj.getId() == id:
    #             return obj
    #
    # def __find_copy_nume(self,nume):
    #     for obj in self.__list_library:
    #         if obj.getNume() == nume:
    #             return obj
    #
    # def __find_copy_cnp(self,cnp):
    #     for obj in self.__list_library:
    #         if obj.getCNP() == cnp:
    #             return obj
    #
    # def __find_copy_titlu(self,titlu):
    #     for obj in self.__list_library:
    #         if obj.getTitlu() == titlu:
    #             return obj

    def __find_id(self,id):
        """
        Functia find cauta obiectul din lista dupa id
        :param id: id ul pe care il cautam
        :return: obiectul
        """
        for obj in self.__list_library:     # for i = 1 ; i <= n ; i++
            if obj.getId() == id:              # if i == crt:
                return obj                          # return crt
        return None                            #return None

    def deleteId(self,id):
        obj = self.__find_id(id)
        if obj is None:
            raise ValueError("Nu exista acest id in baza de date")

        self.__list_library.remove(obj)
        return obj

    def update_carti(self,id,obiect):
        obj = self.__find_id(id)
        if obj is None:
            raise ValueError("Nu exista acest id in baza de date")

        obj.setId(obiect.getId())
        obj.setTitlu(obiect.getTitlu())
        obj.setDescriere(obiect.getDescriere())
        obj.setAutor(obiect.getAutor())
        return obj

    def __randomword(self,length):
        """
        Functia genereaza un string random de marime length
        :param length: marimea stringului pe care dorim sa-l generam
        :return: returneaza un string de marimea length random
        """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def __randomint(self,marime1,marime2):
        """
        Genereaza o valoare de tip int random intr-un interval de forma [marime1,marime2]
        :param marime1: marimea1 reprezinta partea superioara a intervalului
        :param marime2: reprezinta partea inferioara a intervalului
        :return: functia returneaza o valoare de tip int random
        """
        # seed(1)
        value = randint(marime1,marime2)
        return value

    def __CNP_Generator(self,size=13, chars=string.digits):
        """
        Genereaza un CNP random
        :param size: size reprezinta marimea CNP ului pe care dorim sa-l generam
        :param chars: tipul de CNP pe care dorim sa-l generam(daca dorim sa contina litere si cifre)
        :return: returneaza CNP-ul
        """
        return ''.join(random.choice(chars) for _ in range(size))

    def generate_client(self,id):
        """
        Genereaza un client random
        :param id: id ul pe care dorim sa pozitionam clientul random
        :return: returneaza clientul generat
        """
        marime = self.__randomint(5,10)
        nume = self.__randomword(marime)
        CNP = self.__CNP_Generator()
        client = Clienti(id,nume,CNP)
        return client

    def search(self,id):
        obj = self.__find_id(id)
        if obj is None:
            raise ValueError("Nu exista acest id in baza de date")

        return obj

    def update_clienti(self,id,obiect):
        obj = self.__find_id(id)
        if obj is None:
            raise ValueError("Nu exista acest id in baza de date")

        obj.setId(obiect.getId())
        obj.setNume(obiect.getNume())
        obj.setCNP(obiect.getCNP())
        return obj

    def size(self):
        return len(self.__list_library)

    def store(self,obj):

        # if self.__find_copy_id(obj.getId()) is not None:
        #     raise ValueError("Exista deja un element cu acest id")
        #
        # if self.__find_copy_nume(obj.getNume()) is not None:
        #     raise ValueError("Exista deja un client cu acest nume")
        #
        # if self.__find_copy_cnp(obj.getCNP()) is not None:
        #     raise ValueError("Exista deja un client cu acest nume")

        # if self.__find_copy_titlu(obj.getTitlu) is not None:
        #     raise ValueError("Exista deja o carte cu acest titlu")

        if self.__find_id(obj.getId()) is not None:
            raise ValueError("Exista deja un element cu acest id")
        self.__list_library.append(obj)

    def get_all(self):
        return self.__list_library

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

class CartiFileRepository:
    """
    In clasa Repo vom depozita toate datele pentru clienti si carti
    """

    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        # id, titlu, descriere, autor
        try:
            f = open(self.__filename)
        except ValueError as ve:
            print(colored(ve, 'red'))

        all_carti = []
        file = f.read()
        lines = file.splitlines()
        n = len(lines)
        el = 0
        for el in range(0,n,+4):
            carte_id = lines[el].strip()
            carte_titlu = lines[el+1].strip()
            carte_descriere = lines[el+2].strip()
            carte_autor = lines[el+3].strip()
            carte_id = int(carte_id)
            carti = Carti(carte_id,carte_titlu,carte_descriere,carte_autor)
            all_carti.append(carti)
        # print(lines)
        # for line in lines:
        #     carte_id, carte_titlu, carte_descriere, carte_autor = [token.strip() for token in line.splitlines()]
        #     carte_id = int(carte_id)
        #     carti = Carti(carte_id, carte_titlu, carte_descriere, carte_autor)
        #     all_carti.append(carti)
        f.close()
        return all_carti

    def __save_to_file(self, all_carti):
        # id, titlu, descriere, autor
        with open(self.__filename, 'w') as f:
            for carte in all_carti:
                carte_string = str(carte.getId()) + '\n' + str(carte.getTitlu()) + '\n' + str(carte.getDescriere()) + '\n' + str(carte.getAutor()) + '\n'
                f.write(carte_string)

    def __find_id(self, id):
        """
        Functia find cauta obiectul din lista dupa id
        :param id: id ul pe care il cautam
        :return: obiectul
        """
        all_carti = self.__load_from_file()
        for obj in all_carti:
            if obj.getId() == id:
                return obj
        return None

    def deleteId(self, id):
        obj = self.__find_id(id)
        all_carti = self.__load_from_file()
        if obj is None:
            raise ValueError("Nu exista acest id in baza de date")

        all_carti.remove(obj)
        self.__save_to_file(all_carti)
        return obj

    def update_carti(self, id, obiect):
        obj = self.__find_id(id)
        if obj is None:
            raise ValueError("Nu exista acest id in baza de date")

        obj.setId(obiect.getId())
        obj.setTitlu(obiect.getTitlu())
        obj.setDescriere(obiect.getDescriere())
        obj.setAutor(obiect.getAutor())
        return obj

    def __randomword(self, length):
        """
        Functia genereaza un string random de marime length
        :param length: marimea stringului pe care dorim sa-l generam
        :return: returneaza un string de marimea length random
        """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def __randomint(self, marime1, marime2):
        """
        Genereaza o valoare de tip int random intr-un interval de forma [marime1,marime2]
        :param marime1: marimea1 reprezinta partea superioara a intervalului
        :param marime2: reprezinta partea inferioara a intervalului
        :return: functia returneaza o valoare de tip int random
        """
        # seed(1)
        value = randint(marime1, marime2)
        return value

    def __CNP_Generator(self, size=13, chars=string.digits):
        """
        Genereaza un CNP random
        :param size: size reprezinta marimea CNP ului pe care dorim sa-l generam
        :param chars: tipul de CNP pe care dorim sa-l generam(daca dorim sa contina litere si cifre)
        :return: returneaza CNP-ul
        """
        return ''.join(random.choice(chars) for _ in range(size))

    def generate_client(self, id):
        """
        Genereaza un client random
        :param id: id ul pe care dorim sa pozitionam clientul random
        :return: returneaza clientul generat
        """
        marime = self.__randomint(5, 10)
        nume = self.__randomword(marime)
        CNP = self.__CNP_Generator()
        client = Clienti(id, nume, CNP)
        return client

    def search(self, id):
        obj = self.__find_id(id)
        if obj is None:
            raise ValueError("Nu exista acest id in baza de date")

        return obj

    def update_clienti(self, id, obiect):
        obj = self.__find_id(id)
        if obj is None:
            raise ValueError("Nu exista acest id in baza de date")

        obj.setId(obiect.getId())
        obj.setNume(obiect.getNume())
        obj.setCNP(obiect.getCNP())
        return obj

    def size(self):
        return len(self.__load_from_file())

    def store(self, obj):

        # if self.__find_copy_id(obj.getId()) is not None:
        #     raise ValueError("Exista deja un element cu acest id")
        #
        # if self.__find_copy_nume(obj.getNume()) is not None:
        #     raise ValueError("Exista deja un client cu acest nume")
        #
        # if self.__find_copy_cnp(obj.getCNP()) is not None:
        #     raise ValueError("Exista deja un client cu acest nume")

        # if self.__find_copy_titlu(obj.getTitlu) is not None:
        #     raise ValueError("Exista deja o carte cu acest titlu")

        if self.__find_id(obj.getId()) is not None:
            raise ValueError("Exista deja un element cu acest id")
        all_clienti = self.__load_from_file()
        all_clienti.append(obj)
        self.__save_to_file(all_clienti)

    def get_all(self):
        return self.__load_from_file()
    def delete_all(self):
        self.__save_to_file([])
