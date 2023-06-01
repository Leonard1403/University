package aplicatie.persistance.hibernate;

import aplicatie.model.Angajat;
import aplicatie.persistance.Repository;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.boot.MetadataSources;
import org.hibernate.boot.registry.StandardServiceRegistry;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;

import javax.persistence.Query;
import java.util.ArrayList;
import java.util.List;

public class AngajatHibernate implements Repository<Integer, Angajat> {

    public AngajatHibernate(){
        initialize();
    }
    private static SessionFactory sessionFactory;

    public static void initialize() {
        // A SessionFactory is set up once for an application!
        try {
            final StandardServiceRegistry registry = new StandardServiceRegistryBuilder()
                    .configure() // configures settings from hibernate.cfg.xml
                    .build();
            try {
                sessionFactory = new MetadataSources(registry).buildMetadata().buildSessionFactory();
            } catch (Exception e) {
                System.err.println("Exceptie " + e);
                StandardServiceRegistryBuilder.destroy(registry);
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public static void close() {
        if (sessionFactory != null && !sessionFactory.isClosed()) {
            sessionFactory.close();
        }
    }

    @Override
    public Angajat findOne(Integer integer) {
        Angajat angajat = null;
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();

                angajat = session.get(Angajat.class, integer);

                tx.commit();
            } catch (RuntimeException ex) {
                System.err.println("Eroare la cautare " + ex);
                if (tx != null)
                    tx.rollback();
            }
        }
        return angajat;
    }

    public Angajat findOne(String username, String password) {
        Iterable<Angajat> angajatIterable = findAll();
        for(Angajat a: angajatIterable){
            if(a.getUsername().equals(username) && a.getPassword().equals(password)){
                return a;
            }
        }
        return null;
    }

    @Override
    public Iterable<Angajat> findAll() {
        List<Angajat> angajats = new ArrayList<>();
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();

                Query query = session.createQuery("FROM Angajat", Angajat.class);
                angajats = (List<Angajat>) ((org.hibernate.query.Query<?>) query).list();

                tx.commit();
            } catch (RuntimeException ex) {
                System.err.println("Eroare la cautare " + ex);
                if (tx != null)
                    tx.rollback();
            }
        }
        return angajats;
    }

    @Override
    public Angajat save(Angajat entity) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();

                session.save(entity);

                tx.commit();
            } catch (RuntimeException ex) {
                System.err.println("Eroare la salvare " + ex);
                if (tx != null)
                    tx.rollback();
            }
        }
        return entity;
    }

    @Override
    public Angajat delete(Integer integer) {
        return null;
    }

    @Override
    public Angajat update(Angajat entity) {
        return null;
    }
}
