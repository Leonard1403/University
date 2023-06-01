package aplicatie.roadrunnerapp.model;

import java.util.Arrays;

public class Traseu extends Entity<Integer>{
    private int distanta;
    private String[] directie;
    private String descriere;

    public Traseu(){

    }

    public Traseu(int distanta, String[] directie, String descriere) {
        this.distanta = distanta;
        this.directie = directie;
        this.descriere = descriere;
    }

    public int getDistanta() {
        return distanta;
    }

    public void setDistanta(int distanta) {
        this.distanta = distanta;
    }

    public String[] getDirectie() {
        return directie;
    }

    public void setDirectie(String[] directie) {
        this.directie = directie;
    }

    public String getDescriere() {
        return descriere;
    }

    public void setDescriere(String descriere) {
        this.descriere = descriere;
    }

    @Override
    public String toString() {
        return "Traseu{" +
                "distanta=" + distanta +
                ", directie=" + Arrays.toString(directie) +
                ", descriere='" + descriere + '\'' +
                '}';
    }
}
