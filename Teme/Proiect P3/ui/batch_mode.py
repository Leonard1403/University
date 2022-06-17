from ui.console import *
from domain.comenzi import *

def delimitare(prop):
    comenzi = []
    comenzi = prop.split(";")
    return comenzi

def start_batch_mode():
    cheltuieli = []
    cheltuieli_invs = []
    cheltuieli = default_cheltuieli(cheltuieli)
    cheltuieli_invs = cheltuieli_undo_update(cheltuieli_invs, cheltuieli[:])

    while True:
        print("Comenzi: add , show , modif , delete , undo , exit")
        prop = input("Comanda: ")
        cmd = delimitare(prop)
        # print(cmd)
        for el in cmd:
            comanda = el.split()
            executa = comanda[0]
            print("Se executa comanda: " + el)
            if executa == 'add':
                try:
                    ziua = comanda[1]
                    suma = comanda[2]
                    tipul = comanda[3]
                    event_cheltuiala = create_cheltuiala(ziua,suma,tipul)
                    add_event_cheltuiala(cheltuieli,event_cheltuiala)
                    cheltuieli_invs = cheltuieli_undo_update(cheltuieli_invs, cheltuieli)
                except:
                    print("Nu sunt destule date")
            elif executa == 'show':
                show_cheltuieli(cheltuieli)
            elif executa == 'modif':
                try:
                    ziua = comanda[1]
                    suma = comanda[2]
                    tip = comanda[3]
                    cheltuieli_add_update(cheltuieli,ziua,suma,tip)
                    cheltuieli_invs = cheltuieli_undo_update(cheltuieli_invs, cheltuieli)
                except:
                    print("Nu sunt destule date")
            elif executa == 'delete':
                try:
                    ziua = comanda[1]
                    cheltuieli = cheltuieli_delete_zi(cheltuieli,ziua)
                    cheltuieli_invs = cheltuieli_undo_update(cheltuieli_invs, cheltuieli)
                except:
                    print("Nu sunt destule date")
            elif executa == 'undo':
                lungime = int(len(cheltuieli_invs))
                if lungime >= 2:
                    cheltuieli = cheltuieli_invs[lungime - 2]
                    cheltuieli_invs = pop_event_cheltuiala(cheltuieli_invs)
                    print_undo()
                else:
                    print(colored("Nu se poate realiza operatia de undo", "red"))
            elif executa == 'exit':
                return
            else:
                print_invalid()

