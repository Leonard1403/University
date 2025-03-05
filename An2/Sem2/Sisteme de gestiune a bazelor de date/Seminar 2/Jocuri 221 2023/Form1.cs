using Microsoft.Data.SqlClient;
using System.Data;

namespace Jocuri_221_2023
{
    public partial class Form1 : Form
    {
        string connectionString = @"Server=DESKTOP-01E0F0G\SQLEXPRESS;
        Database=Seminar2SGBD2212023;Integrated Security=true;
        TrustServerCertificate=true;";
        DataSet ds = new DataSet();
        SqlDataAdapter parentAdapter = new SqlDataAdapter();
        SqlDataAdapter childAdapter = new SqlDataAdapter();
        BindingSource parentBS = new BindingSource();
        BindingSource childBS = new BindingSource();
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                using(SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    MessageBox.Show(connection.State.ToString());
                    parentAdapter.SelectCommand = new SqlCommand("SELECT * FROM " +
                        "Magazine;",connection);
                    parentAdapter.Fill(ds, "Magazine");
                    childAdapter.SelectCommand = new SqlCommand("SELECT * FROM " +
                        "Jocuri", connection);
                    childAdapter.Fill(ds, "Jocuri");
                    DataColumn parentColumn = ds.Tables["Magazine"].Columns["cod_m"];
                    DataColumn childColumn = ds.Tables["Jocuri"].Columns["cod_m"];
                    DataRelation relation = new DataRelation("FK_Magazine_Jocuri",
                        parentColumn,childColumn);
                    ds.Relations.Add(relation);
                    parentBS.DataSource = ds.Tables["Magazine"];
                    dataGridViewParent.DataSource = parentBS;
                    childBS.DataSource = parentBS;
                    childBS.DataMember = "FK_Magazine_Jocuri";
                    dataGridViewChild.DataSource = childBS;
                    textBox1.DataBindings.Add("Text", parentBS, "nume");

                }
            }
            catch(Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void labelNume_Click(object sender, EventArgs e)
        {

        }

        private void dataGridViewChild_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void dataGridViewParent_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }
    }
}