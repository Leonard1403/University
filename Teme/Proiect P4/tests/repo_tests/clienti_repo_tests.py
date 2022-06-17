from domain.entities import Clienti
from repository.clienti import ClientiFileRepository, ClientiMemoryRepository
import unittest

class TestCaseClientiRepoInMemory(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = ClientiMemoryRepository()
        self.__add_predefined_clients()

    def __add_predefined_clients(self):
        client1 = Clienti(1, 'Leonard', '1234567891126')
        client2 = Clienti(2, 'Dorel', '1298567891126')
        client3 = Clienti(3, 'Marin', '6834567891126')
        client4 = Clienti(4, 'Adi Despot', '3334567891126')
        client5 = Clienti(5, 'Marian', '0734567891126')
        client6 = Clienti(6, 'Miruna', '1298479182726')

        self.__repo.store(client1)
        self.__repo.store(client2)
        self.__repo.store(client3)
        self.__repo.store(client4)
        self.__repo.store(client5)
        self.__repo.store(client6)

    def test_search(self):
        test = self.__repo.search(1)
        self.assertEqual(test.getId(), 1)
        self.assertEqual(test.getNume(), 'Leonard')
        self.assertEqual(test.getCNP(), '1234567891126')

    def test_update(self):
        client_update = Clienti(1, 'Maria', '3334567891126')
        test = self.__repo.update_clienti(1, client_update)
        self.assertEqual(test.getId(), 1)
        self.assertEqual(test.getNume(), 'Maria')
        self.assertEqual(test.getCNP(), '3334567891126')

    def test_delete(self):
        self.__repo.deleteId(2)
        self.assertEqual(self.__repo.size(), 5)

    def test_get_all(self):
        clienti = self.__repo.get_all()
        self.assertIsInstance(clienti, list)

        self.assertEqual(len(clienti), 6)

        self.__repo.deleteId(1)
        self.__repo.deleteId(2)

        clienti = self.__repo.get_all()
        self.assertEqual(len(clienti), 4)

    # def test_load_from_file(self):
    #     self.assertEqual(len(self.__repo.get_all()), 1)

    def test_store(self):
        self.__repo.delete_all()
        self.__repo.store(Clienti(125125, 'Marian', '4834567891126'))
        self.assertEqual(self.__repo.size(), 1)


class TestCaseClientiRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = ClientiFileRepository('test_clienti_repo')
        self.__add_predefined_clients()

    def __add_predefined_clients(self):
        client1 = Clienti(1, 'Leonard', '1234567891126')
        client2 = Clienti(2, 'Dorel', '1298567891126')
        client3 = Clienti(3, 'Marin', '6834567891126')
        client4 = Clienti(4, 'Adi Despot', '3334567891126')
        client5 = Clienti(5, 'Marian', '0734567891126')
        client6 = Clienti(6, 'Miruna', '1298479182726')

        self.__repo.store(client1)
        self.__repo.store(client2)
        self.__repo.store(client3)
        self.__repo.store(client4)
        self.__repo.store(client5)
        self.__repo.store(client6)

    def test_search(self):
        test = self.__repo.search(1)
        self.assertEqual(test.getId(),1)
        self.assertEqual(test.getNume(),'Leonard')
        self.assertEqual(test.getCNP(),'1234567891126')

    def test_update(self):
        client_update = Clienti(1, 'Maria', '3334567891126')
        test = self.__repo.update_clienti(1,client_update)
        self.assertEqual(test.getId(),1)
        self.assertEqual(test.getNume(),'Maria')
        self.assertEqual(test.getCNP(),'3334567891126')

    def test_delete(self):
        self.__repo.deleteId(2)
        self.assertEqual(self.__repo.size(),5)

    def test_get_all(self):
        clienti = self.__repo.get_all()
        self.assertIsInstance(clienti, list)

        self.assertEqual(len(clienti),6)

        self.__repo.deleteId(1)
        self.__repo.deleteId(2)

        clienti = self.__repo.get_all()
        self.assertEqual(len(clienti),4)

    def test_load_from_file(self):
        self.assertEqual(len(self.__repo.get_all()),6)

    def test_store(self):
        self.__repo.delete_all()
        self.__repo.store(Clienti(125125, 'Marian', '4834567891126'))
        self.assertEqual(self.__repo.size(),1)
    def tearDown(self) -> None:
        self.__repo.delete_all()

