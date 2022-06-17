import unittest

from domain.entities import Clienti
from domain.validators import ClientiValidator

# def __init__(self, id, nume, CNP):
from exceptions.exception import ValidationException


class TestCaseClientiDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = ClientiValidator()

    def test_create_clienti(self):
        client = Clienti(1, 'Leonard', '1234567891126')
        # client2 = Clienti(2, 'Dorel', '1298567891126')
        # client3 = Clienti(3, 'Marin', '6834567891126')
        # client4 = Clienti(4, 'Adi Despot', '3334567891126')
        # client5 = Clienti(5, 'Marian', '0734567891126')
        # client6 = Clienti(6, 'Miruna', '1298479182726')

        self.assertEqual(client.getId(),1)
        self.assertEqual(client.getNume(),'Leonard')
        self.assertEqual(client.getCNP(),'1234567891126')

    def test_clienti_validator(self):

        client1 = Clienti(2002, "Leonard", '5001202010005')
        client2 = Clienti(0, "L3onard", '10')

        self.__validator = ClientiValidator()
        self.__validator.validate(client1)
        self.__validator.validate(client2)

        self.assertRaises(ValidationException, self.__validator.validate, client1)
        self.assertRaises(ValidationException, self.__validator.validate, client2)