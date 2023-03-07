using Laborator8.domain;

namespace Laborator8.repository
{
    public class MeciFileRepository
    {
        private readonly string _fileName;

        public MeciFileRepository(string fileName)
        {
            _fileName = fileName;
        }

        public List<Meci> GetAll()
        {
            var meciList = new List<Meci>();

            if (!File.Exists(_fileName))
            {
                Console.WriteLine("Fisierul " + _fileName + " nu exista.");
                return meciList;
            }

            if (new FileInfo(_fileName).Length == 0)
            {
                Console.WriteLine("Fisierul " + _fileName + " este gol.");
                return meciList;
            }

            var lines = File.ReadAllLines(_fileName);
            foreach (var line in lines)
            {
                var parts = line.Split(";");

                // verifica daca prima si a doua parte sunt int-uri
                if (!int.TryParse(parts[0], out int echipa1) || !int.TryParse(parts[1], out int echipa2))
                {
                    Console.WriteLine(
                        "Eroare: datele din fisier sunt scrise gresit. Verifica daca echipa1 si echipa2 sunt int-uri separate prin ';'.");
                    return meciList;
                }

                // verifica daca a treia parte este data valida
                if (!DateTime.TryParse(parts[2], out DateTime data))
                {
                    Console.WriteLine(
                        "Eroare: datele din fisier sunt scrise gresit. Verifica daca data este in formatul corect si este separata prin ';'.");
                    return meciList;
                }

                meciList.Add(new Meci(echipa1, echipa2, data));
            }

            return meciList;
        }

        public void SaveAll(List<Meci> meciList)
        {
            var lines = new List<string>();
            foreach (var meci in meciList)
            {
                lines.Add(meci.Echipa1 + ";" + meci.Echipa2 + ";" + meci.Data);
            }

            File.WriteAllLines(_fileName, lines);
        }
    }
}