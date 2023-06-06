package aplicatie;

import aplicatie.model.Comanda;
import aplicatie.persistance.hibernate.ComandaHibernate;

public class ComandaService implements Service<Comanda, Integer> {

    private ComandaHibernate comandaDbHibernate;

    public ComandaService(ComandaHibernate comandaHibernate){
        this.comandaDbHibernate = comandaHibernate;
    }

    @Override
    public Comanda findOne(Integer integer) {
        return comandaDbHibernate.findOne(integer);
    }

    @Override
    public Iterable<Comanda> findAll() {
        return comandaDbHibernate.findAll();
    }

    @Override
    public Comanda save(Comanda entity) {
        return comandaDbHibernate.save(entity);
    }

    @Override
    public Comanda delete(Integer integer) {
        return comandaDbHibernate.delete(integer);
    }

    @Override
    public Comanda update(Comanda entity) {
        return comandaDbHibernate.update(entity);
    }
}
