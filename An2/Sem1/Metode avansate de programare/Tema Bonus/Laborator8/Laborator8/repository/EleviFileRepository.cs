using Laborator8.domain;
using Laborator8.domain.validator;
using System.Collections.Generic;
using System.Linq;

namespace Laborator8.repository
{
    public class EleviFileRepository : IRepository<int, Elev>
    {
        private IValidator<Elev> _validator;
        private string _fileName;
        private Dictionary<int, Elev> _entities;
        public EleviFileRepository(IValidator<Elev> validator, string fileName)
        {
            _validator = validator;
            _fileName = fileName;
            _entities = new Dictionary<int, Elev>();
            loadFromFile();
        }

        public Elev FindOne(int id)
        {
            if (_entities.TryGetValue(id, out Elev elev))
                return elev;
            return null;
        }

        public IEnumerable<Elev> FindAll()
        {
            return _entities.Values.ToList();
        }

        public Elev Save(Elev entity)
        {
            _validator.Validate(entity);
            _entities[entity.ID] = entity;
            WriteToFile();
            return default;
        }

        public Elev Delete(int id)
        {
            if (_entities.TryGetValue(id, out Elev elev))
            {
                _entities.Remove(id);
                WriteToFile();
                return elev;
            }
            return default;
        }

        public Elev Update(Elev entity)
        {
            _validator.Validate(entity);
            if (_entities.TryGetValue(entity.ID, out Elev elev))
            {
                _entities[entity.ID] = entity;
                WriteToFile();
                return entity;
            }
            return default;
        }

        private void loadFromFile()
        {
            var lines = System.IO.File.ReadAllLines(_fileName);
            foreach (var line in lines)
            {
                var fields = line.Split(";");
                var id = int.Parse(fields[0]);
                var nume = fields[1];
                var scoala = fields[2];
                var elev = new Elev(id, nume, scoala);
                _entities.Add(id, elev);
            }
        }

        private void WriteToFile()
        {
            var lines = _entities.Values.Select(elev => elev.ID + ";" + elev.Nume + ";" + elev.Scoala);
            System.IO.File.WriteAllLines(_fileName, lines);
        }
    }
}
