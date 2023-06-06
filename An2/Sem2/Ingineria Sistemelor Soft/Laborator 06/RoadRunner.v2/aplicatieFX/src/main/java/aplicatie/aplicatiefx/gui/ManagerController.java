package aplicatie.aplicatiefx.gui;

import aplicatie.AngajatService;
import aplicatie.ComandaService;
import aplicatie.ManagerService;
import aplicatie.model.Angajat;
import aplicatie.model.Comanda;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;

import java.util.ArrayList;
import java.util.List;

public class ManagerController {
    AngajatService angajatService;
    ManagerService managerService;
    ComandaService comandaService;

    ObservableList<Angajat> modelAngajat = FXCollections.observableArrayList();
    ObservableList<Comanda> modelComanda = FXCollections.observableArrayList();
    @FXML
    TableView<Comanda> tableViewComenzi;
    @FXML
    TableColumn <Comanda, String> columnNumeComanda;
    @FXML
    TableColumn <Comanda,Integer> columnGreutateComanda;
    @FXML
    TableColumn<Comanda, String> columnTipComanda;

    @FXML
    TableView<Angajat> tableViewAngajati;
    @FXML
    TableColumn <Angajat, String> columnNumeAngajat;
    @FXML
    TableColumn <Angajat, String> columnPrenumeAngajat;

    public void setService(AngajatService angajatService, ManagerService managerService, ComandaService comandaService) {
        this.angajatService = angajatService;
        this.managerService = managerService;
        this.comandaService = comandaService;
        initModel();
    }

    @FXML
    public void initialize(){
        columnNumeComanda.setCellValueFactory(new PropertyValueFactory<Comanda, String>("nume"));
        columnGreutateComanda.setCellValueFactory(new PropertyValueFactory<Comanda,Integer>("greutate"));
        columnTipComanda.setCellValueFactory(new PropertyValueFactory<Comanda, String>("tip"));
        tableViewComenzi.setItems(modelComanda);

        columnNumeAngajat.setCellValueFactory(new PropertyValueFactory<Angajat, String>("nume"));
        columnPrenumeAngajat.setCellValueFactory(new PropertyValueFactory<Angajat, String>("prenume"));
        tableViewAngajati.setItems(modelAngajat);
    }
    private void initModel() {
        Iterable<Angajat> angajatIterable = angajatService.findAll();
        List<Angajat> angajatList= new ArrayList<>();

        Iterable<Comanda> comandaIterable = comandaService.findAll();
        List<Comanda> comandaList = new ArrayList<>();

        for(Angajat angajat: angajatIterable){
            angajatList.add(angajat);
        }
        for(Comanda comanda: comandaIterable){
            comandaList.add(comanda);
        }
        modelAngajat.setAll(angajatList);
        modelComanda.setAll(comandaList);
    }

    @FXML
    public void buttonAcceptComenzi() {
        Comanda selectedComanda = tableViewComenzi.getSelectionModel().getSelectedItem();

        if (selectedComanda != null && selectedComanda.getTipString().equals("Pending")) {
            selectedComanda.setTipString("InProgres");
            comandaService.update(selectedComanda);
            tableViewComenzi.refresh();
        }
    }


    @FXML
    public void buttonRefreshTables(){
        initModel();
    }

    @FXML
    public void buttonAcceptAngajati(){

    }
}
