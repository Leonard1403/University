package com.example.social_network_gui_v2.service;

import com.example.social_network_gui_v2.domain.Entity;
import com.example.social_network_gui_v2.domain.Friendship;
import com.example.social_network_gui_v2.domain.Tuple;
import com.example.social_network_gui_v2.domain.UserGUI;
import com.example.social_network_gui_v2.domain.validation.ValidationException;
import com.example.social_network_gui_v2.repository.Repository;
import com.example.social_network_gui_v2.utils.events.ChangeEventType;
import com.example.social_network_gui_v2.utils.events.FriendshipChangeEvent;
import com.example.social_network_gui_v2.utils.events.FriendshipChangeEvent;
import com.example.social_network_gui_v2.utils.observer.Observable;
import com.example.social_network_gui_v2.utils.observer.Observer;

import java.time.LocalDateTime;
import java.util.*;

/**
 * class Service
 * repoUser-Repository for Users
 * repoFriends-Repository for Friendships
 */
public class ServiceFriendshipGUI implements Observable<FriendshipChangeEvent> {
    private Repository<Long, UserGUI> repoUser;
    private Repository<Tuple<Long,Long>, Friendship> repoFriends;

    /**
     * constructor for the com.example.social_network_gui_v2.service
     * @param RepoUser UserRepository
     * @param RepoFriends FriendsRepository
     */
    public ServiceFriendshipGUI(Repository<Long, UserGUI> RepoUser, Repository<Tuple<Long, Long>, Friendship> RepoFriends){
        repoFriends = RepoFriends;
        repoUser = RepoUser;
//        setName();
    }

    /**
     * add a friendship, call the repo function
     * if is not valid throw ValidationException
     * @param id1-Long
     * @param id2-Long
     */
    public Friendship addFriend(Long id1, Long id2) throws ValidationException {
        UserGUI u1 = repoUser.findOne(id1);
        UserGUI u2 = repoUser.findOne(id2);
        try{
            if(u1 != null && u2 != null) {
                if(repoFriends.findOne(new Tuple<>(id1,id2)) == null) {
                    Friendship friendship = new Friendship();
                    Tuple t = new Tuple(id1, id2);
                    friendship.setId(t);
                    friendship.setDate(LocalDateTime.now());
                    Friendship response = repoFriends.save(friendship);

                    if (response != null)
                        throw new ValidationException("Friendship already made!");
                    else {
                        notifyObservers(new FriendshipChangeEvent(ChangeEventType.ADD, (Friendship) response));
                        return friendship;
                    }
                }
                else
                    throw new ValidationException("Friendship already made!");
            }
            else{
                String errors = "";
                if(u1 == null)
                    errors += "First id does not exist!";
                if(u2 == null)
                    errors += "Second id does not exist!";
                throw new ValidationException(errors);
            }
        }
        catch (ValidationException e){
            throw new ValidationException(e);
        }
    }

        /**
         * delete a friendship, call the repo function
         * if is not valid throw ValidationException
         * @param id1-Long
         * @param id2-Long
         */
        public void deleteFriend(Long id1, Long id2) throws ValidationException {

        Tuple t = new Tuple(id1, id2);
        if (repoUser.findOne(id1) == null)
            throw new ValidationException("first id does not exist");
        if (repoUser.findOne(id2) == null)
            throw new ValidationException("second id does not exist");
        Friendship fr = repoFriends.findOne(t);
        Entity save = repoFriends.delete(t);
        if (save == null)
            throw new ValidationException("ids are not used in a friendship");
        if (save != null)
            notifyObservers(new FriendshipChangeEvent(ChangeEventType.DELETE, (Friendship) save));
    }

    /**
     * @return all the friendships
     */
    public Iterable<Friendship> getAll() {
        return repoFriends.findAll();
    }

    public Iterable<Friendship> getFriends(Long id) throws ValidationException{
        try{
            Set<Friendship> users= new HashSet<>();
            UserGUI response = repoUser.findOne(id);
            if(response == null)
                throw new ValidationException("id invalid!");
            else
                for (Friendship fr : repoFriends.findAll()){
                    if(Objects.equals(fr.getId().getLeft(), id))
                        users.add(fr);
                    if(Objects.equals(fr.getId().getRight(), id))
                        users.add(fr);
                }
            return users;
        }
        catch (ValidationException exception){
            throw new ValidationException(exception);
        }
    }

