namespace Laborator8.domain
{
    public class JucatorActiv
    {
        public int IdJucator { get; set; }
        public int IdMeci { get; set; }
        public int NrPuncteInscrise { get; set; }
        public TipJucator Tip { get; set; }

        public JucatorActiv(int idJucator, int idMeci, int nrPuncteInscrise, TipJucator tip)
        {
            IdJucator = idJucator;
            IdMeci = idMeci;
            NrPuncteInscrise = nrPuncteInscrise;
            Tip = tip;
        }

        public enum TipJucator
        {
            Rezerva, Participat
        }
        public override string ToString()
        {
            return base.ToString() 
                   + " idJucator=" + IdJucator
                   + " idMeci=" + IdMeci  
                   + " nrPuncteInscrise=" + NrPuncteInscrise  
                   + " TipJucator=" + Tip;
        }
    }
}