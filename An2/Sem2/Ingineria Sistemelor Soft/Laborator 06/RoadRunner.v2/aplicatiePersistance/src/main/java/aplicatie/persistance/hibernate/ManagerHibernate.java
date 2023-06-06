package aplicatie.persistance.hibernate;

import aplicatie.model.Manager;
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

public class ManagerHibernate implements Repository<Integer, Manager> {

    private static SessionFactory sessionFactory;

    public ManagerHibernate() {
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
                System.err.println("Exception: " + e);
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
    public Manager findOne(Integer integer) {
        Manager manager = null;
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();

                manager = session.get(Manager.class, integer);

                tx.commit();
            } catch (RuntimeException ex) {
                System.err.println("Error during find operation: " + ex);
                if (tx != null)
                    tx.rollback();
            }
        }
        return manager;
    }

    public Manager findOne(String username, String password) {
        Iterable<Manager> managerIterable = findAll();
        for (Manager m : managerIterable) {
            if (m.getUsername().equals(username) && m.getPassword().equals(password)) {
                return m;
            }
        }
        return null;
    }

    @Override
    public Iterable<Manager> findAll() {
        List<Manager> managers = new ArrayList<>();
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();

                Query query = session.createQuery("FROM Manager", Manager.class);
                managers = (List<Manager>) ((org.hibernate.query.Query<?>) query).list();

                tx.commit();
            } catch (RuntimeException ex) {
                System.err.println("Error during find all operation: " + ex);
                if (tx != null)
                    tx.rollback();
            }
        }
        return managers;
    }

    @Override
    public Manager save(Manager entity) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();

                session.save(entity);

                tx.commit();
                return entity;
            } catch (RuntimeException ex) {
                System.err.println("Error during save operation: " + ex);
                if (tx != null)
                    tx.rollback();
            }
        }
        return null;
    }

    @Override
    public Manager delete(Integer integer) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();

                Manager manager = session.get(Manager.class, integer);
                if (manager != null) {
                    session.delete(manager);
                }

                tx.commit();
                return manager;
            } catch (RuntimeException ex) {
                System.err.println("Error during delete operation: " + ex);
                if (tx != null)
                    tx.rollback();
            }
        }
        return null;
    }

    @Override
    public Manager update(Manager entity) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();

                session.update(entity);

                tx.commit();
                return entity;
            } catch (RuntimeException ex) {
                System.err.println("Error during update operation: " + ex);
                if (tx != null)
                    tx.rollback();
            }
        }
        return null;
    }
}
