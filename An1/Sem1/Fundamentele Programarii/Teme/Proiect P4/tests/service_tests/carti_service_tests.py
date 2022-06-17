import unittest
from domain.entities import Carti
from domain.validators import CartiValidator
from exceptions.exception import ValidationException
from repository.carti import CartiFileRepository, CartiMemoryRepository
from service.carti_service import CartiService


class TestCaseCartiService(unittest.TestCase):
    def setUp(self) -> None:
        repo = CartiMemoryRepository()
        validator = CartiValidator()
        self.__srv = CartiService(repo,validator)

    def test_add_carti(self):

        test_carti = self.__srv.add_carti(2,'da','nu','poate')

        self.assertEqual(test_carti.getId(),2)
        self.assertEqual(test_carti.getTitlu(),'da')
        self.assertEqual(test_carti.getAutor() , 'poate')
        self.assertEqual(test_carti.getDescriere() , 'nu')


    def test_delete_carti(self):

        test_carti = self.__srv.add_carti(2, 'da', 'poate', 'nu')
        deleted_carti = self.__srv.delete_carti_id(2)
        self.assertEqual(len(self.__srv.get_all_carti()) , 0)
        self.assertEqual(test_carti.getId() , 2)
        self.assertEqual(test_carti.getTitlu() , 'da')
        self.assertEqual(test_carti.getAutor() , 'nu')
        self.assertEqual(test_carti.getDescriere() , 'poate')

    def test_search_carti(self):
        self.__srv.add_carti(2, 'da', 'poate', 'nu')
        test = self.__srv.search_carti_id(2)
        self.assertEqual(test.getId() , 2)
        self.assertEqual(test.getTitlu() , 'da')
        self.assertEqual(test.getAutor() , 'nu')
        self.assertEqual(test.getDescriere() , 'poate')


    def test_update_carti(self):

        test = self.__srv.add_carti(2, 'da', 'poate', 'nu')

        self.assertEqual(test.getId() , 2)
        self.assertEqual(test.getTitlu() , 'da')
        self.assertEqual(test.getAutor() , 'nu')
        self.assertEqual(test.getDescriere() , 'poate')

        test = self.__srv.update_carti_id(2,'nu','Poate','da')
        self.assertEqual(test.getId() , 2)
        self.assertEqual(test.getTitlu() , 'nu')
        self.assertEqual(test.getAutor() , 'da')
        self.assertEqual(test.getDescriere() , 'Poate')
