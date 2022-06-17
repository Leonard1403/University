import unittest
from domain.entities import Carti, Clienti, Inchirieri, Perioada
from domain.validators import InchiriereValidator, CartiValidator, ClientiValidator
from repository.inchirieri import InchirieriFileRepository, InchirieriMemoryRepository
from repository.clienti import ClientiMemoryRepository
from repository.carti import CartiMemoryRepository
from service.carti_service import CartiService
from service.clienti_service import ClientiService

from service.inchirieri import InchirieriService

class TestCaseClientiService(unittest.TestCase):
    def setUp(self) -> None:
        carti_repo = CartiMemoryRepository()
        clienti_repo = ClientiMemoryRepository()

        inchirieri_repo = InchirieriMemoryRepository()
        inchirieri_validator = InchiriereValidator()
        # def __init__(self, inchirieri_repo , client_repo , carte_repo , inchirieri_vali):

        self.__srv = InchirieriService(inchirieri_repo,clienti_repo,carti_repo,inchirieri_validator)

    def test_add_inchirieri(self):
        inchirieri = InchirieriMemoryRepository()
        client = ClientiMemoryRepository()
        carte = CartiMemoryRepository()
        validator = InchiriereValidator()

        client1 = Clienti(1, 'Leonard', '1234567891126')
        client2 = Clienti(2, 'Dorel', '1298567891126')
        client3 = Clienti(3, 'Marin', '6834567891126')
        client4 = Clienti(4, 'Adi Despot', '3334567891126')
        client5 = Clienti(5, 'Marian', '0734567891126')
        client6 = Clienti(6, 'Miruna', '1298479182726')

        client.store(client1)
        client.store(client2)
        client.store(client3)
        client.store(client4)
        client.store(client5)
        client.store(client6)

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

        carti4 = Carti(4,
                       'Pas cu pas',
                       'Am adunat in aceasta carte momente din viata publica, incercand sa refac, din ceea ce a selectat memoria, '
                       '\ntraseul profesional care m-a adus de la catedra de fizica la ipostaza de candidat pentru presedintie. '
                       '\nAm inclus in ea si lucruri personale, dar nu am facut o neaparat pentru a raspunde curiozitatii celorlalti.',
                       "Klaus Iohannis")
        carte.store(carti1)
        carte.store(carti2)
        carte.store(carti3)
        carte.store(carti4)


        # def __init__(self, inchirieri_repo , client_repo , carte_repo , inchirieri_vali):
        self.__srv = InchirieriService(inchirieri, client, carte , validator)

        start = 2000
        stop = 2010
        period = Perioada(start, stop)
        chirie1 = self.__srv.add_inchirieri(6, 3, period)

        client = chirie1.getClient()
        carte = chirie1.getCarte()

        # print("TEST")
        self.assertEqual(client.getNume() , 'Miruna')
        self.assertEqual(carte.getTitlu() , 'Arta subtila a nepasarii')

    def test_autor_nrinc(self):
        # def __init__(self, inchirieri_repo, client_repo, carte_repo, inchirieri_vali):
        test_inchirieri_repo = InchirieriMemoryRepository()

        test_client_repo = ClientiMemoryRepository()
        test_carte_repo = CartiMemoryRepository()

        test_carte_vali = CartiValidator()
        test_client_vali = ClientiValidator()

        test_client_service = ClientiService(test_client_repo,test_client_vali)
        test_carte_service = CartiService(test_carte_repo,test_carte_vali)

        da1 = test_client_service.Default()
        da2 = test_carte_service.Default()

        test_inchirieri_vali = InchiriereValidator()

        test_inchirieri = InchirieriService(test_inchirieri_repo,test_client_repo,test_carte_repo,test_inchirieri_vali)
        inchirieri = test_inchirieri.Default()

        lista = test_inchirieri.autor_nrinc()
        lista = test_inchirieri.sorted_by_cr(lista)


        # print("Intrat")
        # for el in lista:
        #     print(el['nume'] + " " + str(el['cr']))

        self.assertEqual(lista[0]['nume'] , 'Mark Manson')
        self.assertEqual(lista[1]['cr'] , 2)