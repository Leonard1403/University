# <id_locatie>, <denumire>, <tip>, <pret_pe_zi>

class Locatie:
    def __init__(self,id_locatie,denumire,tip,pret_pe_zi):
        self.__id_locatie = id_locatie
        self.__denumire = denumire
        self.__tip = tip
        self.__pre_pe_zi = pret_pe_zi

    def getId_locatie(self):
        return self.__id_locatie

    def getDenumire(self):
        return self.__denumire

    def getTip(self):
        return self.__tip

    def getPret_pe_zi(self):
        return self.__pre_pe_zi


    def setId_locatie(self,value):
        self.__id_locatie = value

    def setDenumire(self,value):
        self.__denumire = value

    def setTip(self,value):
        self.__tip = value

    def setPret_pe_zi(self,value):
        self.__pre_pe_zi = value

    def __eq__(self,other):
        if self.__id_locatie == other.getId_locatie():
            return True
        return False

    def __str__(self):
        return str(self.__id_locatie) + ', ' + str(self.__denumire) + ', ' + str(self.__tip) + ', ' + str(self.__pre_pe_zi)