package com.example.social_network_gui_v2.controller;

import com.example.social_network_gui_v2.domain.Friendship;
import com.example.social_network_gui_v2.domain.UserGUI;
import com.example.social_network_gui_v2.domain.validation.ValidationException;
import com.example.social_network_gui_v2.service.ServiceFriendshipGUI;
import com.example.social_network_gui_v2.service.ServiceUserGUI;
import com.example.social_network_gui_v2.unused.MessageAlert;
import com.example.social_network_gui_v2.utils.events.FriendshipChangeEvent;
import com.example.social_network_gui_v2.utils.events.UserChangeEvent;
import com.example.social_network_gui_v2.utils.observer.Observer;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import org.controlsfx.control.action.Action;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import java.util.Scanner;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class UserController implements Observer<UserChangeEvent> {
    ObservableList<UserGUI> model = FXCollections.observableArrayList();
    List<String> username;
    private ServiceUserGUI serviceUserGUI;
    private ServiceFriendshipGUI serviceFriendshipGUI;
    private UserGUI user;

    public void setService(UserGUI user,ServiceUserGUI serviceUserGUI,ServiceFriendshipGUI serviceFriendshipGUI){
        this.serviceUserGUI = serviceUserGUI;
        this.serviceFriendshipGUI = serviceFriendshipGUI;
        this.user = user;
        serviceUserGUI.addObserver(this);
        initModel();
//        username = serviceUserGUI.getAll().stream
//        System.out.println("Constructor intrat: ");
//        System.out.println(this.user);
    }

    private void initModel(){
        model.setAll(getUserList());
    }
    @FXML
    TableColumn<UserGUI, String> tableColumnUser;
    @FXML
    TableView<UserGUI> tableViewUser;

    @FXML
    TextField textFieldName;

    @FXML
    public void initialize(){
//        System.out.println(this.user);
        tableColumnUser.setCellValueFactory(new PropertyValueFactory<UserGUI,String>("username"));
        tableViewUser.setItems(model);

        textFieldName.textProperty().addListener(o -> handleFilter());
    }

    private void handleFilter(){
        Predicate<UserGUI> p1 = n-> n.getUsername().startsWith(textFieldName.getText());

        model.setAll(getUserList()
                .stream()
                .filter(p1)
                .collect(Collectors.toList()));
    }

    private List<UserGUI> getUserList(){
        return serviceFriendshipGUI.getNotFriends(this.user.getId());
    }
    @FXML
    public void handleAddButton(ActionEvent ev){
        UserGUI selected = (UserGUI) tableViewUser.getSelectionModel().getSelectedItem();
        if(selected != null){
            try {
                Friendship fr = serviceFriendshipGUI.addFriend(selected.getId(), user.getId());
//                fr.setSendTo(selected.getUsername());
                serviceFriendshipGUI.corespondent(selected.getId(), user.getId(),selected.getUsername());
                System.out.println("Prietenie adaugata: " + fr);

//                try{
//                    FileWriter myWriter = new FileWriter("data/friends.txt");
//                    myWriter.write(String.valueOf(selected.getId()) + String.valueOf(user.getId()));
//                    myWriter.close();
//                }catch(FileNotFoundException e){
//                    System.out.println("O eroare a aparut");
//                    e.printStackTrace();
//                } catch (IOException e) {
//                    throw new RuntimeException(e);
//                }

                initModel();
            }
            catch (ValidationException e)
            {
                e.getMessage();
            }
        }
        else{
            MessageAlert.showErrorMessage(null, "Nu ati selectat nici un user!");
        }
    }

    @Override
    public void update(UserChangeEvent userChangeEvent){
        initModel();
    }
}
