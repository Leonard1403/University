# Cod de testare si implementare
# In vector se vor salva in urmatorul fel:
#       ziua , suma , tipul

from prints.prints import *

# ------------------------------------DEFAULT---------------------------------

def default_cheltuieli(cheltuieli):
    return [[15,   200,   'Masina'     ],
            [25,   200,   'Chirie'     ],
            [3 ,   30 ,   'Mancare'    ],
            [14,   600,   'Masina'     ],
            [10,   150,   'intretinere'],
            [15,   900,   'Haine'      ],
            [3 ,   100000,'Taxe'       ],
            [30,   40000 ,'Masina'     ],
            [27,   7  ,   'Cumparaturi']
            ]

# -------------------------------------GET------------------------------------

def get_ziua_cheltuiala(cheltuieli):
    return cheltuieli[0]

def get_suma_cheltuiala(cheltuieli):
    return cheltuieli[1]

def get_tipul_cheltuiala(cheltuieli):
    return cheltuieli[2]

# -------------------------------------FUNCTII--------------------------------

def show_cheltuieli(cheltuieli):
    print("Am intrat in funnctie")
    for i , curent_cheltuieli in enumerate(cheltuieli):
        print("Cr." + str(i+1)," Ziua: " + str(get_ziua_cheltuiala(curent_cheltuieli)), " Suma: " + str(get_suma_cheltuiala(curent_cheltuieli)), " Tipul: " + get_tipul_cheltuiala(curent_cheltuieli))

def create_cheltuiala(ziua, suma, tipul):
    return [ziua ,suma , tipul]

def add_event_cheltuiala(cheltuiala,event_cheltuiala):
    cheltuiala.append(event_cheltuiala)

def cheltuieli_add_update(cheltuieli,ziua,suma,tipul):
    """
    Functia de add update actualizeaza o cheltuiala din lista data dupa ziua si tipul oferit
    :param cheltuieli: cheltuieli reprezinta lista pe care o avem
    :param ziua: ziua data de utilizator
    :param suma: suma data de utilizator
    :param tipul: tipul dat de utilizator
    :return: Null
    """
    event_cheltuiala = create_cheltuiala(ziua, suma, tipul)
    for i, curent_cheltuieli in enumerate(cheltuieli):
        if int(get_ziua_cheltuiala(curent_cheltuieli)) == int(
                get_ziua_cheltuiala(event_cheltuiala)) and get_tipul_cheltuiala(
                curent_cheltuieli) == get_tipul_cheltuiala(event_cheltuiala):
            cheltuieli[i][1] = suma
            return

def cheltuieli_add(cheltuieli):
    """
    Functia reprezinta functia main a functii de adaugare in care avem
    2 optiuni, una de de adaugare in lista si cea de update
    :param cheltuieli: lista data
    :return:Null
    """
    print_meniu_cheltuieli_add()
    optiune = input("Introduceti o optiune: ")
    if optiune == '1':
        ziua = input("Introduceti ziua: ")
        suma = input("Introduceti suma: ")
        tipul = input("Introduceti tipul: ")
        event_cheltuiala = create_cheltuiala(ziua, suma, tipul)
        add_event_cheltuiala(cheltuieli,event_cheltuiala)
        print_succes()
    elif optiune == '2':
        ziua = input("Introduceti ziua: ")
        suma = input("Introduceti suma: ")
        tipul = input("Introduceti tipul: ")
        cheltuieli_add_update(cheltuieli,ziua,suma,tipul)
    else:
        print_invalid()

def cheltuieli_delete_zi(cheltuieli, zi):
    """
    Functie de stergere din lista dupa o zi data
    :param cheltuieli: lista data
    :param zi: ziua oferita de utilizator
    :return: Se returneaza lista cu elementele sterse dupa zi
    """
    #TODO: functie stergere
    cheltuieli_noi = []
    for event_cheltuieli in cheltuieli:
        if int(get_ziua_cheltuiala(event_cheltuieli)) != int(zi):
            cheltuieli_noi.append(event_cheltuieli)
    # print("Cheltuieli noi: ")
    # show_cheltuieli(cheltuieli_noi)
    return cheltuieli_noi

