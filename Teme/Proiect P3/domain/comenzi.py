from domain.get import *
from utils.prints import *

def show_cheltuieli(cheltuieli):
    # print("Am intrat in funnctie")
    for i , curent_cheltuieli in enumerate(cheltuieli):
        print("Cr." + str(i+1)," Ziua: " + str(get_ziua_cheltuiala(curent_cheltuieli)), " Suma: " + str(get_suma_cheltuiala(curent_cheltuieli)), " Tipul: " + get_tipul_cheltuiala(curent_cheltuieli))

def create_cheltuiala(ziua, suma, tipul):
    return {'ziua': ziua,'suma': suma,'tipul': tipul}

def add_event_cheltuiala(cheltuiala,event_cheltuiala):
    cheltuiala.append(event_cheltuiala)
    return cheltuiala

def pop_event_cheltuiala(cheltuieli):
    cheltuieli_noi = []
    for event_cheltuieli in cheltuieli:
            cheltuieli_noi.append(event_cheltuieli)
    # print("Cheltuieli noi: ")
    # show_cheltuieli(cheltuieli_noi)
    cheltuieli_noi.pop()
    return cheltuieli_noi

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
            cheltuieli[i]['suma'] = suma
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
    list_afis = []
    for curent_cheltuieli in cheltuieli:
        if int(get_suma_cheltuiala(curent_cheltuieli)) >= int(suma):
            i = i + 1
            event_afis = create_cheltuiala(get_ziua_cheltuiala(curent_cheltuieli),
                                           get_suma_cheltuiala(curent_cheltuieli),
                                           get_tipul_cheltuiala(curent_cheltuieli))
            list_afis.append(event_afis)
    return list_afis

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
        list_afis = []
        list_afis = cheltuieli_filtrare_suma(cheltuieli,suma)
        show_cheltuieli(list_afis)
    else:
        print_invalid()

def cheltuieli_undo_update(cheltuieli_invs,cheltuieli):
    cheltuieli_invs.append(cheltuieli[:])
    return cheltuieli_invs

def cheltuieli_undo(cheltuieli,cheltuieli_invs):
    print_meniu_cheltuieli_undo()
    lungime = int(len(cheltuieli_invs))
    if lungime >= 2:
        cheltuieli = cheltuieli_invs[lungime-2]
        print_undo()
    else:
        print(colored("Nu se poate realiza operatia de undo","red"))

    return cheltuieli
