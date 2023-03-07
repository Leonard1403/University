package com.example.social_network_gui_v2.utils.observer;


//import ro.ubb.map.demogui.utils.events.Event;
import com.example.social_network_gui_v2.utils.events.Event;

public interface Observable<E extends Event> {
    void addObserver(Observer<E> e);
    void removeObserver(Observer<E> e);
    void notifyObservers(E t);
}
