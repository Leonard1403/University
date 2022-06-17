from domain.entities import Locatie
from repository.vacanta_repo import InFileRepo

class VacanteService:
    def __init__(self,repo):
        self.__repo = repo

    def getall(self):
        '''
        Functie care obtine toate locatile
        :return: returneaza toate locatile
        '''
        return self.__repo.getall()

    def search_tip(self,tip):
        '''
        Functie care cauta o locatie dupa un tip dat
        :param tip:
        :return:
        '''
        return self.__repo.search_tip(tip)

    def search_id(self,id):
        '''
        Functie care cauta o locatie dupa un id dat
        :param id:
        :return:
        '''
        return self.__repo.search_id(id)

class BookingInquiry:
    def __init__(self, locatie, buget):
        self.__locatie = locatie
        self.__buget = buget

    def get_number_of_days(self):
        '''
        Functie care determina numarul de zile pe care le poate inchiria o persoana dupa un buget dat
        :return: numarul de zile posibile pentru inchiriere
        '''
        pret_pe_zi = self.__locatie.getPret_pe_zi()
        pret_pe_zi = int(pret_pe_zi)
        return int(self.__buget/pret_pe_zi)

    def get_denumire(self):
        '''
        Functie care obtine denumirea unei locatii date
        :return: returneaza denumirea
        '''
        return self.__locatie.getDenumire()

    def get_tipul(self):
        '''
        Functie care obtine tipul unei locatii date in clasa aceasta
        :return: returneaza locatia
        '''
        return self.__locatie.getTip()

def test_search_id():
    repo = InFileRepo('test.txt')
    srv = VacanteService(repo)


    assert srv.search_id(2).getDenumire() == 'La Ionel'
    assert srv.search_id(4).getDenumire() == 'Seaside Hotel'
    assert srv.search_id(12).getDenumire() == 'River Edge Resort'

    # print(srv.search_id(2).getDenumire())


def TEST():
    test_search_id()

# TEST()