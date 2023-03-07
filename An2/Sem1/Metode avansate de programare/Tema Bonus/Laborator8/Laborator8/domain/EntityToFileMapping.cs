using Laborator8.domain.validator;
using Laborator8.repository;
using Laborator8.validator;

namespace Laborator8.domain
{
    class EntityToFileMapping
    {
        private static EleviFileRepository eleviFileRepository =
            new EleviFileRepository(new ElevValidator(), "elevi.txt");

        private static EchipaFileRepository echipaFileRepository =
            new EchipaFileRepository(new EchipaValidator(), "echipa.txt", CreateEchipa);

        public static Elev CreateElev(string line)
        {
            string[] fields = line.Split(';');
            int id = int.Parse(fields[0]);
            Elev elev = new Elev(id, fields[1], fields[2]);
            return elev;
        }

        public static Echipa CreateEchipa(string line)
        {
            string[] fields = line.Split(';');
            int id = int.Parse(fields[0]);
            Echipa echipa = new Echipa(id, fields[1]);
            return echipa;
        }

        private static EleviFileRepository eleviRepository;
        static EchipaFileRepository echipaRepository;
        public static Jucator CreateJucator(string line)
        {
            string[] fields = line.Split(';');
            int id = int.Parse(fields[0]);
            Jucator jucator = new Jucator(id, eleviRepository.FindOne(int.Parse(fields[1])), echipaRepository.FindOne(int.Parse(fields[2])));
            return jucator;
        }
    }
}