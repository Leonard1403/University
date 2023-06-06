package aplicatie.model;

public class Comanda extends Entity<Integer>{

    private Integer id = getId();
    private String nume;
    private String denumire;
    private int greutate;

    private TypeComanda tip;
    private String tipString;

    public Comanda(){

    }

    public Comanda(String nume, String denumire, int greutate, TypeComanda tip) {
        this.nume = nume;
        this.denumire = denumire;
        this.greutate = greutate;
        this.tip = tip;
    }

    public Comanda(String nume, String denumire, int greutate, String tip) {
        this.nume = nume;
        this.denumire = denumire;
        this.greutate = greutate;
        this.tipString = tip;
        if(tip.equals("Livrat"))
            this.tip = TypeComanda.Livrat;
        if(tip.equals("Anulat"))
            this.tip = TypeComanda.Anulat;
    }
    public Comanda(String nume, String denumire, int greutate) {
        this.nume = nume;
        this.denumire = denumire;
        this.greutate = greutate;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public String getDenumire() {
        return denumire;
    }

    public void setDenumire(String denumire) {
        this.denumire = denumire;
    }

    public int getGreutate() {
        return greutate;
    }

    public void setGreutate(int greutate) {
        this.greutate = greutate;
    }

    public String getTip() {
        if(tip == TypeComanda.Livrat)
            return "Livrat";
        if(tip == TypeComanda.Anulat)
            return "Anulat";
        if(tip == TypeComanda.InProgres)
            return "InProgress";
        return tipString;
    }

    public void setTip(TypeComanda tip) {
        this.tip = tip;
    }

    public String getTipString() {
        return tipString;
    }

    public void setTipString(String tipString) {
        this.tipString = tipString;
    }

    @Override
    public String toString() {
        return "Comanda{" +
                "nume='" + nume + '\'' +
                ", denumire='" + denumire + '\'' +
                ", greutate=" + greutate +
                ", tip=" + tipString +
                '}';
    }
}
