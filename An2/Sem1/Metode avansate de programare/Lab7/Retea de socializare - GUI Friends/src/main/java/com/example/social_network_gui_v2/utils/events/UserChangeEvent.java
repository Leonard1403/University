package com.example.social_network_gui_v2.utils.events;

//import com.example.social_network_gui_v2.domain.Friendship;
import com.example.social_network_gui_v2.domain.UserGUI;

public class UserChangeEvent implements Event{
    private ChangeEventType type;
    private UserGUI data, oldData;

    public UserChangeEvent(ChangeEventType type, UserGUI data){
        this.type = type;
        this.data = data;
    }

    public UserChangeEvent(ChangeEventType type, UserGUI data, UserGUI oldData){
        this.type = type;
        this.data = data;
        this.oldData = oldData;
    }

    public ChangeEventType getType() {
        return type;
    }

    public UserGUI getData() {
        return data;
    }

    public UserGUI getOldData() {
        return oldData;
    }
}