    public List<UserGUI> getNotFriends(Long id) throws ValidationException{
        try{
            List<UserGUI> users= new ArrayList<>();
            for(UserGUI ue:repoUser.findAll())
            {
                users.add(ue);
            }
            UserGUI response = repoUser.findOne(id);
            users.remove(response);
            if(response == null)
                throw new ValidationException("id invalid!");
            else
                for (Friendship fr : repoFriends.findAll()){
//                    if(Objects.equals(fr.getId().getLeft(), id))
//                        continue;
//                    if(Objects.equals(fr.getId().getRight(), id))
//                        continue;
//                    users.add(repoUser.findOne(fr.getId1()));
//                    users.add(repoUser.findOne(fr.getId2()));
                    if(Objects.equals(fr.getId().getLeft(),id))
                        users.remove(repoUser.findOne(fr.getId2()));
                    if(Objects.equals(fr.getId().getRight(),id))
                        users.remove(repoUser.findOne(fr.getId1()));
                }
            return users;
        }
        catch (ValidationException exception){
            throw new ValidationException(exception);
        }
    }

    /**
     * Updates the state of a friendship
     * @param id1 - Long
     * @param id2 - Long
     * @param state - String
     */
    public void update(Long id1, Long id2, String state){
        Friendship friendship = new Friendship();
        Tuple tuple = new Tuple(id1, id2);
        friendship.setId(tuple);
        friendship.setState(state);
        Friendship updated = repoFriends.update(friendship);
        if (updated != null)
            throw new ValidationException("id invalid!");
    }

    public void corespondent(Long id1, Long id2, String nume){
        Friendship friendship = new Friendship();
        Tuple tuple = new Tuple(id1, id2);
        friendship.setId(tuple);
        friendship.setSendTo(nume);
        Friendship updated = repoFriends.corespondent(friendship);
        if (updated != null)
            throw new ValidationException("id invalid!");
    }

    public void acceptFriendship(Long id1, Long id2){
        Tuple tuple = new Tuple(id1, id2);
        Friendship friendship = repoFriends.findOne(tuple);
        if(friendship != null){
            friendship.setState("Approved");
            repoFriends.update(friendship);
        }
        else
            throw new ValidationException("id invalid!");
        if (friendship != null) {
            notifyObservers(new FriendshipChangeEvent(ChangeEventType.UPDATE, friendship));
            System.out.println("intrat modificat");
        }
//        System.out.print("Ce s-a modificat: ");
//        System.out.println(friendship);
    }

    public void rejectFriendship(Long id1, Long id2){
        Tuple tuple = new Tuple(id1, id2);
        Friendship friendship = repoFriends.findOne(tuple);
        if(friendship != null){
            friendship.setState("Rejected");
        }
        else
            throw new ValidationException("id invalid!");
    }

    public void setName(){
        for(Friendship fr:repoFriends.findAll()){
            String nume1 = repoUser.findOne(fr.getId1()).getUsername();
            String nume2 = repoUser.findOne(fr.getId2()).getUsername();
//            System.out.println(nume1 + " " + nume2);
            fr.setNume1(nume1);
            fr.setNume2(nume2);
//            System.out.println("Setat: " + fr.getNume1());
//            System.out.println("Setat: " + fr.getNume2());
        }
    }

    public Friendship findOne(Long id1, Long id2){
        Tuple tuple = new Tuple(id1,id2);
        Friendship friendship = repoFriends.findOne(tuple);
//        if(friendship != null)
//            return friendship;
        return friendship;
    }
    private List<Observer<FriendshipChangeEvent>> observers=new ArrayList<>();

    @Override
    public void addObserver(Observer<FriendshipChangeEvent> e){
        observers.add(e);
    }

    @Override
    public void removeObserver(Observer<FriendshipChangeEvent> e){

    }

    @Override
    public void notifyObservers(FriendshipChangeEvent t){
        observers.stream().forEach(x->x.update(t));
    }

}
