from domain.entities import Clienti, Carti, Inchirieri, Perioada
from repository.inchirieri import InchirieriMemoryRepository , InchirieriFileRepository
import unittest

class TestCaseInchirieriRepoInMemory(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = InchirieriMemoryRepository()

        client1 = Clienti(1, 'Leonard', '1234567891126')
        client2 = Clienti(2, 'Dorel', '1298567891126')
        client3 = Clienti(3, 'Marin', '6834567891126')
        client4 = Clienti(4, 'Adi Despot', '3334567891126')
        client5 = Clienti(5, 'Marian', '0734567891126')
        client6 = Clienti(6, 'Miruna', '1298479182726')

        carti1 = Carti(1,
                       'Atomic Habits',
                       "O carte extrem de practica si utila. James Clear "
                       "\nextrage informatiile fundamentale despre formarea obiceiurilor, astfel ca tu sa poti realiza mai "
                       "\nmult concentrandu-te pe mai putine lucruri.",
                       "James Clear")
        # self.__validator.validate_carti(carti1)
        # self.__repo.store(carti1)

        carti2 = Carti(2,
                       'Tata Bogat',
                       "Principalul motiv pentru care oamenii se lupta cu dificultatile "
                       "\nfinanciare este acela ca au trecut prin scoala fara sa invete nimic despre bani. Rezultatul este ca invata sa lucreze pentru bani dar nu invata niciodata sa puna "
                       "\nbanii sa actioneze pentru ei.",
                       "Robert T. Kiyosaki")
        # self.__validator.validate_carti(carti2)
        # self.__repo.store(carti2)

        carti3 = Carti(3,
                       'Arta subtila a nepasarii',
                       'In acest ghid revolutionar, definitoriu pentru o intreaga '
                       '\ngeneratie, autorul ne invata ca, pentru a fi fericiti, trebuie sa renuntam la a fi "pozitivi" mereu si trebuie, '
                       '\nin schimb, sa ne perfectionam in invingerea obstacolelor.',
                       "Mark Manson")
        # self.__validator.validate_carti(carti3)
        # self.__repo.store(carti3)

        start = 2000
        stop = 2010
        period = Perioada(start, stop)
        inchirie1 = Inchirieri(client4,carti1,period)

        start = 2002
        stop = 2008
        period = Perioada(start, stop)
        inchirie2 = Inchirieri(client4,carti2,period)

        start = 2002
        stop = 2009
        period = Perioada(start, stop)
        inchirie3 = Inchirieri(client4,carti3,period)

        start = 2005
        stop = 2007
        period = Perioada(start, stop)
        inchirie4 = Inchirieri(client2,carti1,period)

        start = 2009
        stop = 2021
        period = Perioada(start, stop)
        inchirie5 = Inchirieri(client3,carti2,period)

        self.__repo.store(inchirie1)
        self.__repo.store(inchirie2)
        self.__repo.store(inchirie3)
        self.__repo.store(inchirie4)
        self.__repo.store(inchirie5)

    def test_search_Nume_Titlu(self):
        test = self.__repo.search_Nume_Titlu('Adi Despot','Tata Bogat')
        client = test.getClient()
        nume = client.getNume()
        carte = test.getCarte()
        titlu = carte.getTitlu()
        self.assertEqual(nume,'Adi Despot')
        self.assertEqual(titlu,'Tata Bogat')

    def test_search_Nume_Titlu_rec(self):
        test = self.__repo.search_Nume_Titlu_rec('Adi Despot','Tata Bogat',0)
        client = test.getClient()
        nume = client.getNume()
        carte = test.getCarte()
        titlu = carte.getTitlu()
        self.assertEqual(nume,'Adi Despot')
        self.assertEqual(titlu,'Tata Bogat')
    def test_client_nrinc(self):
        test = self.__repo.client_nrinc()
        self.assertEqual(test[0]['nume'],'Adi Despot')