def cheltuieli_delete_zile(cheltuieli, zi1 , zi2):
    """
    Functie de stergere dupa 2 zile oferite de catre utilizator , in care se sterg elemente dupa
    2 zile date
    :param cheltuieli: lista data
    :param zi1: ziua 1 oferita de catre utilizator
    :param zi2: ziua 2 oferita de catre utilizator
    :return: lista cu elementele sterse
    """
    cheltuieli_noi = []
    for event_cheltuieli in cheltuieli:
        if int(get_ziua_cheltuiala(event_cheltuieli)) < int(zi1) or int(get_ziua_cheltuiala(event_cheltuieli)) > int(zi2):
            cheltuieli_noi.append(event_cheltuieli)
    # print("Cheltuieli noi: ")
    # show_cheltuieli(cheltuieli_noi)
    return cheltuieli_noi

def cheltuieli_delete_tipul(cheltuieli,tipul):
    """
    Functie care sterge elemente din lista dupa tipul dat
    :param cheltuieli: lista oferita default
    :param tipul: tipul introdus de catre utilizator
    :return: Lista cu elementele sterse in fuctie de parametrul tipul
    """
    cheltuieli_noi = []
    for event_cheltuieli in cheltuieli:
        if get_tipul_cheltuiala(event_cheltuieli) != tipul:
            cheltuieli_noi.append(event_cheltuieli)
    # print("Cheltuieli noi: ")
    # show_cheltuieli(cheltuieli_noi)
    return cheltuieli_noi

def cheltuieli_delete(cheltuieli):
    """
    Functia main de stergere a elementelor din lista
    in care se pot pune optiunile si se vor apela functile
    de stergere pentru o zi data , stergere pentru 2 zile date
    si stergere dupa un tip dat
    :param cheltuieli: lista oferita
    :return: Null
    """
    print_meniu_cheltuieli_delete()
    optiune = input("Introduceti o optiune: ")
    if optiune == '1':
        ziua = input("Introduceti ziua: ")
        cheltuieli = cheltuieli_delete_zi(cheltuieli,ziua)
        print_succes_delete()
        return cheltuieli
    elif optiune == '2':
        ziua1 = input("Introduceti ziua1: ")
        ziua2 = input("Introduceti ziua2: ")
        cheltuieli = cheltuieli_delete_zile(cheltuieli,ziua1,ziua2)
        print_succes_delete()
        return cheltuieli
    elif optiune == '3':
        tipul = input("Introduceti tipul: ")
        cheltuieli = cheltuieli_delete_tipul(cheltuieli,tipul)
        print_succes_delete()
        return cheltuieli
    else:
        print_invalid()

def cheltuieli_cautari_suma(cheltuieli, suma):
    """
    Functie de cautare in lista dupa o suma data
    se vor cauta si se vor afisa date in functie de suma introdusa
    de la tastatura de catre utilizator
    :param cheltuieli: lista data
    :param suma: suma oferita de catre utilizator
    :return: Se va returna numarul de elemente afisate
    """
    # print("Am intrat in funnctie")
    list_afis = []
    i = -1
    for curent_cheltuieli in cheltuieli:
        if int(get_suma_cheltuiala(curent_cheltuieli)) > int(suma):
            event_afis = create_cheltuiala(get_ziua_cheltuiala(curent_cheltuieli),get_suma_cheltuiala(curent_cheltuieli),get_tipul_cheltuiala(curent_cheltuieli))
            list_afis.append(event_afis)
    return list_afis

def cheltuieli_cautari_zi_suma(cheltuieli, zi, suma):
    """
    Se vor afisa toate cheltuielile efectuate inainte
    de o zi data si mai mici decat o suma introdusa
    de catre utilizator
    :param cheltuieli: lista
    :param zi: ziua introdusa de utilizator
    :param suma: suma data de catre utilizator
    :return: Se vor returna numarul de elemente afisate
    """
    i = -1
    list_afis = []
    for curent_cheltuieli in cheltuieli:
        if int(get_suma_cheltuiala(curent_cheltuieli)) < int(suma) and int(get_ziua_cheltuiala(curent_cheltuieli) < int(zi)):
            event_afis = create_cheltuiala(get_ziua_cheltuiala(curent_cheltuieli), get_suma_cheltuiala(curent_cheltuieli),
                                           get_tipul_cheltuiala(curent_cheltuieli))
            list_afis.append(event_afis)
    return list_afis
