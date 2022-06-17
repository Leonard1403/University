#Cont bancar


# def separare_comanda(comanda,i):
#     informatii_comanda = comanda.split()
#     informatii_comanda[i] = informatii_comanda[i].strip()
#     return informatii_comanda[i]

def adaugare_cheltuieli(cheltuieli):
    """
    Functia de adaugare care are 2 comenzi , una de adaugare in dictionar si cealalta de actualizare a
    unui element dat de pe o pozitie data
    :param cheltuieli: parametrul prin care se modifica dictionarul de liste
    :return: NULL
    """
    print("1.Adauga o cheltuiala noua")
    print("2.Actualizeaza o cheltuiala")

    cerinta = int(input("Comanda: "))
    quest = input("Introduceti datele(zi,suma,tipul): ")
    quest_da = quest.split()
    ziua = int(quest_da[0])
    suma = int(quest_da[1])
    tipul = quest_da[2]

    marime1 = int(len(cheltuieli['ziua']))
    if cerinta == 1:
        cheltuieli['ziua'].append(ziua)
        cheltuieli['suma'].append(suma)
        cheltuieli['tipul'].append(tipul)
        marime2 = int(len(cheltuieli['ziua']))
        assert marime1+1 == marime2
    elif cerinta == 2:
        ordin = int(input("Introduceti ordinul: "))
        cheltuieli['ziua'][ordin-1] = ziua
        cheltuieli['suma'][ordin-1] = suma
        cheltuieli['tipul'][ordin-1] = tipul
        marime2 = int(len(cheltuieli['ziua']))
        assert marime1 == marime2
    # if len(cheltuieli['ziua']) == 0:
    #     cheltuieli['ziua'].append(ziua)
    #     cheltuieli['suma'].append(suma)
    #     cheltuieli['tipul'].append(tipul)
    # else:
    #     ok = 0
    #     for el in range(0,len(cheltuieli['ziua'])):
    #         if int(cheltuieli['ziua'][el]) == ziua:
    #             ok = 1
    #             cheltuieli['suma'][el] = suma
    #             cheltuieli['tipul'][el] = tipul
    #     if ok==0:
    #         cheltuieli['ziua'].append(ziua)
    #         cheltuieli['suma'].append(suma)
    #         cheltuieli['tipul'].append(tipul)




def afisare(cheltuieli):
    """
    Functie de afisare care afiseaza toate elementele din dictionarul de liste
    :param cheltuieli: dictionarul de liste prin care furnizam cheltuielile
    :return: NULL
    """
    for el in range(0,len(cheltuieli['ziua'])):
        print("Cr:" + str(el+1) + "|  Ziua : " + str(cheltuieli['ziua'][el]) + "|  Suma : " + str(cheltuieli['suma'][el]) + "|  Tipul : " + str(cheltuieli['tipul'][el]))

