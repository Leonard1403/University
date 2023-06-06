package aplicatie.aplicatiefx.gui;

import aplicatie.AngajatService;
import aplicatie.ComandaService;
import aplicatie.ManagerService;
import aplicatie.model.Comanda;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;

import java.util.ArrayList;
import java.util.List;

public class AngajatController {
    private AngajatService angajatService;
    private ManagerService managerService;
    private ComandaService comandaService;

    ObservableList<Comanda> model = FXCollections.observableArrayList();
    @FXML
    TableView<Comanda> tableView;

    @FXML
    TableColumn<Comanda, String> tableColumnNume;
    @FXML
    TableColumn<Comanda, String> tableColumnDenumire;
    @FXML
    TableColumn<Comanda, Integer> tableColumnGreutate;
    public void setService(AngajatService angajatService, ManagerService managerService, ComandaService comandaService) {
        this.angajatService = angajatService;
        this.managerService = managerService;
        this.comandaService = comandaService;
        initModel();
    }

    @FXML
    public void initialize(){
        tableColumnNume.setCellValueFactory(new PropertyValueFactory<Comanda, String>("nume"));
        tableColumnDenumire.setCellValueFactory(new PropertyValueFactory<Comanda, String>("denumire"));
        tableColumnGreutate.setCellValueFactory(new PropertyValueFactory<Comanda, Integer>("greutate"));
        tableView.setItems(model);
    }

    private void initModel(){
        Iterable<Comanda> comenzi = comandaService.findAll();
        List<Comanda> comandaList = new ArrayList<>();
        for(Comanda comanda: comenzi){
            if(comanda.getTipString().equals("InProgres"))
                comandaList.add(comanda);
        }
        model.setAll(comandaList);
    }

    @FXML
    public void buttonAccept(){
        
    }
}
