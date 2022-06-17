from termcolor import colored

# ------------------------------------CARTI-----------------------------------
class Carti:
    """
    Clasa carti retine detalii despre carti
    """
    def __init__(self, id, titlu, descriere, autor):
        """
        Initializarea
        :param id: trebuie sa fie de tip int si reprezinta o variabila esentiale
        dupa care se vor apela niste functii
        :param titlu:
        :param descriere:
        :param autor:
        """
        self.__id = id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor

# -------------------------------------GET------------------------------------
    def getId(self):
        return self.__id

    def getTitlu(self):
        return self.__titlu

    def getDescriere(self):
        return self.__descriere

    def getAutor(self):
        return self.__autor

# -------------------------------------SET------------------------------------
    def setId(self, value):
        self.__id = value

    def setTitlu(self, value):
        self.__titlu = value

    def setDescriere(self, value):
        self.__descriere = value

    def setAutor(self, value):
        self.__autor = value

# ------------------------------------FUN-------------------------------------
    def __eq__(self, other):
        if self.__id == other.getId():
            return True
        return False

    def __le__(self, other):
        if self.__id <= other.getId():
            return True
        return False

    def __lt__(self,other):
        if self.__id < other.getId():
            return True
        return False

    def __gt__(self,other):
        if self.__id > other.getId():
            return True
        return False

    def __ge__(self,other):
        if self.__id >= other.getId():
            return True
        return False

    def __ne__(self,other):
        if self.__id != other.getId():
            return True
        return False

    def __str__(self):
        return "ID: " + colored(str(self.__id),'cyan') + " | Titlu: " + \
               colored(self.__titlu,'cyan') + " | Descriere: " + colored(self.__descriere,'green') + " | Autor: " + \
               colored(self.__autor,'cyan')




# ------------------------------------CLIENTI---------------------------------
class Clienti:
    """
    Clasa Clienti retine detalii esentiale pentru clienti
    """
    def __init__(self, id, nume, CNP):
        self.__id = id
        self.__nume = nume
        self.__CNP = CNP

# -------------------------------------GET------------------------------------
    def getId(self):
        return self.__id

    def getNume(self):
        return self.__nume

    def getCNP(self):
        return self.__CNP

# -------------------------------------SET------------------------------------
    def setId(self, value):
        self.__id = value

    def setNume(self, value):
        self.__nume = value

    def setCNP(self, value):
        self.__CNP = value
# ------------------------------------FUN-------------------------------------
    def __eq__(self, other):
        if self.__id == other.getId():
            return True
        return False

    def __str__(self):
        return "Id: " + colored(str(self.__id),'cyan') + " | Nume : " + colored(self.__nume,'cyan') + " | Cnp: " + colored(str(self.__CNP),'cyan')

class Perioada:
    def __init__(self,start,stop):
        self.__start = start
        self.__stop = stop

    def getStart(self):
        return self.__start

    def getStop(self):
        return self.__stop

    def setStart(self,value):
        self.__start = value

    def setStop(self,value):
        self.__stop = value

class Inchirieri:
    def __init__(self,client,carte,perioada):
        self.__client = client
        self.__carte = carte
        self.__perioada = perioada

    def getClient(self):
        return self.__client

    def getCarte(self):
        return self.__carte

    def getPerioada(self):
        return self.__perioada

    def setClient(self,value):
        self.__client = value

    def setCarte(self,value):
        self.__carte = value

    def setPerioada(self,value):
        self.__perioada = value

    def __eq__(self,other):
        if self.__client == other.__client and self.__carte == other.__carte:
            return True
        return False

    def __str__(self):
        return 'Client:[' + colored(str(self.__client.getNume()),'cyan') + ']  ' + \
               'Carte:[' + colored(str(self.__carte.getTitlu()),'cyan') + ']  ' + \
               'Inchiriere:[' + 'inceput: ' + colored(str(self.__perioada.getStart()),'cyan') + ' | sfarsit: ' + colored(str(self.__perioada.getStop()),'cyan') + ']'



# carte1 = Carti('0100010',"Scufita Rosie" , "A fost odata o scufita" , "Ionn Creanga")
# print(carte1)
# client1 = Clienti('1012','Leonard','500120201000')
# print(client1)

def test_create_clienti():
    carte1 = Carti(1209552, "Punguta cu doi bani", "Descriere" , "Ion Creanga")
    client1 = Clienti(1918 , "Mihai" , '40040140141240')
    assert (carte1.getId() == 1209552)
    assert (carte1.getTitlu() == "Punguta cu doi bani")
    assert (carte1.getDescriere() == "Descriere")
    assert (carte1.getAutor() == "Ion Creanga")

    assert (client1.getId() == 1918)
    assert (client1.getNume() == "Mihai")
    assert (client1.getCNP() == '40040140141240')

def test_equals_carti_and_clients():
    carte1 = Carti('0100010', "Scufita Rosie", "A fost odata o scufita", "Ion Creanga")
    carte2 = Carti('0100010', "Morometii" , "Aceasta este descrierea cartii" , "Marin Preda")
    assert (carte1==carte2)

    carte3 = Carti('10101011' , "Mein Kempf" , "Istoria Germaniei" , "Hitler")
    assert (carte1 != carte3)

    client1 = Clienti(2002,"Leonard"  , '5001202010009')
    client2 = Clienti(2002,"Vlad"     , '5002020001008')
    client3 = Clienti(2010,"Ionela"   , '6060060606007')

    assert (client1==client2)
    assert (client1!=client3)

def TEST():
    test_create_clienti()
    test_equals_carti_and_clients()

TEST()