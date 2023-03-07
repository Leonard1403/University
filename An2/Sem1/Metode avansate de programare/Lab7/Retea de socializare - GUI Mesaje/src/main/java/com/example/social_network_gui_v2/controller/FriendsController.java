package com.example.social_network_gui_v2.controller;

import com.example.social_network_gui_v2.Main;
import com.example.social_network_gui_v2.domain.Friendship;
import com.example.social_network_gui_v2.domain.UserGUI;
import com.example.social_network_gui_v2.domain.validation.ValidationException;
import com.example.social_network_gui_v2.service.ServiceFriendshipGUI;
import com.example.social_network_gui_v2.service.ServiceMesajGUI;
import com.example.social_network_gui_v2.service.ServiceUserGUI;
import com.example.social_network_gui_v2.unused.MessageAlert;
import com.example.social_network_gui_v2.utils.events.FriendshipChangeEvent;
import com.example.social_network_gui_v2.utils.observer.Observer;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;

import com.example.social_network_gui_v2.domain.TheFriends;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.GridPane;
import javafx.stage.Modality;
import javafx.stage.Stage;

import java.io.IOException;
import java.security.Provider;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

public class FriendsController implements Observer<FriendshipChangeEvent> {

    ServiceFriendshipGUI service;
    UserGUI user;
    ServiceUserGUI serv;

    ServiceMesajGUI serviceMesajGUI;
    ObservableList<TheFriends> model = FXCollections.observableArrayList();

    @FXML
//    TableView<Friendship> tableView;
    TableView<TheFriends> tableView;
    @FXML
//    TableColumn<Friendship,String> tableColumnUsername;
    TableColumn<TheFriends,String> tableColumnUsername;
    @FXML
//    TableColumn<Friendship,String> tableColumnData;
    TableColumn<TheFriends,String> tableColumnData;
    @FXML
//    TableColumn<Friendship,String> tableColumnStatus;
    TableColumn<TheFriends,String> tableColumnStatus;

    public void setFriendshipService(UserGUI user, ServiceUserGUI serv, ServiceFriendshipGUI serviceFriendshipGUI, ServiceMesajGUI serviceMesajGUI){
        this.user = user;
        this.serv = serv;
        this.serviceMesajGUI = serviceMesajGUI;
        service = serviceFriendshipGUI;
        service.addObserver(this);
        initModel();
    }

    @FXML
    public void initialize(){
        tableColumnUsername.setCellValueFactory(new PropertyValueFactory<TheFriends,String> ("nume"));
        tableColumnStatus.setCellValueFactory(new PropertyValueFactory<TheFriends,String>("state"));
        tableColumnData.setCellValueFactory(new PropertyValueFactory<TheFriends,String>("date"));
        tableView.setItems(model);
    }

    private void initModel(){
//        Iterable <Friendship> friendships = service.getAll();
//        service.setName();

        Iterable <Friendship> friendships = service.getFriends(user.getId());
//        System.out.println(user);
////        friendships.forEach(System.out::println);
//        List<Friendship> friendshipList = StreamSupport.stream(friendships.spliterator(),false).collect(Collectors.toList());
//
//        System.out.println("Afisare lista: ");
//        friendshipList.forEach(System.out::println);

        //-----------------------------------------------------
        List < TheFriends > prietenii = new ArrayList<TheFriends>();

        for(Friendship fr:friendships){
            if(user.getId() == fr.getId1()){
                prietenii.add(new TheFriends(serv.findOne(fr.getId2()).getUsername(),fr.getDate(),fr.getState()));
//                TheFriends folk = new TheFriends(serv.findOne(fr.getId2()).getUsername(),fr.getDate(),fr.getState());
//                System.out.println(folk);
            }
            else {
                prietenii.add(new TheFriends(serv.findOne(fr.getId1()).getUsername(),fr.getDate(),fr.getState()));
//                TheFriends folk = new TheFriends(serv.findOne(fr.getId1()).getUsername(),fr.getDate(),fr.getState());
//                System.out.println(folk);
            }
        }
        for(TheFriends pr: prietenii)
            System.out.println(pr);

        model.setAll(prietenii);

        //-----------------------------------------------

//        model.setAll(friendshipList);
//        friendships.forEach(System.out::println);
    }

