package com.example.social_network_gui_v2.controller;

import com.example.social_network_gui_v2.Main;
import com.example.social_network_gui_v2.domain.UserGUI;
import com.example.social_network_gui_v2.domain.validation.ValidationException;
import com.example.social_network_gui_v2.unused.MessageAlert;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;

import java.io.IOException;

import com.example.social_network_gui_v2.service.ServiceUserGUI;
import javafx.stage.Stage;
import com.example.social_network_gui_v2.domain.validation.UserValidator;
public class RegisterController {
    @FXML
    private Button register;
    @FXML
    private TextField usernameField;
    @FXML
    private PasswordField passwordField;

    private ServiceUserGUI service;
    private Stage dialogStage;
    public void setService(ServiceUserGUI service, Stage stage){
        this.service = service;
        this.dialogStage = stage;
    }

    public void RegisterButtonAction(ActionEvent evemt) throws IOException {
        System.out.println(usernameField.getText());
        System.out.println(passwordField.getText());
        System.out.println("Register button pressed");
//        service.getAll().forEach(System.out::println);
//            try{
//
//            } catch(Exception e) {
//                e.printStackTrace();
//            }

//            Main m = new Main();
//            m.changeScene("views/login-view.fxml");
        UserGUI user = service.findUsername(usernameField.getText());
        UserValidator val = new UserValidator();
//        try {
//            val.validate(user);


        if (!user.getUsername().equals("_")) {
            MessageAlert.showErrorMessage(null, "Username-ul exista deja");
        } else if (passwordField.getText().equals("")) {
            MessageAlert.showErrorMessage(null, "Parola trebuie sa contina caractere");
        } else {
            try{
            service.save(usernameField.getText(), passwordField.getText());
            dialogStage.close();
            }
            catch(ValidationException e){
                MessageAlert.showErrorMessage(null, "Username-ul invalid");
            }
        }
//        catch(ValidationException e){
//            MessageAlert.showErrorMessage(null, "S-a detectat o problema, incercati sa modificati user sau parola");
//            e.getMessage();
    }
}