def cheltuieli_cautari_tip(cheltuieli, tipul):
    """
    Functie pentru cautare in functie de tipul introdus de catre utilizator
    :param cheltuieli: lista
    :param tipul: tipul introdus de catre utilizator
    :return: Se vor returna numarul de elemente afisate
    """
    i = -1
    list_afis = []
    for curent_cheltuieli in cheltuieli:
        if get_tipul_cheltuiala(curent_cheltuieli) == tipul:
            event_afis = create_cheltuiala(get_ziua_cheltuiala(curent_cheltuieli), get_suma_cheltuiala(curent_cheltuieli),
                                           get_tipul_cheltuiala(curent_cheltuieli))
            list_afis.append(event_afis)
    return list_afis


def cheltuieli_cautari(cheltuieli):
    """
    Functia main in care se vor apela functile
    de cautare
    :param cheltuieli: lista
    :return: Null
    """
    print_meniu_cheltuieli_cautari()
    afisare_lista = []
    optiune = input("Introduceti o optiune: ")
    if optiune == '1':
        suma = input("Introduceti suma: ")
        afisare_lista = cheltuieli_cautari_suma(cheltuieli, suma)
        show_cheltuieli(afisare_lista)
    elif optiune == '2':
        ziua = input("Introduceti ziua: ")
        suma = input("Introduceti suma: ")
        afisare_lista = cheltuieli_cautari_zi_suma(cheltuieli, ziua , suma)
        show_cheltuieli(afisare_lista)
    elif optiune == '3':
        tipul = input("Introduceti tipul: ")
        afisare_lista = cheltuieli_cautari_tip(cheltuieli,tipul)
        show_cheltuieli(afisare_lista)
    else:
        print_invalid()

def cheltuieli_rapoarte_sumtotal(cheltuieli,tipul):
    """
    Functia de rapoarte in care se vor returna
    suma totala pentru un anumit de tip introdus
    de la tastatura
    :param cheltuieli: lista
    :param tipul: tipul oferit de catre utilizator
    :return: Se va returna suma totala pentru un tip de data dat
    """
    sum_total = 0
    for curent_cheltuieli in cheltuieli:
        if get_tipul_cheltuiala(curent_cheltuieli) == tipul:
            sum_total = sum_total + int(get_suma_cheltuiala(curent_cheltuieli))
    return sum_total

def cheltuieli_rapoarte_zisumax(cheltuieli):
    """
    Functia care determina suma maxima pentru o zi oferita
    :param cheltuieli: lista
    :return: Se returneaza ziua in care a fost suma maxima
    """
    sum_max = 0
    ziulica = 0
    for curent_cheltuieli in cheltuieli:
        if int(get_suma_cheltuiala(curent_cheltuieli)) > int(sum_max):
            sum_max = int(get_suma_cheltuiala(curent_cheltuieli))
            ziulica = get_ziua_cheltuiala(curent_cheltuieli)
    return ziulica

def cheltuieli_rapoarte_suma(cheltuieli,suma):
    """
    Functie de rapoarte in care
    se vor afisa elementele din lista pentru o suma data
    :param cheltuieli: lista
    :param suma: suma oferita de catre utilizator
    :return: Null
    """
    i = -1
    list_afis = []
    for curent_cheltuieli in cheltuieli:
        if int(get_suma_cheltuiala(curent_cheltuieli)) == int(suma):
            i = i + 1
            event_afis = create_cheltuiala(get_ziua_cheltuiala(curent_cheltuieli),
                                           get_suma_cheltuiala(curent_cheltuieli),
                                           get_tipul_cheltuiala(curent_cheltuieli))
            list_afis.append(event_afis)
    return list_afis

def exista_tipul(vector , tip):
    """
    Functie in care se verifica daca exista un element
    intr-o lista
    :param vector: lista
    :param tip: tipul pe care il cautam in lista
    :return: Adevarat sau Fals in functie de prezenta tipului in vector
    """
    for el in vector:
        if el == tip:
            return True
    return False

def cheltuieli_rapoarte_sortate_tip(cheltuieli):
    """
    Functie de sortare a elementelor din lista dupa tipul dat
    :param cheltuieli: lista
    :return: Null
    """
    #Vom crea un vector in care vom adauga toate tipurile de cheltuieli pe care le-am inregistrat
    tipul = []
    for curent_cheltuieli in cheltuieli:
        if exista_tipul(tipul,get_tipul_cheltuiala(curent_cheltuieli)) == False:
            tipul.append(get_tipul_cheltuiala(curent_cheltuieli))
    i = -1
    list_afis = []
    for curent_tipul in tipul:
        for curent_cheltuieli in cheltuieli:
            if curent_tipul == get_tipul_cheltuiala(curent_cheltuieli):
                i = i + 1
                event_afis = create_cheltuiala(get_ziua_cheltuiala(curent_cheltuieli),
                                               get_suma_cheltuiala(curent_cheltuieli),
                                               get_tipul_cheltuiala(curent_cheltuieli))
                list_afis.append(event_afis)
    return list_afis
