import unittest

from domain.entities import Clienti, Carti, Inchirieri, Perioada
from domain.validators import InchiriereValidator

class TestCaseInchirieriDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = InchiriereValidator()

    def test_create_inchirieri(self):
        carti = Carti(125, 'Ion', 'Un taran care la final moare', 'Liviu Rebreanu')
        client = Clienti(1, 'Leonard', '1234567891126')
        start = 2010
        stop = 2019
        period = Perioada(start,stop)
        inchiriere = Inchirieri(client, carti, period)

        self.assertEqual(inchiriere.getClient().getId(),1)
        self.assertEqual(inchiriere.getClient().getNume(),'Leonard')

    def test_equal_rating(self):
        carti = Carti(125, 'Ion', 'Un taran care la final moare', 'Liviu Rebreanu')
        client = Clienti(1, 'Leonard', '1234567891126')
        start = 2010
        stop = 2019
        period = Perioada(start, stop)
        inchiriere1 = Inchirieri(client, carti, period)
        inchiriere2 = Inchirieri(client, carti, period)

        self.assertEqual(inchiriere2,inchiriere1)

