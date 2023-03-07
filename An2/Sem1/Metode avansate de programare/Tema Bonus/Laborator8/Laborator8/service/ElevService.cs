using Laborator8.domain;
using Laborator8.repository;
using System.Collections.Generic;

namespace Laborator8.service
{
    public class ElevService
    {
        private IRepository<int, Elev> _repository;

        public ElevService(IRepository<int, Elev> repository)
        {
            _repository = repository;
        }

        public Elev AddElev(int id, string nume, string scoala)
        {
            var elev = new Elev(id, nume, scoala);
            return _repository.Save(elev);
        }

        public Elev DeleteElev(int id)
        {
            return _repository.Delete(id);
        }

        public IEnumerable<Elev> GetAllElevi()
        {
            return _repository.FindAll();
        }

        public Elev GetElev(int id)
        {
            return _repository.FindOne(id);
        }

        public Elev UpdateElev(int id, string nume, string scoala)
        {
            var elev = new Elev(id, nume, scoala);
            return _repository.Update(elev);
        }
    }
}