package aplicatie.model;

public class Manager extends Entity<Integer>{
    private Integer id = getId();
    private String nume;
    private String prenume;
    private int varsta;
    private String username;
    private String password;

    public Manager(){
    }

    public Manager(String nume, String prenume, int varsta) {
        this.nume = nume;
        this.prenume = prenume;
        this.varsta = varsta;
    }

    public Manager(String nume, String prenume, int varsta, String username, String password) {
        this.nume = nume;
        this.prenume = prenume;
        this.varsta = varsta;
        this.username = username;
        this.password = password;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public String getPrenume() {
        return prenume;
    }

    public void setPrenume(String prenume) {
        this.prenume = prenume;
    }

    public int getVarsta() {
        return varsta;
    }

    public void setVarsta(int varsta) {
        this.varsta = varsta;
    }

    @Override
    public String toString() {
        return "Manager{" +
                "nume='" + nume + '\'' +
                ", prenume='" + prenume + '\'' +
                ", varsta=" + varsta +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                '}';
    }
}
