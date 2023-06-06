package aplicatie;

import aplicatie.model.Comanda;
import aplicatie.persistance.hibernate.ComandaHibernate;

public class Main {
    public static void main(String[] args) {

//        AngajatHibernate angajatHibernate = new AngajatHibernate();
//        Iterable<Angajat> all = angajatHibernate.findAll();
//        for(Angajat a: all){
//            System.out.println(a);
//        }

//        Angajat angajat = new Angajat("Test","Test123","test", "test", 12);
//        angajatHibernate.save(angajat);

//        angajatHibernate.close();

//        ManagerHibernate managerHibernate = new ManagerHibernate();
//        Iterable<Manager> all2 = managerHibernate.findAll();
//        for(Manager a: all2){
//            System.out.println(a);
//        }
//        managerHibernate.close();

        ComandaHibernate comandaHibernate = new ComandaHibernate();
//        Comanda comanda = new Comanda("Nume","Denumire",100, "Livrat");
//        System.out.println(comanda.getTip());
//        comandaHibernate.save(comanda);
        Iterable<Comanda> all3 = comandaHibernate.findAll();
        for(Comanda a: all3){
            System.out.println(a);
        }
        comandaHibernate.close();
    }
}