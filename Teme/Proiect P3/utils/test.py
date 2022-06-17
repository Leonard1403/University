from ui.console import *
from domain.get import *


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
    assert (int(len(cheltuieli_filtrare_tip(test,'Masina'))) == 6)
    assert (int(len(cheltuieli_filtrare_suma(test,500))) == 4)

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

def test_cheltuieli_update():
    test_cheltuieli_invs = []
    test_cheltuieli = []
    test_cheltuieli = default_cheltuieli(test_cheltuieli)
    test_cheltuieli_invs = cheltuieli_undo_update(test_cheltuieli_invs, test_cheltuieli[:])
    assert int(len(test_cheltuieli_invs)) == 1
    test_event = create_cheltuiala(15,9000,'Masina')
    add_event_cheltuiala(test_cheltuieli,test_event)
    test_cheltuieli_invs = cheltuieli_undo_update(test_cheltuieli_invs,test_cheltuieli)
    assert int(len(test_cheltuieli_invs[0])) == int(len(test_cheltuieli_invs[1])) - 1
    assert int(len(test_cheltuieli_invs[0])) == 9
    assert int(len(test_cheltuieli_invs[1])) == 10

def TEST():
    test_cheltuieli_add()
    test_cheltuieli_delete()
    test_cheltuieli_cautari()
    test_cheltuieli_rapoarte()
    test_cheltuieli_filtrare()
    test_cheltuieli_update()
# print(colored("TEST: ","red"))