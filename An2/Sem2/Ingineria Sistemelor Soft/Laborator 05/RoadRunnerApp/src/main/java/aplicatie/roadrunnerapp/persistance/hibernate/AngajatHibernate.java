package aplicatie.roadrunnerapp.persistance.hibernate;

import aplicatie.roadrunnerapp.model.Angajat;
import org.hibernate.SessionFactory;
import org.hibernate.boot.MetadataSources;
import org.hibernate.boot.registry.StandardServiceRegistry;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import aplicatie.roadrunnerapp.persistance.Repository;

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
        return null;
    }

    @Override
    public Iterable<Angajat> findAll() {
        return null;
    }

    @Override
    public Angajat save(Angajat entity) {
        return null;
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
