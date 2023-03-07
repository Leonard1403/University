package com.example.social_network_gui_v2.domain;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Friendship extends Entity <Tuple < Long , Long> >{
    private LocalDateTime date;
    private String state;

    private String nume1;
    private String nume2;
    private String sendTo;

    public Friendship(){
        this.state = "Pending";
    }

    public void setDate(LocalDateTime Date){
        date=Date;
    }
    public LocalDateTime getDate(){
        return date;
    }

    public void setState(String state){
        this.state = state;
    }

    public String getState(){
        return this.state;
    }

    public void setSendTo(String nume){this.sendTo = nume;};
    public void setNume1(String nume){
        this.nume1 = nume;
    }
    public void setNume2(String nume){
        this.nume2 = nume;
    }

    public Long getId1(){
        return getId().getLeft();
    }

    public Long getId2(){
        return getId().getRight();
    }
    public String getSendTo(){return this.sendTo;}

    @Override
    public String toString() {
//        Friendship fr = new Friendship();
//        fr.getId1();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        return "Friendship{" +getId().getLeft()+" "+getId().getRight()+" "+
                "date=" + date.format(formatter) + "state=" + state +
                '}' + getSendTo();
    }
}
