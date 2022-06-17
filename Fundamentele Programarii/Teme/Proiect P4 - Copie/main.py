from termcolor import colored

from domain.validators import ClientiValidator
from domain.validators import CartiValidator
from domain.validators import InchiriereValidator
from ui.console_file import ConsoleFile
from repository.carti import CartiFileRepository
from repository.clienti import ClientiFileRepository
from repository.inchirieri import InchirieriFileRepository

# from repository.library_repo import InMemoryRepository

from repository.carti import CartiMemoryRepository
from repository.clienti import ClientiMemoryRepository
from repository.inchirieri import InchirieriMemoryRepository

from service.carti_service import CartiService
from service.clienti_service import ClientiService
from service.inchirieri import InchirieriService

from ui.console import Console

def Start():
    while True:
        print("1.Aplicatia va rula in memorie")
        print("2.Aplicatia va rula cu fisiere")
        print("3.Exit")
        try:
            ans = int(input("In ce mod doriti sa folositi aplicatia ?: "))
        except ValueError:
            print(colored('Va rugam introduceti 1 sau 2','red'))
        if ans == 1:
            carti_repo = CartiMemoryRepository()
            carti_vali = CartiValidator()
            carti_srv = CartiService(carti_repo,carti_vali)

            clienti_repo = ClientiMemoryRepository()
            clienti_vali = ClientiValidator()
            clienti_srv = ClientiService(clienti_repo,clienti_vali)

            inchirieri_repo = InchirieriMemoryRepository()
            inchirieri_vali = InchiriereValidator()
            inchiriere_srv = InchirieriService(inchirieri_repo,clienti_repo,carti_repo,inchirieri_vali)

            ui = Console(carti_srv, clienti_srv, inchiriere_srv)
            ui.show_ui()
        elif ans == 2:
            clienti_repo = ClientiFileRepository('data/clienti.txt')
            clienti_vali = ClientiValidator()
            clienti_srv = ClientiService(clienti_repo, clienti_vali)

            carti_repo = CartiFileRepository('data/carti.txt')
            carti_vali = CartiValidator()
            carti_srv = CartiService(carti_repo, carti_vali)

            inchirieri_repo = InchirieriFileRepository('data/inchirieri.txt', 'data/clienti.txt', 'data/carti.txt')
            inchirieri_vali = InchiriereValidator()
            inchiriere_srv = InchirieriService(inchirieri_repo, clienti_repo, carti_repo, inchirieri_vali)

            ui = ConsoleFile(carti_srv, clienti_srv, inchiriere_srv)
            ui.show_ui()
        elif ans == 3:
            return

Start()
