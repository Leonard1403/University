using Laborator8.domain;
using Laborator8.repository;
using System.Collections.Generic;

namespace Laborator8.service
{
    public class EchipaService
    {
        private IRepository<int, Echipa> repository;

        public EchipaService(IRepository<int, Echipa> repository)
        {
            this.repository = repository;
        }

        public void AddEchipa(Echipa echipa)
        {
            repository.Save(echipa);
        }

        public void DeleteEchipa(int id)
        {
            repository.Delete(id);
        }

        public void UpdateEchipa(Echipa echipa)
        {
            repository.Update(echipa);
        }

        public Echipa FindOne(int id)
        {
            return repository.FindOne(id);
        }

        public IEnumerable<Echipa> FindAll()
        {
            return repository.FindAll();
        }
    }
}