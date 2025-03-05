using System.Data;
using Microsoft.Data.SqlClient;

namespace Laborator01
{
    public partial class Form1 : Form
    {
        string connectionString = @"Data Source=DESKTOP-UIQ2NDG;
        Initial Catalog=Farmacie;Integrated Security=true;TrustServerCertificate=true;";

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
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    MessageBox.Show(connection.State.ToString());
                    parentAdapter.SelectCommand = new SqlCommand("SELECT * FROM " +
                        "Clienti;", connection);
                    parentAdapter.Fill(ds, "Clienti");
                    childAdapter.SelectCommand = new SqlCommand("SELECT * FROM " +
                        "Comenzi", connection);
                    childAdapter.Fill(ds, "Comenzi");
                    DataRelation dr = new DataRelation("FK_Clienti_Comenzi", ds.Tables["Clienti"].Columns["idClient"], ds.Tables["Comenzi"].Columns["idClient"]);
                    ds.Relations.Add(dr);
                    parentBS.DataSource = ds.Tables["Clienti"];
                    dataGridParent.DataSource = parentBS;
                    childBS.DataSource = parentBS;
                    childBS.DataMember = "FK_Clienti_Comenzi";
                    dataGridChild.DataSource = childBS;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void dataGridParent_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    string sql = "DELETE FROM COMENZI WHERE idComanda = @idComanda";
                    SqlCommand command = new SqlCommand(sql, connection);

                    //command.Parameters.AddWithValue("@DataLivrare", dateTimePicker1.Value);
                    //command.Parameters.AddWithValue("@numeComenzi", textBox1.Text);
                    command.Parameters.AddWithValue("@idComanda", dataGridChild.CurrentRow.Cells["idComanda"].Value);
                    int rowsAffected = command.ExecuteNonQuery();
                    if (rowsAffected > 0)
                    {
                        MessageBox.Show("Stergere efectuată cu succes!");
                        // Refacem interogarea și reîncărcăm datele în grid-uri
                        childAdapter.SelectCommand = new SqlCommand("SELECT * FROM Comenzi", connection);
                        ds.Tables["Comenzi"].Clear();
                        childAdapter.Fill(ds, "Comenzi");
                        // Resetăm sursele de date ale grid-urilor pentru a le actualiza
                        //parentBS.ResetBindings(false);
                        childBS.ResetBindings(false);
                    }
                    else
                    {
                        MessageBox.Show("Stergere nereușită!");
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            /*
            // afișăm un mesaj de confirmare
            DialogResult dr;
            //dr = MessageBox.Show("Are you sure?\n No undo after delete", "Confirm Deletion", MessageBoxButtons.YesNo);
            //if (dr == DialogResult.Yes)
            //{
                // obținem comanda de ștergere și setăm parametrul @id cu valoarea corespunzătoare
                childAdapter.DeleteCommand = new SqlCommand("DELETE FROM Comenzi WHERE idComanda=@id", new SqlConnection(connectionString));
                childAdapter.DeleteCommand.Parameters.Add("@id", SqlDbType.Int).Value = (int)dataGridChild.CurrentRow.Cells["idComanda"].Value;

                // ștergem înregistrarea curentă din DataSet
                ds.Tables["Comenzi"].Rows[dataGridChild.CurrentRow.Index].Delete();

                // actualizăm baza de date
                try
                {
                    childAdapter.Update(ds, "Comenzi");
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            //}
            */
        }


        private void dataGridChild_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void dataGridChild_CellEndEdit(object sender, DataGridViewCellEventArgs e)
        {
            try
            {
                childAdapter.Update(ds, "Comenzi");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e){
            try
            {
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    string sql = "UPDATE Comenzi SET Data_Livrare = @DataLivrare, numeComenzi = @numeComenzi WHERE idComanda = @idComanda";
                    SqlCommand command = new SqlCommand(sql, connection);
                    
                    command.Parameters.AddWithValue("@DataLivrare", dateTimePicker1.Value);
                    command.Parameters.AddWithValue("@numeComenzi", textBox1.Text);
                    command.Parameters.AddWithValue("@idComanda", dataGridChild.CurrentRow.Cells["idComanda"].Value);
                    int rowsAffected = command.ExecuteNonQuery();
                    if (rowsAffected > 0)
                    {
                        MessageBox.Show("Actualizare efectuată cu succes!");
                        // Refacem interogarea și reîncărcăm datele în grid-uri
                        childAdapter.SelectCommand = new SqlCommand("SELECT * FROM Comenzi", connection);
                        ds.Tables["Comenzi"].Clear();
                        childAdapter.Fill(ds, "Comenzi");
                        // Resetăm sursele de date ale grid-urilor pentru a le actualiza
                        //parentBS.ResetBindings(false);
                        childBS.ResetBindings(false);
                    }
                    else
                    {
                        MessageBox.Show("Actualizare nereușită!");
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }




        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                // obținem id-ul comenzii
                int idComanda = 0;
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    SqlCommand cmd = new SqlCommand("SELECT MAX(idComanda) FROM Comenzi", connection);
                    object result = cmd.ExecuteScalar();
                    if (result != null && result != DBNull.Value)
                    {
                        idComanda = (int)result;
                    }
                }
                idComanda++;

                // obținem id-ul clientului din selecția curentă
                int idClient = (int)dataGridParent.CurrentRow.Cells["idClient"].Value;

                // adăugăm o nouă înregistrare în DataSet
                DataRow newRow = ds.Tables["Comenzi"].NewRow();
                newRow["idComanda"] = idComanda;
                newRow["Data_Livrare"] = dateTimePicker1.Value;
                newRow["numeComenzi"] = textBox1.Text;
                newRow["idClient"] = idClient;
                ds.Tables["Comenzi"].Rows.Add(newRow);

                // actualizăm baza de date
                childAdapter.InsertCommand = new SqlCommand("INSERT INTO Comenzi (idComanda, Data_Livrare, numeComenzi, idClient) VALUES (@idComanda, @Data_Livrare, @numeComenzi, @idClient)", new SqlConnection(connectionString));
                childAdapter.InsertCommand.Parameters.Add("@idComanda", SqlDbType.Int).Value = idComanda;
                childAdapter.InsertCommand.Parameters.Add("@Data_Livrare", SqlDbType.Date).Value = dateTimePicker1.Value.Date;
                childAdapter.InsertCommand.Parameters.Add("@numeComenzi", SqlDbType.VarChar, 60).Value = textBox1.Text;
                childAdapter.InsertCommand.Parameters.Add("@idClient", SqlDbType.Int).Value = idClient;
                childAdapter.Update(ds, "Comenzi");

                // reîncărcăm selecția pentru a reflecta adăugarea noii înregistrări
                childBS.DataSource = parentBS;
                childBS.DataMember = "FK_Clienti_Comenzi";
                dataGridChild.DataSource = childBS;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }


        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {

        }
    }
}
