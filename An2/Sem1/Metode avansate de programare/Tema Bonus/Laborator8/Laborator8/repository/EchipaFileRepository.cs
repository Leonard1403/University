using Laborator8.domain;
using Laborator8.domain.validator;
using System.Collections.Generic;
using System.Linq;

namespace Laborator8.repository
{
    public class EchipaFileRepository : InFileRepository<int, Echipa>
    {
        public EchipaFileRepository(IValidator<Echipa> validator, string fileName, CreateEntity<Echipa> createEntity) :
            base(validator, fileName, createEntity)
        {
        }

        public Echipa Save(Echipa entity)
        {
            base.Save(entity);
            writeToFile();
            return default(Echipa);
        }

        public Echipa Update(Echipa entity)
        {
            base.Update(entity);
            writeToFile();
            return default(Echipa);
        }

        public Echipa Delete(int id)
        {
            Echipa echipa = base.Delete(id);
            writeToFile();
            return echipa;
        }

        private void writeToFile()
        {
            var lines = entities.Values.Select(e => e.ID + ";" + e.Nume);
            System.IO.File.WriteAllLines(fileName, lines);
        }
    }
}