def stergere_cheltuieli(cheltuieli):
    """
    Functie de stergere cheltuieli
    :param cheltuieli: dictionarul de liste prin care furnizam cheltuielile
    :return: NULL
    """
    print("1.Sterge cheltuieli pentru o zi data")
    print("2.Sterge cheltuieli pentru un interval de timp")
    print("3.Sterge cheltuieli pentru un anumit timp")
    cerinta = int(input("Comanda: "))
    # assert isinstance(cerinta, str) == True
    if cerinta == 1:
        zi = int(input("Ziua data: "))



        # new_cheltuieli = [indc from indc in cheltuieli if int(indc['ziua']) == zi]


        marime = int(len(cheltuieli['ziua']))
        el = 0
        while el<marime:
            if int(cheltuieli['ziua'][el]) == zi:
                while el < marime-1:
                    cheltuieli['ziua'][el] = cheltuieli['ziua'][el+1]
                    cheltuieli['suma'][el] = cheltuieli['suma'][el+1]
                    cheltuieli['tipul'][el] = cheltuieli['tipul'][el+1]
                    el = el + 1
                marime = marime - 1
                cheltuieli['ziua'].pop()
                cheltuieli['suma'].pop()
                cheltuieli['tipul'].pop()
                el = -1
            el = el + 1
        if int(cheltuieli['ziua'][marime]) == zi:
            cheltuieli['ziua'].pop()
            cheltuieli['suma'].pop()
            cheltuieli['tipul'].pop()
    elif cerinta == 2:
        zi1 = int(input("Ziua1: "))
        zi2 = int(input("Ziua2: "))
        if(zi1>zi2):
            aux = zi1
            zi1 = zi2
            zi2 = aux
        marime = int(len(cheltuieli['ziua']))
        el = 0
        while el < marime:
            if int(cheltuieli['ziua'][el]) >= zi1 and int(cheltuieli['ziua'][el]) <= zi2:
                while el < marime - 1:
                    cheltuieli['ziua'][el] = cheltuieli['ziua'][el + 1]
                    cheltuieli['suma'][el] = cheltuieli['suma'][el + 1]
                    cheltuieli['tipul'][el] = cheltuieli['tipul'][el + 1]
                    cheltuieli['ziua'].pop()
                    cheltuieli['suma'].pop()
                    cheltuieli['tipul'].pop()
                    el = el + 1
                marime = marime - 1
                el = -1
            el = el + 1
        if int(cheltuieli['ziua'][marime]) >= zi1 and int(cheltuieli['ziua'][marime]) <= zi2:
                cheltuieli['ziua'].pop()
                cheltuieli['suma'].pop()
                cheltuieli['tipul'].pop()
    elif cerinta == 3:
        tip = input("Introduceti tipul: ")
        marime = int(len(cheltuieli['ziua']))
        el = 0
        while el < marime:
            if cheltuieli['tip'][el] == tip:
                while el < marime - 1:
                    cheltuieli['ziua'][el] = cheltuieli['ziua'][el + 1]
                    cheltuieli['suma'][el] = cheltuieli['suma'][el + 1]
                    cheltuieli['tipul'][el] = cheltuieli['tipul'][el + 1]
                    cheltuieli['ziua'].pop()
                    cheltuieli['suma'].pop()
                    cheltuieli['tipul'].pop()
                    el = el + 1
                marime = marime - 1
                el = -1
            el = el + 1
        if cheltuieli['tip'][marime] == tip:
            cheltuieli['ziua'].pop()
            cheltuieli['suma'].pop()
            cheltuieli['tipul'].pop()

def cautare_cheltuieli(cheltuieli):
    """
    Functia de cautare cheltuieli care are 3 functionalitati
    :param cheltuieli:
    :return: NULL
    """

    print("1.Tiparire toate cheltuielile mai mari decat o suma data")
    print("2.Tiparire toate cheltuielile efectuate inainte de o zi data si mai mici decat o suma")
    print("3.Tiparire toate cheltuielile de un anumit tip")
    cerinta = int(input("Comanda: "))
    assert isinstance(cerinta, int) == True
    if cerinta == 1:
        suma = int(input("Introduceti suma: "))
        ok = 1
        for el in range(0,len(cheltuieli['ziua'])):
            if int(cheltuieli['suma'][el]) > suma:
                assert int(cheltuieli['suma'][el]) > suma
                print("Cr:" + str(ok) + "|  Ziua : " + str(cheltuieli['ziua'][el]) + "|  Suma : " + str(cheltuieli['suma'][el]) + "|  Tipul : " + str(cheltuieli['tipul'][el]))
                ok = ok + 1
    elif cerinta == 2:
        zi = int(input("Introduceti ziua: "))
        suma = int(input("Introduceti suma: "))
        ok = 1
        for el in range(0,len(cheltuieli['ziua'])):
            if int(cheltuieli['suma'][el]) < suma and int(cheltuieli['ziua'][el]) < zi:
                print("Cr:" + str(ok) + "|  Ziua : " + str(cheltuieli['ziua'][el]) + "|  Suma : " + str(cheltuieli['suma'][el]) + "|  Tipul : " + str(cheltuieli['tipul'][el]))
                ok = ok + 1
    elif cerinta == 3:
        ok = 1
        tip = input("Introduceti tipul: ")
        for el in range(0,len(cheltuieli['ziua'])):
            if cheltuieli['tipul'][el] == tip:
                print("Cr:" + str(ok) + "|  Ziua : " + str(cheltuieli['ziua'][el]) + "|  Suma : " + str(cheltuieli['suma'][el]) + "|  Tipul : " + str(cheltuieli['tipul'][el]))
                ok = ok + 1

