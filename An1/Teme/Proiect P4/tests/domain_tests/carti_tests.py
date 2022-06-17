import unittest

from domain.entities import Carti
from domain.validators import CartiValidator
from exceptions.exception import ValidationException

# def __init__(self, id, titlu, descriere, autor):



class TestCaseCartiRatingDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = CartiValidator()

    def test_create_carti(self):
        """
        Functie de testare creare carti
        :return:
        """
        carti = Carti(125,'Ion','Un taran care la final moare','Liviu Rebreanu')

        self.assertEqual(carti.getId(),125)
        self.assertEqual(carti.getTitlu(),'Ion')
        self.assertEqual(carti.getDescriere(),'Un taran care la final moare')
        self.assertEqual(carti.getAutor(),'Liviu Rebreanu')

    def test_equal_carti(self):
        """
        Functie de verificare a egalitatii unei carti
        :return:
        """
        carti1 = Carti(125, 'Ion', 'Un taran care la final moare', 'Liviu Rebreanu')
        carti2 = Carti(120, 'Ion', 'Un taran care la final moare', 'Liviu Rebreanu')

        self.assertEqual(carti1,carti2)

    def test_carti_validator(self):
        carti = Carti(125, 'Ion', 'Un taran care la final moare', 'Liviu Rebreanu')

        self.__validator = CartiValidator()
        self.__validator.validate(carti)

        self.assertRaises(ValidationException,self.__validator.validate,carti)



