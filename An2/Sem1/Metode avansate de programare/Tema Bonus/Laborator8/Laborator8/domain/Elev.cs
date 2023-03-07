using System;

namespace Laborator8.domain
{
    public class Elev : Entity<int>
    {
        public string Nume { get; set; }
        public string Scoala { get; set; }
        
        public Elev(int id, string nume, string scoala)
        {
            ID = id;
            Nume = nume;
            Scoala = scoala;
        }

        public override bool Equals(object obj)
        {
            var elev = obj as Elev;
            return elev != null &&
                   ID == elev.ID;
        }

        public override int GetHashCode()
        {
            return HashCode.Combine(ID);
        }

        public override string ToString()
        {
            return "Elev ID: " + ID + " Nume: " + Nume + " Scoala: " + Scoala;
        }
    }
}