    @FXML
    public void handleSearchUserButtonAction(){
        System.out.println("Search user Button pressed");
        try {
            FXMLLoader SearchLoader = new FXMLLoader(Main.class.getResource("views/user-view.fxml"));
            Scene scene = new Scene(SearchLoader.load(),660,438);
//            AnchorPane rootLayout = (AnchorPane) loader.load();

            Stage UserStage = new Stage();
            UserStage.setTitle("User");
            UserStage.initModality(Modality.WINDOW_MODAL);

//            System.out.println("intrat");

            UserStage.setScene(scene);

            UserController UserController = SearchLoader.getController();
            UserController.setService(user,serv,service);

            System.out.println("Userul " + user.getUsername() + " nu este prieten cu : ");

            service.getNotFriends(user.getId()).forEach(System.out::println);

//            System.out.println("intrat");
            UserStage.show();
        }
        catch(IOException e){
            e.getMessage();
        }
    }

    @FXML
    public void handleDeleteUser(ActionEvent ev){

        TheFriends selected = (TheFriends) tableView.getSelectionModel().getSelectedItem();
        if(selected != null) {
//        System.out.println(serv.findUsername(selected.getNume()));
            System.out.println("intrat delete");
            UserGUI us = serv.findUsername(selected.getNume());
            System.out.println(us);
            try {
                service.deleteFriend(user.getId(), us.getId());
                System.out.println("S-a sters");
            } catch (ValidationException e) {
                MessageAlert.showErrorMessage(null, "User nu a fost sters!");
//                MessageAlert.showMessage(null, Alert.AlertType.INFORMATION, "Delete", "Studentul a fost sters cu succes!");
            }
        }
        else MessageAlert.showErrorMessage(null,"Nu ati selectat niciun User!");
    }

    @FXML
    public void handleAcceptUser(ActionEvent ev){
        System.out.println("accept actionat");
        TheFriends selected = (TheFriends) tableView.getSelectionModel().getSelectedItem();
        if(selected != null){
            System.out.println("intrat accept");
            UserGUI us = serv.findUsername(selected.getNume());
//            System.out.println("USER UL CU CARE SUNTEM CONECTATI + USERUL DE LA CARE AVEM CEREREA");
//            System.out.println(us);
//            System.out.println(service.findOne(us.getId(), user.getId()).getSendTo());
            if(service.findOne(us.getId(),user.getId()).getSendTo()==null)
                MessageAlert.showErrorMessage(null, "Nu se poate accepta cererea trimisa de tine!");
             else if(service.findOne(us.getId(),user.getId()).getSendTo().equals(us.getUsername())) {
                 MessageAlert.showErrorMessage(null, "Nu se poate accepta cererea trimisa de tine!");
             }
             else {
                 try {
                     service.acceptFriendship(user.getId(), us.getId());
                     service.getAll().forEach(System.out::println);
                     System.out.println("S-a acceptat");
                 } catch (ValidationException e) {
                     MessageAlert.showErrorMessage(null, "Eroare!");
                 }
             }
        }
        else MessageAlert.showErrorMessage(null,"Nu ati selectat niciun User!");
    }

    @FXML
    public void handleMesajeButtonAction(){
        System.out.println("Mesaje button actioned");
        TheFriends selected = (TheFriends) tableView.getSelectionModel().getSelectedItem();

        if(selected != null) {
            if(selected.getState().equals("Approved")) {
                try {

//                System.out.println("ajuns1");

                    FXMLLoader MesajeLoader = new FXMLLoader(Main.class.getResource("views/message-views.fxml"));
                    Scene scene = new Scene(MesajeLoader.load(), 660, 438);
//            AnchorPane rootLayout = (AnchorPane) loader.load();

//                System.out.println("ajuns2");

//                System.out.println("ajuns");

                    Stage MesajeStage = new Stage();
                    MesajeStage.setTitle("Mesage: " + user.getUsername() + "->" + selected.getNume());
                    MesajeStage.initModality(Modality.WINDOW_MODAL);

//            System.out.println("intrat");

                    MesajeStage.setScene(scene);

                    MessageController MesajeController = MesajeLoader.getController();
                    UserGUI destinatar = serv.findUsername(selected.getNume());
                    MesajeController.setService(user, destinatar, serviceMesajGUI);

//            MessageController.setService(user,serv.findUsername(selected.getNume()),serviceMesajGUI);
//            MessageController.setService();
//            System.out.println("Userul " + user.getUsername() + " nu este prieten cu : ");

                    service.getNotFriends(user.getId()).forEach(System.out::println);

//            System.out.println("intrat");
                    MesajeStage.show();
                } catch (IOException e) {
                    e.getMessage();
                }
            }
            else {
                System.out.println("Nu sunt prieteni");
            }
        }
        else {
            MessageAlert.showErrorMessage(null,"Nu ati selectat niciun User!");
        }
    }

    @Override
    public void update(FriendshipChangeEvent friendshipChangeEvent){
        initModel();
    }

}