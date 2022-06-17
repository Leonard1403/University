"""
Functie comuna pentru librarie care stocheaza clienti si carti
acest fisier nu mai este folosit deoarece li s-a dat split in carti si clienti
din fisierul repository
"""



from domain.entities import Clienti
# from random import seed
from random import randint

import random, string

class InMemoryRepository:
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
        for obj in self.__list_library:
            if obj.getId() == id:
                return obj
        return None

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

class InFileRepository:
    """
    In clasa Repo vom depozita toate datele pentru clienti si carti
    """
    def __init__(self,filename):
        self.__filename = filename


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
        for obj in self.__list_library:
            if obj.getId() == id:
                return obj
        return None

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


def test_default_clienti():
    client1 = Clienti(1, 'Leonard', '1234567891126')
    client2 = Clienti(2, 'Dorel', '1298567891126')
    client3 = Clienti(3, 'Marin', '6834567891126')
    client4 = Clienti(4, 'Adi Despot', '3334567891126')
    client5 = Clienti(5, 'Marian', '0734567891126')
    client6 = Clienti(6, 'Miruna', '1298479182726')
    memory_test = InMemoryRepository()
    memory_test.store(client1)
    memory_test.store(client2)
    memory_test.store(client3)
    memory_test.store(client4)
    memory_test.store(client5)
    memory_test.store(client6)
    return memory_test


def test_search():
    memory_test = test_default_clienti()
    test = memory_test.search(1)
    assert test.getId() == 1
    assert test.getNume() == 'Leonard'
    assert test.getCNP() == '1234567891126'

def test_update():
    memory_test = test_default_clienti()
    client_update = Clienti(1,'Maria','3334567891126')
    test = memory_test.update_clienti(1,client_update)
    assert test.getId() == 1
    assert test.getNume() == 'Maria'
    assert test.getCNP() == '3334567891126'

def test_delete():
    memory_test = test_default_clienti()
    memory_test.deleteId(2)
    assert memory_test.size() == 5

def TEST():
    test_search()
    test_update()
    test_delete()

TEST()


