package aplicatie.persistance.hibernate;

import aplicatie.model.Comanda;
import aplicatie.persistance.Repository;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.boot.MetadataSources;
import org.hibernate.boot.registry.StandardServiceRegistry;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import org.hibernate.query.Query;

import java.util.ArrayList;
import java.util.List;

public class ComandaHibernate implements Repository<Integer, Comanda> {
    private static SessionFactory sessionFactory;

    public ComandaHibernate() {
        initialize();
    }

    public static void initialize() {
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

    public void close() {
        if (sessionFactory != null && !sessionFactory.isClosed()) {
            sessionFactory.close();
        }
    }

    @Override
    public Comanda findOne(Integer integer) {
        Session session = sessionFactory.openSession();
        Comanda comanda = session.get(Comanda.class, integer);
        session.close();
        return comanda;
    }

    @Override
    public Iterable<Comanda> findAll() {
        List<Comanda> comenzi = new ArrayList<>();
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();

                Query<Comanda> query = session.createQuery("FROM Comanda", Comanda.class);
                comenzi = (List<Comanda>) ((org.hibernate.query.Query<?>) query).list();

                tx.commit();
            } catch (RuntimeException ex) {
                System.err.println("Eroare la cautare " + ex);
                if (tx != null)
                    tx.rollback();
            }
        }
        return comenzi;
    }


    @Override
    public Comanda save(Comanda entity) {
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
    public Comanda delete(Integer integer) {
        Session session = sessionFactory.openSession();
        Transaction transaction = session.beginTransaction();
        Comanda comanda = session.get(Comanda.class, integer);
        if (comanda != null) {
            session.delete(comanda);
        }
        transaction.commit();
        session.close();
        return comanda;
    }

    @Override
    public Comanda update(Comanda entity) {
        Session session = sessionFactory.openSession();
        Transaction transaction = session.beginTransaction();
        session.update(entity);
        transaction.commit();
        session.close();
        return entity;
    }
}
