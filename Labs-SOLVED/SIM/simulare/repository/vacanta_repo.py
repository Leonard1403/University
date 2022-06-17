from domain.entities import Locatie
# <id_locatie>, <denumire>, <tip>, <pret_pe_zi>

class InMemoryRepo:
    def __init__(self):
        vacante = []

    def getall(self):
        return self.__vacante



class InFileRepo:
    def __init__(self,filename):
        self.__filename = filename

    def __load(self):
        '''
        Functie care scoate valori din fisier
        :return:
        '''
        # try:
        #     f = open(self.__filename,'r')
        # except IOError:
        #     print("Eroare la citire")
        with open(self.__filename, 'r') as f:
            all_vacante = []
            lines = f.readlines()
            for line in lines:
                id_locatie , denumire , tip , pret_pe_zi = [token.strip() for token in line.split(',')]
                pret_pe_zi = int(pret_pe_zi)
                vacanta = Locatie(id_locatie,denumire,tip,pret_pe_zi)
                all_vacante.append(vacanta)
            # f.close()
            return all_vacante

    def __save(self,all_vacante):
        '''
        Functie care salveaza in fisier
        :param all_vacante:
        :return:
        '''
        with open(self.__filename,'w') as f:
            for vacanta in all_vacante:
                vacante_string = str(vacanta.getId_locatie()) + ', ' + str(vacanta.getDenumire()) + ', ' + str(vacanta.getTip) + ', ' + str(vacanta.getPret_pe_zi) + '\n'
                f.write(vacante_string)

    def getall(self):
        '''
        Returneaza toate valorile din fisier
        :return: returneaza valorile din fisier
        '''
        return self.__load()

    def search_tip(self,tip):
        '''
        Functie care cauta o locatie pentru un tip dat
        :param tip: tip reprezinta tipul unde se afla locatia data
        :return: se returneaza toate vacantele care au un anumit tip dat
        '''
        vacante_tip = []
        all_vacante = self.getall()

        for vacanta in all_vacante:
            if vacanta.getTip() == tip:
                vacante_tip.append(vacanta)

        return vacante_tip

    def search_id(self,id):
        '''
        Functie care cauta o locatie pentru un id dat
        :param id: id ul reprezinta id-ul pe care il are locatia data
        :return: returneaza vacanta daca se gaseste locatia cu id-ul dat , daca nu, se returneaza None
        '''
        all_vacante = self.getall()
        for vacanta in all_vacante:
            if vacanta.getId_locatie() == id:
                return vacanta
        return None

class Teste:
    def __init__(self,filename,repo):
        self.__filename = filename
        self.__repo = repo

    def __test_search_tip(self):
        vacante = self.__repo.search_tip('munte')
        vacanta = vacante[0]
        assert vacanta.getId_locatie() == '2'
        assert vacanta.getDenumire() == 'La Ionel'
        assert vacanta.getPret_pe_zi() == 85

    def __test_search_id(self):
        vacanta = self.__repo.getall(2)
        print(vacanta)
        # assert vacanta.getId_locatie() == '12'
        assert vacanta.getDenumire() == 'River Edge Resort'
        assert vacanta.getTip() == 'aproape de munte'
        assert vacanta.getPret_pe_zi() == 330

    def TEST(self):
        self.__test_search_tip()
        # self.__test_search_id()
