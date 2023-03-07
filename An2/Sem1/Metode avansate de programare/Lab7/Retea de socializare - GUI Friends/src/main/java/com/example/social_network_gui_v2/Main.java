package com.example.social_network_gui_v2;

import com.example.social_network_gui_v2.controller.LoginController;
import com.example.social_network_gui_v2.controller.RegisterController;
import com.example.social_network_gui_v2.domain.Friendship;
import com.example.social_network_gui_v2.domain.Tuple;
import com.example.social_network_gui_v2.domain.UserGUI;
import com.example.social_network_gui_v2.domain.validation.UserValidator;

import com.example.social_network_gui_v2.repository.database.FriendshipDbRepositoryGUI;
import com.example.social_network_gui_v2.service.ServiceFriendshipGUI;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

import com.example.social_network_gui_v2.repository.Repository;
import com.example.social_network_gui_v2.repository.database.UserDbRepositoryGUI;
import com.example.social_network_gui_v2.service.ServiceUserGUI;

import java.io.IOException;

public class Main extends Application {

    private static Stage stg;
    Repository<Long, UserGUI> repo = new UserDbRepositoryGUI("jdbc:postgresql://localhost:5432/academicGUI","postgres","1234",new UserValidator());
    Repository<Tuple<Long,Long>, Friendship> repoFriendship = new FriendshipDbRepositoryGUI("jdbc:postgresql://localhost:5432/academicGUI","postgres","1234");
    ServiceUserGUI serv = new ServiceUserGUI(repo,repoFriendship);
    ServiceFriendshipGUI serviceFriendshipGUI = new ServiceFriendshipGUI(repo,repoFriendship);
//    public ServiceUserGUI getService(){
//        return this.serv;
//    }

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws IOException {
        serv.getAll().forEach(System.out::println);

        stg = primaryStage;
        FXMLLoader fxmlLoader = new FXMLLoader();

//        for(Friendship fr:serviceFriendshipGUI.getAll()){
//            System.out.println(fr.getId1() + " este prieten cu " + fr.getId2());
//        }

//        fxmlLoader.setLocation(getClass().getResource("views/register-view.fxml"));
//        stg.setScene(new Scene((GridPane)fxmlLoader.load(),420,240));
//        RegisterController register_controller = fxmlLoader.getController();
//        register_controller.setService(serv);

        fxmlLoader.setLocation(getClass().getResource("views/login-view.fxml"));
//        GridPane rootLayout = (GridPane)fxmlLoader.load();
//        Scene scene = new Scene(rootLayout, 420, 240);
        stg.setScene(new Scene((GridPane)fxmlLoader.load(),420,240));

        LoginController login_controller = fxmlLoader.getController();
        login_controller.setService(serv,serviceFriendshipGUI);

        serviceFriendshipGUI.getAll().forEach(System.out::println);

        stg.setTitle("Log in");
        stg.show();
    }

//    public void changeScene(String fxml) throws IOException{
////        Parent pane = FXMLLoader.load(getClass().getResource(fxml));
//        if(fxml.equals("views/login-view.fxml")) {
//            System.out.println("intrat");
//            System.out.println(serv);
//            FXMLLoader fxmlLoader = new FXMLLoader();
//            fxmlLoader.setLocation(getClass().getResource("views/login-view.fxml"));
//            stg.setScene(new Scene((GridPane)fxmlLoader.load(),420,240));
//            LoginController login_controller = fxmlLoader.getController();
//            login_controller.setService(serv);
//        }
//        else{
//            FXMLLoader fxmlLoader = new FXMLLoader();
//            fxmlLoader.setLocation(getClass().getResource("views/register-view.fxml"));
//            stg.setScene(new Scene((GridPane)fxmlLoader.load(),420,240));
//            RegisterController register_controller = fxmlLoader.getController();
//            register_controller.setService(serv);
//        }
////        stg.setTitle("Register");
//        stg.getScene().setRoot(FXMLLoader.load(getClass().getResource(fxml)));
//    }
}