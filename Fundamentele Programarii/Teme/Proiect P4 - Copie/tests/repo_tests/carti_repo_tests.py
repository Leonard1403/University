from domain.entities import Carti
from repository.carti import CartiFileRepository, CartiMemoryRepository
import unittest

class TestCaseCartiiRepoInMemory(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = CartiMemoryRepository()
        self.__add_predefined_clients()

    def __add_predefined_clients(self):
        carti1 = Carti(1,
                       'Atomic Habits',
                       "O carte extrem de practica si utila. James Clear "
                       "\nextrage informatiile fundamentale despre formarea obiceiurilor, astfel ca tu sa poti realiza mai "
                       "\nmult concentrandu-te pe mai putine lucruri.",
                       "James Clear")


        carti2 = Carti(2,
                       'Tata Bogat',
                       "Principalul motiv pentru care oamenii se lupta cu dificultatile "
                       "\nfinanciare este acela ca au trecut prin scoala fara sa invete nimic despre bani. Rezultatul este ca invata sa lucreze pentru bani dar nu invata niciodata sa puna "
                       "\nbanii sa actioneze pentru ei.",
                       "Robert T. Kiyosaki")


        carti3 = Carti(3,
                       'Arta subtila a nepasarii',
                       'In acest ghid revolutionar, definitoriu pentru o intreaga '
                       '\ngeneratie, autorul ne invata ca, pentru a fi fericiti, trebuie sa renuntam la a fi "pozitivi" mereu si trebuie, '
                       '\nin schimb, sa ne perfectionam in invingerea obstacolelor.',
                       "Mark Manson")


        carti4 = Carti(4,
                       'Pas cu pas',
                       'Am adunat in aceasta carte momente din viata publica, incercand sa refac, din ceea ce a selectat memoria, '
                       '\ntraseul profesional care m-a adus de la catedra de fizica la ipostaza de candidat pentru presedintie. '
                       '\nAm inclus in ea si lucruri personale, dar nu am facut o neaparat pentru a raspunde curiozitatii celorlalti.',
                       "Klaus Iohannis")

        self.__repo.store(carti1)
        self.__repo.store(carti2)
        self.__repo.store(carti3)
        self.__repo.store(carti4)


    def test_search(self):
        """
        Functie test de cautare dupa un id dat
        :return:
        """
        test = self.__repo.search(1)
        self.assertEqual(test.getId(),1)
        self.assertEqual(test.getTitlu(),'Atomic Habits')

        carti = Carti(10,'Da','Da','Da')
        self.__repo.store(carti)
        test = self.__repo.search(10)
        self.assertEqual(test.getId(),10)
        self.assertEqual(test.getTitlu(),'Da')

    def test_delete(self):
        """
        Functie de testare care verifica daca se sterge un element din lista
        :return:
        """
        self.__repo.deleteId(2)
        self.assertEqual(self.__repo.size(), 3)

    def test_get_all(self):
        """
        Functie care testeaza daca e obtin toate obiectele
        :return:
        """
        clienti = self.__repo.get_all()
        self.assertIsInstance(clienti, list)

        self.assertEqual(len(clienti), 4)

        self.__repo.deleteId(1)
        self.__repo.deleteId(2)

        clienti = self.__repo.get_all()
        self.assertEqual(len(clienti), 2)

    # def test_load_from_file(self):
    #     self.assertEqual(len(self.__repo.get_all()), 1)

    def test_store(self):
        pass


class TestCaseClientiRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = CartiFileRepository('test_carti_repo')
        self.__add_predefined_clients()

    def __add_predefined_clients(self):
        carti1 = Carti(1,
                       'Atomic Habits',
                       "O carte extrem de practica si utila. James Clear "
                       "extrage informatiile fundamentale despre formarea obiceiurilor, astfel ca tu sa poti realiza mai"
                       "mult concentrandu-te pe mai putine lucruri.",
                       "James Clear")

        carti2 = Carti(2,
                       'Tata Bogat',
                       "Principalul motiv pentru care oamenii se lupta cu dificultatile "
                       "financiare este acela ca au trecut prin scoala fara sa invete nimic despre bani. Rezultatul este ca invata sa lucreze pentru bani dar nu invata niciodata sa puna "
                       "banii sa actioneze pentru ei.",
                       "Robert T. Kiyosaki")

        carti3 = Carti(3,
                       'Arta subtila a nepasarii',
                       'In acest ghid revolutionar, definitoriu pentru o intreaga '
                       'generatie, autorul ne invata ca, pentru a fi fericiti, trebuie sa renuntam la a fi "pozitivi" mereu si trebuie, '
                       'in schimb, sa ne perfectionam in invingerea obstacolelor.',
                       "Mark Manson")

        carti4 = Carti(4,
                       'Pas cu pas',
                       'Am adunat in aceasta carte momente din viata publica, incercand sa refac, din ceea ce a selectat memoria, '
                       'traseul profesional care m-a adus de la catedra de fizica la ipostaza de candidat pentru presedintie. '
                       'Am inclus in ea si lucruri personale, dar nu am facut o neaparat pentru a raspunde curiozitatii celorlalti.',
                       "Klaus Iohannis")

        self.__repo.store(carti1)
        self.__repo.store(carti2)
        self.__repo.store(carti3)
        self.__repo.store(carti4)

    def test_search(self):
        test = self.__repo.search(1)
        self.assertEqual(test.getId(), 1)
        self.assertEqual(test.getTitlu(), 'Atomic Habits')

        carti = Carti(10, 'Da', 'Da', 'Da')
        self.__repo.store(carti)
        test = self.__repo.search(10)
        self.assertEqual(test.getId(), 10)
        self.assertEqual(test.getTitlu(), 'Da')

    def test_delete(self):
        self.__repo.deleteId(2)
        self.assertEqual(self.__repo.size(), 3)

    def test_get_all(self):
        clienti = self.__repo.get_all()
        self.assertIsInstance(clienti, list)

        self.assertEqual(len(clienti), 4)

        self.__repo.deleteId(1)
        self.__repo.deleteId(2)

        clienti = self.__repo.get_all()
        self.assertEqual(len(clienti), 2)

    def test_load_from_file(self):
        self.assertEqual(len(self.__repo.get_all()),4)

    def test_store(self):
        self.__repo.delete_all()
        self.__repo.store(Carti(1251, 'Da', 'Da', 'Da'))
        self.assertEqual(self.__repo.size(),1)
    def tearDown(self) -> None:
        self.__repo.delete_all()

