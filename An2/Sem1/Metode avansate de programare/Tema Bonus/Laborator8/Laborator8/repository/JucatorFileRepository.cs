using System;
using System.Collections.Generic;
using System.Linq;
using Laborator8.domain;
using Laborator8.domain.validator;

namespace Laborator8.repository
{
    public class JucatorFileRepository : InFileRepository<int, Jucator>
    {
        public JucatorFileRepository(IValidator<Jucator> validator, string fileName, CreateEntity<Jucator> createEntity)
            : base(validator, fileName, createEntity)
        {
        }

        public Jucator Save(Jucator entity)
        {
            base.Save(entity);
            WriteToFile();
            return entity;
        }

        public Jucator Delete(int id)
        {
            Jucator jucator = FindOne(id);
            if (jucator == null)
                return default(Jucator);
            entities.Remove(id);
            WriteToFile();
            return jucator;
        }

        public Jucator Update(Jucator entity)
        {
            Jucator jucator = FindOne(entity.ID);
            if (jucator == null)
                return default(Jucator);
            vali.Validate(entity);
            entities[entity.ID] = entity;
            WriteToFile();
            return entity;
        }

        private void WriteToFile()
        {
            List<string> jucatori = new List<string>();
            foreach (Jucator jucator in FindAll())
            {
                jucatori.Add(jucator.ID + ";" + jucator.Nume + ";" + jucator.Scoala + ";" + jucator.Echipa.ID);
            }

            System.IO.File.WriteAllLines(fileName, jucatori);
        }

        public Jucator FindOne(int id)
        {
            return entities.TryGetValue(id, out Jucator jucator) ? jucator : default(Jucator);
        }

        public IEnumerable<Jucator> FindAll()
        {
            return entities.Values;
        }
    }
}