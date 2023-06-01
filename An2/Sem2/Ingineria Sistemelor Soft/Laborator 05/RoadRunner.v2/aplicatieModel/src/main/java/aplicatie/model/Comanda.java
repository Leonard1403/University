package aplicatie.model;

public class Comanda extends Entity<Integer>{
    private String nume;
    private String denumire;
    private int greutate;
    private TypeComanda tip;

    public Comanda(){

    }
    public Comanda(String nume, String denumire, int greutate, TypeComanda tip) {
        this.nume = nume;
        this.denumire = denumire;
        this.greutate = greutate;
        this.tip = tip;
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

    public TypeComanda getTip() {
        return tip;
    }

    public void setTip(TypeComanda tip) {
        this.tip = tip;
    }

    @Override
    public String toString() {
        return "Comanda{" +
                "nume='" + nume + '\'' +
                ", denumire='" + denumire + '\'' +
                ", greutate=" + greutate +
                ", tip=" + tip +
                '}';
    }
}
