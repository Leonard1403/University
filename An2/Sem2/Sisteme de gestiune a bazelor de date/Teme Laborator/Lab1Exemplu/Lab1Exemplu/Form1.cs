using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace Lab1Exemplu
{
    public partial class Form1 : Form
    {
        SqlConnection connection;
        SqlDataAdapter daArtist, daCS;
        DataSet ds;
        SqlCommandBuilder cb;
        BindingSource bsArtist, bsCS;

        public Form1()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            daArtist.Update(ds, "Solist");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            connection = new SqlConnection(@"Data Source = DESKTOP-UIQ2NDG; Initial Catalog=DBSolisti; Integrated Security = True");
            //connection.Open();
            ds = new DataSet();
            daArtist = new SqlDataAdapter("select * from Solist", connection);
            daCS = new SqlDataAdapter("select * from CasaDiscuri", connection);
            cb = new SqlCommandBuilder(daArtist);
            daArtist.Fill(ds, "Solist");
            daCS.Fill(ds, "CasaDiscuri");
            DataRelation dr = new DataRelation("FK_CasaDiscuri_Artist", ds.Tables["CasaDiscuri"].Columns["codCD"], ds.Tables["Solist"].Columns["codCD"]);
            ds.Relations.Add(dr);
            bsArtist = new BindingSource();
            bsCS = new BindingSource();
            bsCS.DataSource = ds;
            bsCS.DataMember = "CasaDiscuri";
            bsArtist.DataSource = bsCS;
            bsArtist.DataMember = "FK_CasaDiscuri_Artist";
            GridArtist.DataSource = bsArtist;
            GridCasaDiscuri.DataSource = bsCS;
            
            //connection.Close();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
        private void GridArtist_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void GridCasaDiscuri_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}