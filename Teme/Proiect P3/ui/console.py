# -------------------------------------FUNCTII--------------------------------

from domain.generate import *
from domain.comenzi import *

# -------------------------------------START----------------------------------
def start():
    cheltuieli = []
    cheltuieli_invs = []
    cheltuieli = default_cheltuieli(cheltuieli)
    cheltuieli_invs = cheltuieli_undo_update(cheltuieli_invs,cheltuieli[:])

    while True:
        print_meniu()
        optiune = input("Introduceti o optiune: ")
        if optiune == '1':
            cheltuieli_add(cheltuieli)
            cheltuieli_invs = cheltuieli_undo_update(cheltuieli_invs,cheltuieli)
        elif optiune == '2':
            cheltuieli = cheltuieli_delete(cheltuieli)
            cheltuieli_invs = cheltuieli_undo_update(cheltuieli_invs,cheltuieli)
        elif optiune == '3':
            cheltuieli_cautari(cheltuieli)
            # cheltuiala_invs = add_event_cheltuiala(cheltuieli_invs, cheltuieli)
        elif optiune == '4':
            cheltuieli_rapoarte(cheltuieli)
            # cheltuiala_invs = add_event_cheltuiala(cheltuieli_invs,cheltuieli)
        elif optiune == '5':
            cheltuieli_filtrare(cheltuieli)
        elif optiune == '6':
            cheltuieli = cheltuieli_undo(cheltuieli,cheltuieli_invs)
            lungime = int(len(cheltuieli_invs))
            if lungime >= 2:
                cheltuieli_invs = pop_event_cheltuiala(cheltuieli_invs)

        elif optiune == 'A':
            show_cheltuieli(cheltuieli)
            # pass
            # print_valid()
        elif optiune == 'C':
            # print_valid()
            return
        else:
            print_invalid()

        # print("Lista undo: ")
        # lungime = int(len(cheltuieli_invs))
        # for i in range(0,lungime):
        #     print(i)
        #     show_cheltuieli(cheltuieli_invs[i])