package aplicatie.aplicatiefx.gui;

import aplicatie.AngajatService;
import aplicatie.ManagerService;
import aplicatie.model.Angajat;
import aplicatie.model.Manager;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;

public class LoginController {

    private AngajatService angajatService;
    private ManagerService managerService;

    Parent mainAplicatieParent;
    private Stage myStage;
    @FXML
    private TextField usernameField;
    @FXML
    private TextField passwordField;

    public void setParentSign(Parent p){
        System.out.println("ParentSign seted");
        mainAplicatieParent = p;
    }
    public void setService(AngajatService angajatService, ManagerService managerService){
        this.angajatService = angajatService;
        this.managerService = managerService;
    }
    public void setStage(Stage stage){
        this.myStage = stage;
    }

    @FXML
    public void handleLoginButton(ActionEvent actionEvent) throws IOException {
        System.out.println("Login button pressed");
        String username = usernameField.getText();
        String password = passwordField.getText();
        Manager manager = managerService.findOne(username,password);
        Angajat angajat = angajatService.findOne(username,password);

        if(angajat == null && manager != null){
            System.out.println("It's a manager");

            FXMLLoader managerLoader = new FXMLLoader(
                    getClass().getClassLoader().getResource("manager.fxml")
            );
            Parent managerParent = managerLoader.load();
            ManagerController managerController = managerLoader.<ManagerController>getController();
            managerController.setService(angajatService, managerService);

            Stage managerStage = new Stage();
            managerStage.setTitle("Manager");
            managerStage.setScene(new Scene(managerParent));
            managerStage.show();
            ((Node)(actionEvent.getSource())).getScene().getWindow().hide();
        }
        else if(manager == null && angajat != null){
            System.out.println("It's a customer");

            FXMLLoader angajatLoader = new FXMLLoader(
                    getClass().getClassLoader().getResource("angajat.fxml")
            );
            Parent angajatParent = angajatLoader.load();
            AngajatController angajatController = angajatLoader.<AngajatController>getController();
            angajatController.setService(angajatService, managerService);

            Stage angajatStage = new Stage();
            angajatStage.setTitle("Manager");
            angajatStage.setScene(new Scene(angajatParent));
            angajatStage.show();
            ((Node)(actionEvent.getSource())).getScene().getWindow().hide();
        }
        else{
            System.out.println("U are wrong");
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Error");
            alert.setHeaderText("Authentication failure");
            alert.setContentText("Wrong username or password");
            alert.showAndWait();
        }
    }
    @FXML
    public void handleSignButton(ActionEvent actionEvent) throws IOException {
        System.out.println("Sign in button pressed");
        myStage.show();
        ((Node)(actionEvent.getSource())).getScene().getWindow().hide();
    }

}
