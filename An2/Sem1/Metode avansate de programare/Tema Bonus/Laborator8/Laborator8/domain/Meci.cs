
namespace Laborator8.domain
{
    public class Meci
    {
        public int Echipa1 { get; set; }
        public int Echipa2 { get; set; }
        public DateTime Data { get; set; }

        public Meci(int echipa1, int echipa2, DateTime data)
        {
            Echipa1 = echipa1;
            Echipa2 = echipa2;
            Data = data;
        }

        public override string ToString()
        {
            return base.ToString() + " echipa1=" + Echipa1
                                   + " echipa2=" + Echipa2
                                   + " data=" + Data;
        }
    }
}