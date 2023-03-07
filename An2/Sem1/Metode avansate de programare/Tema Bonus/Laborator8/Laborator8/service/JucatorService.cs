using Laborator8.domain;
using Laborator8.repository;
using System.Collections.Generic;

namespace Laborator8.service
{
    public class JucatorService
    {
        private IRepository<int, Jucator> repository;

        public JucatorService(IRepository<int, Jucator> repository)
        {
            this.repository = repository;
        }

        public void AddJucator(Jucator jucator)
        {
            repository.Save(jucator);
        }

        public void DeleteJucator(int id)
        {
            repository.Delete(id);
        }

        public void UpdateJucator(Jucator jucator)
        {
            repository.Update(jucator);
        }

        public Jucator FindOne(int id)
        {
            return repository.FindOne(id);
        }

        public IEnumerable<Jucator> FindAll()
        {
            return repository.FindAll();
        }
    }
}