# from domain.entities import Clienti
from domain.entities import Carti

# from domain.validators import ClientiValidator
from domain.validators import CartiValidator

from repository.library_repo import InMemoryRepository


class CartiService:
    """
    In clasa carti vom scrie functiile pentru Carti
    pe care le vom apela in ui
    """
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def get_all_carti(self):
        return self.__repo.get_all()

    def add_carti(self, id, titlu, descriere, autor):
        """
        Functia add_carti adauga carti in lista de carti
        utilizand repo
        :param id: id-ul cartii
        :param titlu: titlul cartii pe care doriti sa o introduceti
        :param descriere: Descrierea cartii
        :param autor: Autorul cartii
        :return: functia returneaza obiectul adaugat
        """
        carti = Carti(id, titlu, descriere, autor)

        self.__validator.validate(carti)
        self.__repo.store(carti)
        return carti
    def show_carti(self):
        """
        Functia show_carti returneaza toata lista
        :return:
        """
        return self.__repo.get_all()

    def delete_carti_id(self, id):
        return self.__repo.deleteId(id)

    def update_carti_id(self,id,titlu,descriere,autor):
        carti1 = Carti(id,titlu,descriere,autor)
        self.__validator.validate(carti1)
        return self.__repo.update_carti(id,carti1)

    def search_carti_id(self,id):
        return self.__repo.search(id)

    def sorted(self, list, key=lambda x: x, reversed=False, cmp=None):
        return self.__repo.sorted(list, key, reversed, cmp)

    def Default(self):
        carti1 = Carti(1,
                       'Atomic Habits',
                       "O carte extrem de practica si utila. James Clear "
                       "\nextrage informatiile fundamentale despre formarea obiceiurilor, astfel ca tu sa poti realiza mai "
                       "\nmult concentrandu-te pe mai putine lucruri.",
                       "James Clear")
        self.__validator.validate(carti1)
        self.__repo.store(carti1)

        carti2 = Carti(2,
                       'Tata Bogat',
                       "Principalul motiv pentru care oamenii se lupta cu dificultatile "
                       "\nfinanciare este acela ca au trecut prin scoala fara sa invete nimic despre bani. Rezultatul este ca invata sa lucreze pentru bani dar nu invata niciodata sa puna "
                       "\nbanii sa actioneze pentru ei.",
                       "Robert T. Kiyosaki")
        self.__validator.validate(carti2)
        self.__repo.store(carti2)

        carti3 = Carti(3,
                       'Arta subtila a nepasarii',
                       'In acest ghid revolutionar, definitoriu pentru o intreaga '
                       '\ngeneratie, autorul ne invata ca, pentru a fi fericiti, trebuie sa renuntam la a fi "pozitivi" mereu si trebuie, '
                       '\nin schimb, sa ne perfectionam in invingerea obstacolelor.',
                       "Mark Manson")
        self.__validator.validate(carti3)
        self.__repo.store(carti3)

        carti4 = Carti(4,
                       'Pas cu pas',
                       'Am adunat in aceasta carte momente din viata publica, incercand sa refac, din ceea ce a selectat memoria, '
                       '\ntraseul profesional care m-a adus de la catedra de fizica la ipostaza de candidat pentru presedintie. '
                       '\nAm inclus in ea si lucruri personale, dar nu am facut o neaparat pentru a raspunde curiozitatii celorlalti.',
                       "Klaus Iohannis")
        self.__validator.validate(carti4)
        self.__repo.store(carti4)

        carti5 = Carti(5,
                       'Fake',
                       'Bani contrafacuti. In 1971, presedintele Richard Nixon a anulat etalonul aur in privinta dolarului. In 1971, '
                       '\ndolarul american a devenit moneda fiduciara, adica banul guvernului. Tatal bogat numea banii guvernului '
                       '\n„bani contrafacuti“, meniti sa ii faca pe bogati si mai bogati. Problema este ca acestia ii fac pe cei saraci '
                       '\nsi pe cei din clasa de mijloc si mai saraci.',
                       "Robert T. Kiyosaki")
        self.__validator.validate(carti5)
        self.__repo.store(carti5)
        return self.__repo