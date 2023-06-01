package aplicatie.aplicatiefx.gui;

import aplicatie.AngajatService;
import aplicatie.ManagerService;
import aplicatie.model.Angajat;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.control.Alert;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;

public class SignController {
    private AngajatService angajatService;
    private ManagerService managerService;

    @FXML
    private TextField usernameField;
    @FXML
    private TextField passwordField;
    @FXML
    private TextField numeField;
    @FXML
    private TextField prenumeField;
    @FXML
    private TextField varstaField;
    Parent mainAplicatieParent;
    Parent p2;
    private Stage myStage;

    public void setParent(Parent p, Parent p2){
        mainAplicatieParent = p;
        this.p2 = p2;
    }

    public void setStage(Stage stage){
        this.myStage = stage;
    }
    public void setService(AngajatService angajatService, ManagerService managerService){
        this.angajatService = angajatService;
        this.managerService = managerService;
    }

    @FXML
    public void handleBackButton(ActionEvent actionEvent) throws IOException {
        System.out.println("Back button pressed");
        myStage.show();
        ((Node)(actionEvent.getSource())).getScene().getWindow().hide();
    }


    @FXML
    public void handleSignButton(ActionEvent actionEvent){
        System.out.println("Sign in button pressed");
        String nume = numeField.getText();
        String prenume = prenumeField.getText();
        int varsta = Integer.parseInt(varstaField.getText());
        String username = usernameField.getText();
        String password = passwordField.getText();
        Angajat angajat = new Angajat(username,password,nume,prenume,varsta);
        if(angajatService.save(angajat) != null){
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Succes");
            alert.setHeaderText("Saved");
            alert.showAndWait();
        }
        else{
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Error");
            alert.setHeaderText("Save failure");
            alert.setContentText("Wrong username or password");
            alert.showAndWait();
        }
        myStage.show();
        ((Node)(actionEvent.getSource())).getScene().getWindow().hide();
    }

}
