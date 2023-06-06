package aplicatie.aplicatiefx;

import aplicatie.AngajatService;
import aplicatie.ManagerService;
import aplicatie.aplicatiefx.gui.LoginController;
import aplicatie.aplicatiefx.gui.SignController;
import aplicatie.persistance.hibernate.AngajatHibernate;
import aplicatie.persistance.hibernate.ManagerHibernate;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class Main extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        AngajatHibernate angajatHibernate = new AngajatHibernate();
        AngajatService angajatService = new AngajatService(angajatHibernate);

        ManagerHibernate managerHibernate = new ManagerHibernate();
        ManagerService managerService = new ManagerService(managerHibernate);

        FXMLLoader login = new FXMLLoader(
                getClass().getClassLoader().getResource("login.fxml")
        );
        Parent loginParent = login.load();
        LoginController loginController = login.<LoginController>getController();
        loginController.setService(angajatService, managerService);


        FXMLLoader signin = new FXMLLoader(
                getClass().getClassLoader().getResource("signin.fxml"));
        Parent signRoot = signin.load();

        loginController.setParentSign(signRoot);

        SignController signController = signin.<SignController>getController();
        signController.setParent(loginParent,signRoot);
        signController.setService(angajatService,managerService);

        stage.setTitle("Login");
        stage.setScene(new Scene(loginParent,520,320));

        Stage signStage = new Stage();
        signStage.setTitle("Sign in");
        signStage.setScene(new Scene(signRoot));


        loginController.setStage(signStage);
        signController.setStage(stage);

        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}