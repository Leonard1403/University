# -------------------------------------PRINT----------------------------------

from termcolor import colored

def print_invalid():
    print(colored("Optiune invalida", "red"))

def print_valid():
    print(colored("Optiune valida", "green"))

def print_meniu():
    print("1.Adauga o cheltuiala")
    print("2.Sterge")
    print("3.Cautari")
    print("4.Rapoarte")
    print("5.Filtrare")
    print("6.Undo")
    print("A.Afisare lista")
    print("C.Inchidere program")

def print_meniu_cheltuieli_add():
    print("1.Adauga o noua cheltuiala (se specifica ziua/suma/tipul)")
    print("2.Actualizeaza o cheltuiala(se specifica ziua/suma/tipul)")

def print_meniu_cheltuieli_delete():
    print("1.Sterge toate cheltuielile pentru o zi data")
    print("2.Sterge cheltuielile pentru un interval de timp(zi inceput-zi sfarsit")
    print("3.Sterge toate cheltuielile de un anumit tip")

def print_meniu_cheltuieli_cautari():
    print("1.Tipareste toate cheltuielile mai mari decat o suma data")
    print("2.Tipareste toate cheltuielile efectuate inainte de o zi data si mai mici decat o suma")
    print("3.Tipareste toate cheltuielile de un anumit tip")

def print_meniu_cheltuieli_rapoarte():
    print("1.Tipareste suma totala pentru un anumit tip de cheltuiala")
    print("2.Gaseste ziua in care suma cheltuita este maxima")
    print("3.Tipareste toate cheltuielile ce au o anumita suma")
    print("4.Tipareste cheltuielile sortate dupa tip")

def print_meniu_cheltuieli_filtrare():
    print("1.Elimina toate cheltuielile de un anumit tip")
    print("2.Elimina toate cheltuielile mai mici decat o suma data")

def print_succes_delete():
    print(colored("Elementele din lista au fost sterse cu succes", "green"))

def print_succes():
    print(colored("Cheltuiala a fost adaugata cu succes","green"))