def rapoarte_cheltuieli(cheltuieli):
    """
    Functie de rapoarte cheltuieli care tipareste in functie de cerinta
    :param cheltuieli:dictionarul de liste prin care furnizam cheltuielile
    :return:
    """

    print("1.Tipareste suma totala pentru un anumit tip de cheltuiala")
    print("2.Se afiseaza ziua in care suma cheltuita este maxima")
    print("3.Tipareste toate cheltuielile ce au o anumita suma")
    print("4.Tipareste cheltuielile dupa tip")
    cerinta = int(input("Comanda: "))
    assert isinstance(cerinta, str) == True
    if cerinta==1:
        tip = input("Tipul pentru care se doreste calcularea sumei: ")
        zuma = 0
        for el in range(0, len(cheltuieli['ziua'])):
            if cheltuieli['tipul'][el] == tip:
                zuma = zuma + int(cheltuieli['suma'][el])
        print("Suma este " + str(zuma))
    elif cerinta == 2:
        pass
    elif cerinta == 3:
        pass
    elif cerinta == 4:
        pass


def filtrare_cheltuilei(cheltuieli):
    print("1.Elimina toate cheltuielile de un anumit tip")
    print("2.Elimina toate cheltuielile mai mici decat o suma data")
    cerinta = int(input("Comanda: "))
    assert isinstance(cerinta, int) == True
    if cerinta == 1:
        tip = input("Tipul: ")
        assert isinstance(tip, str) == True
        ok = 1
        for el in range(0,len(cheltuieli['ziua'])):
            if cheltuieli['tipul'][el] != tip:
                assert cheltuieli['tipul'][el] != tip
                print("Cr:" + str(ok) + "|  Ziua : " + str(cheltuieli['ziua'][el]) + "|  Suma : " + str(
                    cheltuieli['suma'][el]) + "|  Tipul : " + str(cheltuieli['tipul'][el]))
                ok = ok + 1

    elif cerinta == 2:
        suma = int(input("Suma: "))
        ok = 1
        assert isinstance(suma, int) == True
        for el in range(0, len(cheltuieli['ziua'])):
            if int(cheltuieli['suma'][el]) >= suma:
                assert cheltuieli['suma'][el] >= suma
                print("Cr:" + str(ok) + "|  Ziua : " + str(cheltuieli['ziua'][el]) + "|  Suma : " + str(
                    cheltuieli['suma'][el]) + "|  Tipul : " + str(cheltuieli['tipul'][el]))


def undo_cheltuieli(cheltuieli):
    pass

def meniu():
    cheltuieli = {
        'ziua': [15 , 15 , 19 , 20 , 9 , 8 , 17 , 17],
        'suma': [2000 , 124 , 200 , 10 , 120 , 90 , 12587 , 18],
        'tipul':['Miere' , 'avion' , 'Apartament' , 'Orez' , 'GOGOSI' , 'Apartament' , 'Masina' , 'Apartament']
    }

    while True:
        print("Pentru fiecare comanda introduceti 'numele_comenzii' + ziua + suma + tipul")
        print("Comenzile pot fi:")
        print("1.adaugare")
        print("2.stergere")
        print("3.cautare")
        print("4.rapoarte")
        print("5.filtrare")
        print("6.afisare")
        print("7.undo")
        print("8.iesire")

        comanda = input("Comanda:\>  ")
        assert isinstance(comanda, str) == True or isinstance(comanda, int) == True
        # informatii_comanda = separare_comanda(comanda)

        informatii_comanda = comanda.strip()

        # print(informatii_comanda + " " + str(ziua) + " " + str(suma) + " " + tipul)

        if informatii_comanda == "adaugare" or informatii_comanda == "1":
            adaugare_cheltuieli(cheltuieli)
        elif informatii_comanda == "stergere" or informatii_comanda == "2":
            stergere_cheltuieli(cheltuieli)
        elif informatii_comanda == "cautare" or informatii_comanda == "3":
            cautare_cheltuieli(cheltuieli)
        elif informatii_comanda == "rapoarte" or informatii_comanda == "4":
            rapoarte_cheltuieli(cheltuieli)
        elif informatii_comanda == "filtrare" or informatii_comanda == "5":
            filtrare_cheltuilei(cheltuieli)
        elif informatii_comanda == "afisare" or informatii_comanda == "6":
            afisare(cheltuieli)
        elif informatii_comanda == "undo" or informatii_comanda == "7":
            pass
        elif informatii_comanda == "iesire" or informatii_comanda == "8":
            return

meniu()