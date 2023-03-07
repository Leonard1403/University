package com.example.social_network_gui_v2.service;

import com.example.social_network_gui_v2.domain.Mesaj;
import com.example.social_network_gui_v2.domain.validation.ValidationException;
import com.example.social_network_gui_v2.repository.database.MesajDbRepositoryGUI;
import com.example.social_network_gui_v2.utils.events.ChangeEventType;
import com.example.social_network_gui_v2.utils.events.FriendshipChangeEvent;
import com.example.social_network_gui_v2.utils.events.MesajChangeEvent;
import com.example.social_network_gui_v2.utils.observer.Observable;
import com.example.social_network_gui_v2.utils.observer.Observer;

import java.util.ArrayList;
import java.util.List;

public class ServiceMesajGUI implements Observable<MesajChangeEvent> {

    private final MesajDbRepositoryGUI repoMesaj;

    public ServiceMesajGUI(MesajDbRepositoryGUI RepoMesaj){
        this.repoMesaj = RepoMesaj;
//        setName();
    }

    public void save(String nume, String destinatar, String mesaj) {
        Mesaj msj = new Mesaj(nume,destinatar,mesaj);

//        UserGUI user = new UserGUI(username,password);
//        long id = get_size();
//        id++;
//        user.setId(id);
//        UserGUI save = repoUser.save(user);
//        if (save != null)
//            throw new ValidationException("ID ALREADY USED!");

        Mesaj save = repoMesaj.save(msj);
        if(save != null){
            throw new ValidationException("Nu se salveaza");
        }
        else{
            notifyObservers(new MesajChangeEvent(ChangeEventType.ADD,(Mesaj)save));
        }
    }

    public Iterable<Mesaj> printUs(String nume, String destinatar){
        return repoMesaj.findAll(nume, destinatar);
    }

    private List<Observer<MesajChangeEvent>> observers=new ArrayList<>();
    @Override
    public void addObserver(Observer<MesajChangeEvent> e){
        observers.add(e);
    }

    @Override
    public void removeObserver(Observer<MesajChangeEvent> e){

    }

    @Override
    public void notifyObservers(MesajChangeEvent t) {
        observers.stream().forEach(x->x.update(t));
    }

}
