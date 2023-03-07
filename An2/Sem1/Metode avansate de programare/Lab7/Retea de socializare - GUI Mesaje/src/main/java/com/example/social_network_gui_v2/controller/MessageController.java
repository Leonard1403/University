package com.example.social_network_gui_v2.controller;

//import javafx.fxml.FXML;

import com.example.social_network_gui_v2.Main;
import com.example.social_network_gui_v2.domain.Friendship;
import com.example.social_network_gui_v2.domain.Mesaj;
import com.example.social_network_gui_v2.domain.TheFriends;
import com.example.social_network_gui_v2.domain.UserGUI;
import com.example.social_network_gui_v2.domain.validation.ValidationException;
import com.example.social_network_gui_v2.service.ServiceFriendshipGUI;
import com.example.social_network_gui_v2.service.ServiceMesajGUI;
import com.example.social_network_gui_v2.service.ServiceUserGUI;
import com.example.social_network_gui_v2.unused.MessageAlert;
import com.example.social_network_gui_v2.utils.events.MesajChangeEvent;
import com.example.social_network_gui_v2.utils.observer.Observer;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.GridPane;
import javafx.scene.text.Text;
import javafx.stage.Modality;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class MessageController implements Observer<MesajChangeEvent> {

    ServiceMesajGUI service;
//    Mesaj mesaj;
    UserGUI user;
    UserGUI destinatar;
    ObservableList<Mesaj> model = FXCollections.observableArrayList();

    @FXML
    TableView< Mesaj > tableView;

    @FXML
    TableColumn<Mesaj,String> tableColumnNume;
    @FXML
    TableColumn <Mesaj,String> tableColumnDestinatar;
    @FXML
    TableColumn <Mesaj,String> tableColumnMesaj;

    @FXML
    TextField textFieldMesaj;

    @FXML
    Button buttonSend;

    public void setService(UserGUI user,UserGUI destinatar, ServiceMesajGUI serv){
        this.user = user;
        this.destinatar = destinatar;
        this.service = serv;
        service.addObserver(this);
        initModel();
    }
    @FXML
    public void initialize(){
        tableColumnNume.setCellValueFactory(new PropertyValueFactory<Mesaj,String>("nume"));
        tableColumnDestinatar.setCellValueFactory(new PropertyValueFactory<Mesaj,String>("destinatar"));
        tableColumnMesaj.setCellValueFactory(new PropertyValueFactory<Mesaj,String>("mesaj"));
        tableView.setItems(model);
    }

    private void initModel(){
//        Iterable <Friendship> friendships = service.getAll();
//        service.setName();

//        Iterable <Friendship> friendships = service.getFriends(user.getId());
        Iterable <Mesaj> mesaj = service.printUs(user.getUsername(),destinatar.getUsername());
//        System.out.println(user);
////        friendships.forEach(System.out::println);
//        List<Friendship> friendshipList = StreamSupport.stream(friendships.spliterator(),false).collect(Collectors.toList());
//
//        System.out.println("Afisare lista: ");
//        friendshipList.forEach(System.out::println);

        //-----------------------------------------------------
//        List< TheFriends > prietenii = new ArrayList<TheFriends>();
        List < Mesaj > mesaje = new ArrayList<>();

//        for(Friendship fr:friendships){
//            if(user.getId() == fr.getId1()){
//                prietenii.add(new TheFriends(serv.findOne(fr.getId2()).getUsername(),fr.getDate(),fr.getState()));
////                TheFriends folk = new TheFriends(serv.findOne(fr.getId2()).getUsername(),fr.getDate(),fr.getState());
////                System.out.println(folk);
//            }
//            else {
//                prietenii.add(new TheFriends(serv.findOne(fr.getId1()).getUsername(),fr.getDate(),fr.getState()));
////                TheFriends folk = new TheFriends(serv.findOne(fr.getId1()).getUsername(),fr.getDate(),fr.getState());
////                System.out.println(folk);
//            }
//        }
//        for(TheFriends pr: prietenii)
//            System.out.println(pr);
//
//        model.setAll(prietenii);

        for(Mesaj fr:mesaj){
            mesaje.add(new Mesaj(fr.getNume(),fr.getDestinatar(),fr.getMesaj()));
        }

        model.setAll(mesaje);
        //-----------------------------------------------

//        model.setAll(friendshipList);
//        friendships.forEach(System.out::println);
    }

    @FXML
    public void SendButtonAction(){
        System.out.println("Send button actioned");
        try {
            service.save(user.getUsername(),destinatar.getUsername(),textFieldMesaj.getText());
        }
        catch(ValidationException e){
            e.getMessage();
        }
    }

    @Override
    public void update(MesajChangeEvent mesajChangeEvent) {
        initModel();
    }
}
