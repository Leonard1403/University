package aplicatie;

import aplicatie.model.Angajat;
import aplicatie.model.Manager;
import aplicatie.persistance.hibernate.AngajatHibernate;
import aplicatie.persistance.hibernate.ManagerHibernate;

public class Main {
    public static void main(String[] args) {

        AngajatHibernate angajatHibernate = new AngajatHibernate();
        Iterable<Angajat> all = angajatHibernate.findAll();
        for(Angajat a: all){
            System.out.println(a);
        }
        angajatHibernate.close();

        ManagerHibernate managerHibernate = new ManagerHibernate();
        Iterable<Manager> all2 = managerHibernate.findAll();
        for(Manager a: all2){
            System.out.println(a);
        }
    }
}