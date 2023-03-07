package com.example.social_network_gui_v2.service;

import com.example.social_network_gui_v2.domain.*;
import com.example.social_network_gui_v2.domain.validation.ValidationException;
import com.example.social_network_gui_v2.repository.Repository;
import com.example.social_network_gui_v2.utils.events.FriendshipChangeEvent;
import com.example.social_network_gui_v2.utils.events.UserChangeEvent;
import com.example.social_network_gui_v2.utils.observer.Observable;
import com.example.social_network_gui_v2.utils.observer.Observer;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

/**
 * class Service
 * repoUser-Repository for Users
 * repoFriends-Repository for Friendships
 */
public class ServiceUserGUI implements Observable<UserChangeEvent> {
    private final Repository<Long, UserGUI> repoUser;
    private final Repository<Tuple<Long, Long>, Friendship>  repoFriends;
    public ServiceUserGUI(Repository<Long, UserGUI> RepoUser, Repository<Tuple<Long, Long>, Friendship> repoFriends) {
        this.repoUser = RepoUser;
        this.repoFriends = repoFriends;
    }


    public void save(String username, String password) {
        UserGUI user = new UserGUI(username,password);
        long id = get_size();
        id++;
        user.setId(id);
        UserGUI save = repoUser.save(user);
        if (save != null)
            throw new ValidationException("ID ALREADY USED!");

    }

    public void update(Long id, String username, String password) {
        UserGUI user = new UserGUI(username,password);
        user.setId(id);
        UserGUI save = repoUser.update(user);
        if (save != null)
            throw new ValidationException("ID INVALID!");
    }

    public Entity delete(Long id) {

        Entity deleted = repoUser.delete(id);
        if (deleted == null)
            throw new ValidationException("ID INVALID!");
        return deleted;
    }

    public Long get_size() {
        Long maxim = 0L;
        for (UserGUI ur : repoUser.findAll())
            if (ur.getId() > maxim)
                maxim = ur.getId();
        return maxim;
    }

    public Iterable<UserGUI> printUs() {
        return repoUser.findAll();
    }

    /**Display friends for a given user
     * @param nr integer id of a posible user
     * @return the user with the given id
     * @throws ValidationException if the id for user given is invalid
     */
    public UserGUI findOne(Long nr) {
        if (repoUser.findOne(nr) != null)
            return repoUser.findOne(nr);
        else
            throw new ValidationException("ID INVALID!");
    }

    public Iterable<UserGUI> getAll(){
        return repoUser.findAll();
    }

    public UserGUI findUsername(String username){
//        Iterable u = repoUser.findAll();
//        System.out.println(username);
        for(UserGUI u:repoUser.findAll()){
//            System.out.println(u.getUsername());
            if(u.getUsername().trim().equals(username.trim())){
//                System.out.println("Intrat");
                return u;
            }
        }
        UserGUI user = new UserGUI("_","_");
//        System.out.println("Negasit");
        return user;
//        throw new ValidationException("Nu s-a gasit");
    }

    public Iterable<UserGUI> getFriends(Long id) throws ValidationException{
        try{
            Set<UserGUI> users= new HashSet<>();
            UserGUI response = repoUser.findOne(id);
            if(response == null)
                throw new ValidationException("id invalid!");
            else
                for (Friendship fr : repoFriends.findAll()){
                    if(Objects.equals(fr.getId().getLeft(), id))
                        users.add(repoUser.findOne(fr.getId().getRight()));
                    if(Objects.equals(fr.getId().getRight(), id))
                        users.add(repoUser.findOne(fr.getId().getLeft()));
                }
            return users;
        }
        catch (ValidationException exception){
            throw new ValidationException(exception);
        }
    }

    private List<Observer<UserChangeEvent>> observers=new ArrayList<>();

    @Override
    public void addObserver(Observer<UserChangeEvent> e){
        observers.add(e);
    }

    @Override
    public void removeObserver(Observer<UserChangeEvent> e){
    }
    @Override
    public void notifyObservers(UserChangeEvent t){
        observers.stream().forEach(x->x.update(t));
    }
}
