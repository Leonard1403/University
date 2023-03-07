package com.example.social_network_gui_v2.domain;

import java.time.format.DateTimeFormatter;

public class Mesaj extends Entity<Long> {

    private String mesaj;
    private String nume;
    private String destinatar;
    private DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
    public Mesaj(String nume, String destinatar, String mesaj){
        this.nume = nume;
        this.destinatar = destinatar;
        this.mesaj = mesaj;
    }

    public void setMesaj(String mesaj){
        this.mesaj = mesaj;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public void setDestinatar(String destinatar) {
        this.destinatar = destinatar;
    }

    public String getMesaj(){
        return this.mesaj;
    }

    public String getDestinatar(){
        return this.destinatar;
    }

    public String getNume(){
        return this.nume;
    }
}
