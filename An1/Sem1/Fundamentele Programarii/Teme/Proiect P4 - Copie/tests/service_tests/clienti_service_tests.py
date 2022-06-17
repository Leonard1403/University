import unittest
from domain.validators import ClientiValidator
from domain.entities import Clienti
from exceptions.exception import *
from repository.clienti import ClientiMemoryRepository
from service.clienti_service import ClientiService

class TestCaseClientiService(unittest.TestCase):
    def setUp(self) -> None:
        repo = ClientiMemoryRepository()
        validator = ClientiValidator()
        self.__srv = ClientiService(repo,validator)

    def test_add_clienti(self):

        test_clienti = self.__srv.add_clienti(15,'Miruna','0734567891126')
        self.assertEqual(test_clienti.getId(),15)
        self.assertEqual(test_clienti.getNume(),'Miruna')
        self.assertEqual(test_clienti.getCNP(),'0734567891126')

    def test__delete_clienti(self):

        self.__srv.add_clienti(15, 'Miruna', '0734567891126')
        self.__srv.add_clienti(12, 'Monica', '0123468918126')
        deleted_clienti = self.__srv.delete_clienti_id(12)
        self.assertEqual(len(self.__srv.get_all_clienti()),1)
        self.assertEqual(deleted_clienti.getId(),12)
        self.assertEqual(deleted_clienti.getNume(),'Monica')
        self.assertEqual(deleted_clienti.getCNP(),'0123468918126')

    def test_search_clienti(self):

        self.__srv.add_clienti(15,'Simon','5274567891126')
        obj = self.__srv.search_clienti_id(15)
        self.assertEqual(obj.getId(),15)
        self.assertEqual(obj.getNume(),'Simon')
        self.assertEqual(obj.getCNP(),'5274567891126')

    def test_update_clienti(self):
        self.__srv.add_clienti(15,'Simon','5274567891126')
        obj = self.__srv.search_clienti_id(15)
        self.assertEqual(obj.getId(),15)
        self.assertEqual(obj.getNume(),'Simon')
        self.assertEqual(obj.getCNP(),'5274567891126')

        self.__srv.update_clienti_id(15,'Miruna','6274567891126')

        obj = self.__srv.search_clienti_id(15)
        self.assertEqual(obj.getId(),15)
        self.assertEqual(obj.getNume(),'Miruna')
        self.assertEqual(obj.getCNP(),'6274567891126')
