package com.example.social_network_gui_v2.domain;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class TheFriends {

    private String state;
    private String nume;
    private LocalDateTime date;
    private Long id;

    public TheFriends(String nume, LocalDateTime date, String state){
        this.nume = nume;
        this.date = date;
        this.state = state;
    }

    public void setState(String state){
        this.state = state;
    }
    public void setDate(LocalDateTime date){
        this.date = date;
    }
    public void setNume(String nume){
        this.nume = nume;
    }

    public String getState(){
        return this.state;
    }
    public String getNume(){
        return this.nume;
    }
    public LocalDateTime getDate(){
        return this.date;
    }

    @Override
    public String toString() {
//        Friendship fr = new Friendship();
//        fr.getId1();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        return "Prietenia {" + this.nume + " " + this.date + " " + this.state + "}";
    }
}
