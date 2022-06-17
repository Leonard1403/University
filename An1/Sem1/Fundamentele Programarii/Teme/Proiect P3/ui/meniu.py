from ui.batch_mode import *
from ui.console import start

def meniu():
    while True:
        print("In ce mod doriti sa intrati?:")
        print("1.Normal")
        print("2.Batch Mode")
        print("3.Iesire din program")
        comanda = int(input("Introduceti optiunea: "))
        if comanda == 1:
            start()
        elif comanda == 2:
            start_batch_mode()
        elif comanda == 3:
            return
        else:
            print_invalid()