def cheltuieli_rapoarte(cheltuieli):
    """
    Functia main pentru rapoarte in care vom apela functile specifice
    :param cheltuieli: lista
    :return: Null
    """
    print_meniu_cheltuieli_rapoarte()
    optiune = input("Introduceti o optiune: ")
    if optiune == '1':
        tipul = input("Introduceti tipul:")
        print("Suma totala pentru un anumit tip de cheltuiala este: " + str(cheltuieli_rapoarte_sumtotal(cheltuieli,tipul)))
    elif optiune == '2':
        print("Ziua in care suma cheltuita este maxima este: " + str(cheltuieli_rapoarte_zisumax(cheltuieli)))
    elif optiune == '3':
        suma = input("Introduceti suma: ")
        list_afis = []
        list_afis = cheltuieli_rapoarte_suma(cheltuieli,suma)
        show_cheltuieli(list_afis)
    elif optiune == '4':
        list_afis = []
        list_afis = cheltuieli_rapoarte_sortate_tip(cheltuieli)
        show_cheltuieli(list_afis)
    else:
        print_invalid()

def cheltuieli_filtrare_tip(cheltuieli, tipul):
    """
    Functie de filtrare pentru un tip dat
    :param cheltuieli: lista
    :param tipul: tipul de data introdus de la tastatura
    :return: Numarul de elemente afisate
    """
    i = -1
    list_afis = []
    for curent_cheltuieli in cheltuieli:
        if get_tipul_cheltuiala(curent_cheltuieli) != tipul:
            i = i + 1
            event_afis = create_cheltuiala(get_ziua_cheltuiala(curent_cheltuieli),
                                           get_suma_cheltuiala(curent_cheltuieli),
                                           get_tipul_cheltuiala(curent_cheltuieli))
            list_afis.append(event_afis)
    return list_afis

def cheltuieli_filtrare_suma(cheltuieli, suma):
    i = -1
    for curent_cheltuieli in cheltuieli:
        if int(get_suma_cheltuiala(curent_cheltuieli)) >= int(suma):
            i = i + 1
            print("Cr." + str(i + 1), " Ziua: " + str(get_ziua_cheltuiala(curent_cheltuieli)),
                  " Suma: " + str(get_suma_cheltuiala(curent_cheltuieli)),
                  " Tipul: " + get_tipul_cheltuiala(curent_cheltuieli))
    return i+1

def cheltuieli_filtrare(cheltuieli):
    """
    Functia main pentru filtrare
    :param cheltuieli: lista
    :return: Null
    """
    print_meniu_cheltuieli_filtrare()
    optiune = input("Introduceti o optiune: ")
    if optiune == '1':
        tip = input("Introduceti tipul: ")
        list_afis = []
        list_afis = cheltuieli_filtrare_tip(cheltuieli,tip)
        show_cheltuieli(list_afis)
    elif optiune == '2':
        suma = input("Introduceti suma: ")
        cheltuieli_filtrare_suma(cheltuieli,suma)
    else:
        print_invalid()

#
# -------------------------------------START----------------------------------
def start():
    cheltuieli = []
    cheltuieli = default_cheltuieli(cheltuieli)
    while True:
        print_meniu()
        optiune = input("Introduceti o optiune: ")
        if optiune == '1':
            cheltuieli_add(cheltuieli)
        elif optiune == '2':
            cheltuieli = cheltuieli_delete(cheltuieli)
        elif optiune == '3':
            cheltuieli_cautari(cheltuieli)
        elif optiune == '4':
            cheltuieli_rapoarte(cheltuieli)
        elif optiune == '5':
            cheltuieli_filtrare(cheltuieli)
        elif optiune == '6':
            pass
            # print_valid()
        elif optiune == 'A':
            show_cheltuieli(cheltuieli)
            # pass
            # print_valid()
        elif optiune == 'C':
            # print_valid()
            return
        else:
            print_invalid()

# -------------------------------------TESTE----------------------------------

