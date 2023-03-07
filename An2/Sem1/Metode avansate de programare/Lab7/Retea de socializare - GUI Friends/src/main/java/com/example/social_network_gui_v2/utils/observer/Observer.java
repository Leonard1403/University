package com.example.social_network_gui_v2.utils.observer;


//import ro.ubb.map.demogui.utils.events.Event;
import com.example.social_network_gui_v2.utils.events.Event;

public interface Observer<E extends Event> {
    void update(E e);
}