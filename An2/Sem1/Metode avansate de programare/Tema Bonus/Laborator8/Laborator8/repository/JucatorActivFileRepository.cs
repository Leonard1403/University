using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Laborator8.domain;

namespace Laborator8.repository
{
    public class JucatorActiveFileRepository
    {
        private readonly string _fileName;

        public JucatorActiveFileRepository(string fileName)
        {
            _fileName = fileName;
        }

        public List<JucatorActiv> GetAll()
        {
            var jucatorList = new List<JucatorActiv>();

            if (!File.Exists(_fileName))
            {
                return jucatorList;
            }

            var lines = File.ReadAllLines(_fileName);
            foreach (var line in lines)
            {
                var parts = line.Split(";");
                int idJucator = int.Parse(parts[0]);
                int idMeci = int.Parse(parts[1]);
                int nrPuncteInscrise = int.Parse(parts[2]);
                var tip = (JucatorActiv.TipJucator)Enum.Parse(typeof(JucatorActiv.TipJucator), parts[3]);
                jucatorList.Add(new JucatorActiv(idJucator, idMeci, nrPuncteInscrise, tip));
            }

            return jucatorList;
        }

        public void SaveAll(List<JucatorActiv> jucatorList)
        {
            var lines = new List<string>();
            foreach (var jucator in jucatorList)
            {
                lines.Add(jucator.IdJucator + ";" + jucator.IdMeci + ";" + jucator.NrPuncteInscrise + ";" +
                          jucator.Tip);
            }

            File.WriteAllLines(_fileName, lines);
        }

        public void Add(JucatorActiv jucator)
        {
            var jucatorList = GetAll();
            jucatorList.Add(jucator);
            SaveAll(jucatorList);
        }

        public void Update(JucatorActiv jucator)
        {
            var jucatorList = GetAll();
            var jucatorToUpdate =
                jucatorList.FirstOrDefault(j => j.IdJucator == jucator.IdJucator && j.IdMeci == jucator.IdMeci);
            if (jucatorToUpdate != null)
            {
                jucatorList.Remove(jucatorToUpdate);
                jucatorList.Add(jucator);
                SaveAll(jucatorList);
            }
        }

        public void Delete(int idJucator, int idMeci)
        {
            var jucatorList = GetAll();
            var jucatorToDelete = jucatorList.FirstOrDefault(j => j.IdJucator == idJucator && j.IdMeci == idMeci);
            if (jucatorToDelete != null)
            {
                jucatorList.Remove(jucatorToDelete);
                SaveAll(jucatorList);
            }
        }

        public void DeleteAll()
        {
            var jucatorList = new List<JucatorActiv>();
            SaveAll(jucatorList);
        }
    }
}