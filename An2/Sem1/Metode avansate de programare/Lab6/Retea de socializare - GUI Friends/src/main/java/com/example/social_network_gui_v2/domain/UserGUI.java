package com.example.social_network_gui_v2.domain;

import java.util.Objects;

public class UserGUI extends Entity<Long>{
    private String username , password;

    public UserGUI(String username, String password){
        this.username = username;
        this.password = password;
    }

    public String getUsername(){
        return this.username;
    }

    public String getPassword(){
        return this.password;
    }

    public void setUsername(String username){
        this.username = username;
    }
    public void setPassword(String password){
        this.password = password;
    }

    @Override
    public String toString(){
        String s;
        s = "User{ id='" + this.getId() + '\'' +
                ", username='" + this.username + '\'' +
                ", lastName='" + this.password + "' }" ;
        return s;
    }

    @Override
    public boolean equals(Object o){
        if(this == o) return true;
        if (!(o instanceof UserGUI)) return false;
        UserGUI user = (UserGUI) o;
        return Objects.equals(getUsername(), user.getUsername()) && Objects.equals(getPassword(), user.getPassword());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getUsername(), getPassword());
    }
}
