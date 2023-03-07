package com.example.social_network_gui_v2.utils.events;

import com.example.social_network_gui_v2.domain.Friendship;
import com.example.social_network_gui_v2.domain.Mesaj;

public class MesajChangeEvent implements Event{
    private ChangeEventType type;
    private Mesaj data, oldData;

    public MesajChangeEvent(ChangeEventType type, Mesaj data){
        this.type = type;
        this.data = data;
    }

    public MesajChangeEvent(ChangeEventType type, Mesaj data, Mesaj oldData){
        this.type = type;
        this.data = data;
        this.oldData = oldData;
    }

    public ChangeEventType getType() {
        return type;
    }

    public Mesaj getData() {
        return data;
    }

    public Mesaj getOldData() {
        return oldData;
    }
}
