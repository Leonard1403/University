using System;

namespace Laborator8.domain
{
    public class Jucator : Elev
    {
        public Echipa Echipa { get; set; }

        public Jucator(int id, Elev elev, Echipa echipa) : base(id, elev.Nume, elev.Scoala)
        {
            Echipa = echipa;
        }

        public override string ToString()
        {
            return base.ToString() + " | Echipa : " + Echipa;
        }
    }

}