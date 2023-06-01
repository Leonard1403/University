package aplicatie;

import aplicatie.model.Manager;
import aplicatie.persistance.hibernate.ManagerHibernate;

public class ManagerService implements Service<Manager, Integer>{

    private ManagerHibernate managerDbRepository;

    public ManagerService(ManagerHibernate managerHibernate){
        managerDbRepository = managerHibernate;
    }
    @Override
    public Manager findOne(Integer integer) {
        return managerDbRepository.findOne(integer);
    }

    public Manager findOne(String username, String password){
        return managerDbRepository.findOne(username,password);
    }
    @Override
    public Iterable<Manager> findAll() {
        return managerDbRepository.findAll();
    }

    @Override
    public Manager save(Manager entity) {
        return managerDbRepository.save(entity);
    }

    @Override
    public Manager delete(Integer integer) {
        return managerDbRepository.delete(integer);
    }

    @Override
    public Manager update(Manager entity) {
        return managerDbRepository.update(entity);
    }
}
