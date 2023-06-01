package aplicatie.aplicatiefx.gui;

import aplicatie.AngajatService;
import aplicatie.ManagerService;

public class AngajatController {
    private AngajatService angajatService;
    private ManagerService managerService;
    public void setService(AngajatService angajatService, ManagerService managerService) {
        this.angajatService = angajatService;
        this.managerService = managerService;
    }
}
