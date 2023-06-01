package aplicatie;

import aplicatie.model.Angajat;
import aplicatie.persistance.hibernate.AngajatHibernate;

public class AngajatService implements Service<Angajat, Integer>{
    private AngajatHibernate angajatDbRepository;
    public AngajatService(AngajatHibernate angajatHibernate){
        angajatDbRepository = angajatHibernate;
    }

    @Override
    public Angajat findOne(Integer integer) {
        return angajatDbRepository.findOne(integer);
    }

    public Angajat findOne(String username, String password){
        return angajatDbRepository.findOne(username,password);
    }

    @Override
    public Iterable<Angajat> findAll() {
        return angajatDbRepository.findAll();
    }

    @Override
    public Angajat save(Angajat entity) {
        return angajatDbRepository.save(entity);
    }

    @Override
    public Angajat delete(Integer integer) {
        return angajatDbRepository.delete(integer);
    }

    @Override
    public Angajat update(Angajat entity) {
        return angajatDbRepository.update(entity);
    }
}