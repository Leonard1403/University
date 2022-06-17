class Parcari:
    def __init__(self,id,nume,strada,numar_utilizari):
        self.__id = id
        self.__nume = nume
        self.__strada = strada
        self.__numar_utilizari = numar_utilizari

    def getid(self):
        return self.__id
    def getnume(self):
        return self.__nume
    def getstrada(self):
        return self.__strada
    def getnumar_utilizari(self):
        return self.__numar_utilizari

    def setid(self,value):
        self.__id = value

    def setnume(self,value):
        self.__nume = value

    def setstrada(self,value):
        self.__strada = value

    def setnumar_utilizari(self,value):
        self.__numar_utilizari = value

    def __eq__(self,other):
        if self.__id == other.getid():
            return True
        return False

    def __str__(self):
        return str(self.__id) + ',' + str(self.__nume) + ',' + str(self.__strada) + ',' + str(self.__numar_utilizari)