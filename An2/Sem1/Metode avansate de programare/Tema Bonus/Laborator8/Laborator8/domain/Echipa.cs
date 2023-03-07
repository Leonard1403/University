using System;

namespace Laborator8.domain
{
    public class Echipa : Entity<int>
    {
        public string Nume { get; set; }

        public Echipa(int id, string nume)
        {
            ID = id;
            Nume = nume;
        }

        public override string ToString()
        {
            return ID + " " + Nume;
        }
    }
}