def test_cheltuieli_add():
    test = []
    event_test = create_cheltuiala(20,7000,'Mancare')
    add_event_cheltuiala(test,event_test)
    assert (len(test) == 1)
    assert get_tipul_cheltuiala(event_test) == 'Mancare'
    assert get_suma_cheltuiala(event_test) == 7000
    assert get_ziua_cheltuiala(event_test) == 20

    cheltuieli_add_update(test,20,90,'Mancare')
    assert get_tipul_cheltuiala(event_test) == 'Mancare'
    assert get_suma_cheltuiala(event_test) == 90
    assert get_ziua_cheltuiala(event_test) == 20

def test_cheltuieli_delete():
    test = []
    event_test = create_cheltuiala(15,800,'Masini')
    add_event_cheltuiala(test,event_test)
    event_test = create_cheltuiala(18,10,'Chirie')
    add_event_cheltuiala(test,event_test)

    test = cheltuieli_delete_zi(test,15)
    assert (len(test)==1)
    test = cheltuieli_delete_zi(test,18)
    assert (len(test)==0)

    test = default_cheltuieli(test)
    assert (len(test)==9)
    test = cheltuieli_delete_zile(test,1,30)
    assert (len(test)==0)

    test = default_cheltuieli(test)
    assert (len(test)==9)
    test = cheltuieli_delete_tipul(test,'Masina')
    assert (len(test)==6)

# cheltuieli_cautari_tip()
# cheltuieli_cautari_zi_suma()
# cheltuieli_cautari_suma()

def test_cheltuieli_cautari():
    test = []
    event_test = create_cheltuiala(20,500,'Masini')
    add_event_cheltuiala(test,event_test)
    event_test = create_cheltuiala(18, 10, 'Chirie')
    add_event_cheltuiala(test,event_test)

    afisare_lista = []
    afisare_lista = cheltuieli_cautari_suma(test,30)
    assert len(afisare_lista) == 1
    afisare_lista = cheltuieli_cautari_suma(test,5)
    assert len(afisare_lista) == 2
    afisare_lista = cheltuieli_cautari_tip(test,'Masini')
    assert len(afisare_lista) == 1
    afisare_lista = cheltuieli_cautari_tip(test,'Mancare')
    afisare_lista = cheltuieli_cautari_tip(test, 'Mancare')
    assert len(afisare_lista) == 0
    afisare_lista = cheltuieli_cautari_zi_suma(test, 19, 20)
    assert len(afisare_lista) == 1
    afisare_lista = cheltuieli_cautari_zi_suma(test, 30, 200)
    assert len(afisare_lista) == 1

# cheltuieli_rapoarte_suma()
# cheltuieli_rapoarte_zisumax()
# cheltuieli_rapoarte_sumtotal()
# cheltuieli_rapoarte_sortate_tip()

def test_cheltuieli_rapoarte():
    test = []
    test = default_cheltuieli(test)
    assert (int(cheltuieli_rapoarte_sumtotal(test,'Masina')) == 40800)
    assert (int(cheltuieli_rapoarte_zisumax(test)) == 3)

# cheltuieli_filtrare_suma()
# cheltuieli_filtrare_tip()

def test_cheltuieli_filtrare():
    test = []
    test = default_cheltuieli(test)
    assert (int(cheltuieli_filtrare_tip(test,'Masina')) == 6)
    assert (int(cheltuieli_filtrare_suma(test,500)) == 4)

# cheltuieli_rapoarte_sumtotal()
# cheltuieli_rapoarte_zisumax()
# cheltuieli_rapoarte_suma()
# cheltuieli_rapoarte_sortate_tip()


def test_cheltuieli_rapoarte():
    test = []
    test = default_cheltuieli(test)
    list_afis = []
    assert int(cheltuieli_rapoarte_sumtotal(test,'Masina')) == 40800
    # list_afis = cheltuieli_rapoarte_zisumax()
    assert int(cheltuieli_rapoarte_zisumax(test)) == 3
    list_afis = cheltuieli_rapoarte_suma(test,200)
    assert int(len(list_afis)) == 2
    # list_afis = cheltuieli_rapoarte_sortate_tip()


def TEST():
    test_cheltuieli_add()
    test_cheltuieli_delete()
    test_cheltuieli_cautari()
    test_cheltuieli_rapoarte()
    # test_cheltuieli_filtrare()
# print(colored("TEST: ","red"))
TEST()

start()