package com.example.social_network_gui_v2.controller;

import com.example.social_network_gui_v2.Main;
import com.example.social_network_gui_v2.domain.UserGUI;
import com.example.social_network_gui_v2.domain.validation.ValidationException;
import com.example.social_network_gui_v2.service.ServiceFriendshipGUI;
import com.example.social_network_gui_v2.service.ServiceUserGUI;
import com.example.social_network_gui_v2.unused.MessageAlert;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.GridPane;
import javafx.scene.text.Text;
import javafx.stage.Modality;
import javafx.stage.Stage;

import java.io.IOException;

public class LoginController {
    @FXML
    private TextField usernameField;
    @FXML
    private PasswordField passwordField;

    @FXML
    public void initialize(){
    }

    private ServiceUserGUI service;
    private ServiceFriendshipGUI serviceFriendshipGUI;
    public void setService(ServiceUserGUI service,ServiceFriendshipGUI serviceFriendshipGUI){
        this.service = service;
        this.serviceFriendshipGUI = serviceFriendshipGUI;
    }

    @FXML
    public void SigninButtonAction() throws IOException {
        System.out.println("Sign in button pressed");
//        Main m = new Main();
//        m.changeScene("views/register-view.fxml");
        try {
            FXMLLoader loader = new FXMLLoader(Main.class.getResource("views/register-view.fxml"));
//            loader.setLocation(Main.class.getResource("views/register-view.fxml"));

//            AnchorPane root = (AnchorPane) loader.load();

            GridPane rootLayout = (GridPane)loader.load();

            Stage registerStage = new Stage();
            registerStage.setTitle("Register");
            registerStage.initModality(Modality.WINDOW_MODAL);
//
            Scene scene = new Scene(rootLayout);
            registerStage.setScene(scene);

            RegisterController registerController = loader.getController();
            registerController.setService(service,registerStage);

            registerStage.show();
        }
        catch(IOException e){
            e.getMessage();
        }
    }

    @FXML
    public void LoginButtonAction(){
        try {
            System.out.println("Log in button pressed");
            System.out.println(usernameField.getText());
            System.out.println(passwordField.getText());
//            this.service.getAll().forEach(System.out::println);
            UserGUI user = service.findUsername(usernameField.getText());
//            System.out.println(user.getUsername() + " " + user.getPassword());
            //in cazul in care nu se gaseste un user cu acest nume se va crea un user cu caracterul _
            if(user.getUsername()=="_")
                MessageAlert.showErrorMessage(null,"Username nu exista");
            else if(user.getPassword().equals(passwordField.getText())){
//                System.out.println("intrat");
                FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("views/friends-views.fxml"));
                Scene scene = new Scene(fxmlLoader.load(), 630, 400);
                Stage stage = new Stage();
                stage.setTitle("Friends: " + user.getUsername());
                stage.setScene(scene);

                FriendsController friendsController = fxmlLoader.getController();
                friendsController.setFriendshipService(user,service,serviceFriendshipGUI);

//                serviceFriendshipGUI.getAll().forEach(System.out::println);

                stage.show();
            }
            else{
                MessageAlert.showErrorMessage(null,"Parola nu este corecta");
            }
        }
        catch(ValidationException e){
            e.getMessage();
        } catch (IOException e) {
            e.getMessage();
        }
    }
}
