from repository.vacanta_repo import InFileRepo
from service.vacanta_service import VacanteService
from ui.console import Console
from repository.vacanta_repo import Teste

vacante_repo = InFileRepo('data/vacante.txt')
vacante_service = VacanteService(vacante_repo)

test = Teste('repository/test.txt',vacante_repo)
test.TEST()

ui = Console(vacante_service)

ui.show_ui()
