from domain.entities import Parcari



class InMemoryRepo:
    def __init__(self):
        self.__parcari = []
    def store(self,parcare):
        self.__parcari.append(parcare)

    def get_all(self):
        return self.__parcari

    def search_strada(self):
        pass

class InFileRepo:
    def __init__(self,file_name):
        self.__filename = file_name

    def __load(self):
        try:
            f = open(self.__filename,'r')
        except IOError as ve:
            print("Eroare de citire din fisier")

        all_parcari = []
        lines = f.readlines()
        for line in lines:
            id , nume , strada , numar_utilizari = [token.strip() for token in line.split(',')]
            parcare = Parcari(id,nume,strada,numar_utilizari)
            all_parcari.append(parcare)
        f.close()
        return all_parcari

    def __save(self,all_parcari):
        with open(self.__filename,'w') as f:
            for parcare in all_parcari:
                parcare_string = parcare.getid() + ',' + parcare.getnume() + ',' + parcare.getstrada() + ',' + parcare.getnumar_utilizari() + '\n'
                f.write(parcare_string)
    def get_all(self):
        return self.__load()

    def search_strada(self,strada):
        all_parcari = self.get_all()
        iduri = []
        for parcare in all_parcari:
            if parcare.getstrada() == strada:
                iduri.append(parcare.getid())
        return iduri

    def baga(self,numele,strada):
        return {'strada' : strada , 'numele' : numele}

    def __getstrada(self):
        return ['strada']
    def __getnumele(self):
        return ['numele']

    def __exista(self,lista, strada):
        for el in lista:
            if el.self.__getstrada() == strada:
                return el
        return False

    def utilizat(self):
        parcari = []
        if self.__exista()