from repository.parcare_repo import InFileRepo
from service.parcare_service import ParcariService
from ui.console import Console

parcare_repo = InFileRepo('data/parcari.txt')
parcare_service = ParcariService(parcare_repo)

ui = Console(parcare_service)

ui.show_ui()