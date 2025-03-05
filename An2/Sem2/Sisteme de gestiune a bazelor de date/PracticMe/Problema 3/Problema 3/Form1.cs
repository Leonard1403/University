using System.Data;
using System.Data.SqlClient;

namespace Problema_3
{
    public partial class Form1 : Form
    {
        string connectionString = @"Data Source=DESKTOP-UIQ2NDG;
        Initial Catalog=Problema3;Integrated Security=true;TrustServerCertificate=true;";

        DataSet ds = new DataSet();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                string query = "SELECT * FROM Producatori";

                SqlCommand command = new SqlCommand(query, connection);

                try
                {
                    connection.Open();

                    SqlDataAdapter adapter = new SqlDataAdapter(command);
                    DataTable dt = new DataTable();
                    adapter.Fill(dt);

                    dataGridViewProducatori.DataSource = dt;
                }
                catch (Exception ex)
                {
                    MessageBox.Show("A apărut o eroare: " + ex.Message);
                }
            }
        }

        private void IncarcaBiscuitiProducator(int codProducator)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                string query = "SELECT * FROM Biscuiti WHERE cod_p = @codProducator";

                SqlCommand command = new SqlCommand(query, connection);
                command.Parameters.AddWithValue("@codProducator", codProducator);

                try
                {
                    connection.Open();

                    SqlDataAdapter adapter = new SqlDataAdapter(command);
                    DataTable dt = new DataTable();
                    adapter.Fill(dt);

                    dataGridViewBiscuiti.DataSource = dt;
                }
                catch (Exception ex)
                {
                    MessageBox.Show("A apărut o eroare: " + ex.Message);
                }
            }
        }

        private void dataGridViewBiscuiti_SelectionChanged(object sender, EventArgs e)
        {

        }

        private void dataGridViewProducatori_SelectionChanged(object sender, EventArgs e)
        {
            if (dataGridViewProducatori.SelectedRows.Count > 0)
            {
                DataGridViewRow selectedRow = dataGridViewProducatori.SelectedRows[0];
                int codProducator = Convert.ToInt32(selectedRow.Cells["cod_p"].Value);

                IncarcaBiscuitiProducator(codProducator);
            }
        }

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            // Verificați dacă un producător este selectat în dataGridViewProducatori
            if (dataGridViewProducatori.SelectedRows.Count > 0)
            {
                // Obțineți codul producătorului selectat
                int codProducator = Convert.ToInt32(dataGridViewProducatori.SelectedRows[0].Cells["cod_p"].Value);

                // Obțineți valorile din TextBox-uri
                string nume = textBoxNume.Text;
                int calorii = Convert.ToInt32(textBoxCalorii.Text);
                float pret = Convert.ToSingle(textBoxPret.Text);

                // Conectați-vă la baza de date și inserați biscuitul
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    string insertQuery = "INSERT INTO Biscuiti (nume_b, nr_calorii, pret, cod_p) VALUES (@nume, @calorii, @pret, @codProducator)";
                    SqlCommand command = new SqlCommand(insertQuery, connection);
                    command.Parameters.AddWithValue("@nume", nume);
                    command.Parameters.AddWithValue("@calorii", calorii);
                    command.Parameters.AddWithValue("@pret", pret);
                    command.Parameters.AddWithValue("@codProducator", codProducator);
                    command.ExecuteNonQuery();
                }

                // Actualizați dataGridViewBiscuiti cu biscuiții actualizați
                UpdateBiscuitiGridView(codProducator);
            }
            else
            {
                MessageBox.Show("Vă rugăm să selectați un producător în dataGridViewProducatori.");
            }
        }

        private void UpdateBiscuitiGridView(int codProducator)
        {
            if (ds == null)
            {
                ds = new DataSet();
            }

            if (!ds.Tables.Contains("Biscuiti"))
            {
                ds.Tables.Add("Biscuiti");
            }

            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();
                string selectQuery = "SELECT cod_b, nume_b, nr_calorii, pret FROM Biscuiti WHERE cod_p = @codProducator";
                SqlCommand command = new SqlCommand(selectQuery, connection);
                command.Parameters.AddWithValue("@codProducator", codProducator);
                SqlDataAdapter adapter = new SqlDataAdapter(command);
                ds.Tables["Biscuiti"].Clear();
                adapter.Fill(ds, "Biscuiti");
                dataGridViewBiscuiti.DataSource = ds.Tables["Biscuiti"];
            }
        }

        private void buttonUpdate_Click(object sender, EventArgs e)
        {
            // Verificăm dacă un biscuit este selectat
            if (dataGridViewBiscuiti.SelectedRows.Count > 0)
            {
                DataGridViewRow selectedRow = dataGridViewBiscuiti.SelectedRows[0];

                // Obținem valorile din TextBox-uri
                string numeBiscuit = textBoxNume.Text;
                int nrCalorii = Convert.ToInt32(textBoxCalorii.Text);
                double pret = Convert.ToDouble(textBoxPret.Text);

                // Obținem codul biscuitului selectat
                int codBiscuit = Convert.ToInt32(selectedRow.Cells["cod_b"].Value);

                // Conectare la baza de date și actualizarea biscuitului
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    string updateQuery = "UPDATE Biscuiti SET nume_b = @numeBiscuit, nr_calorii = @nrCalorii, pret = @pret WHERE cod_b = @codBiscuit";
                    SqlCommand command = new SqlCommand(updateQuery, connection);
                    command.Parameters.AddWithValue("@numeBiscuit", numeBiscuit);
                    command.Parameters.AddWithValue("@nrCalorii", nrCalorii);
                    command.Parameters.AddWithValue("@pret", pret);
                    command.Parameters.AddWithValue("@codBiscuit", codBiscuit);
                    command.ExecuteNonQuery();
                }

                // Actualizăm GridView-ul cu biscuiți
                int codProducator = Convert.ToInt32(dataGridViewProducatori.SelectedRows[0].Cells["cod_p"].Value);
                UpdateBiscuitiGridView(codProducator);
            }
            else
            {
                MessageBox.Show("Vă rugăm să selectați un biscuit.");
            }
        }

        private void buttonDelete_Click(object sender, EventArgs e)
        {
            // Verificăm dacă un biscuit este selectat
            if (dataGridViewBiscuiti.SelectedRows.Count > 0)
            {
                DataGridViewRow selectedRow = dataGridViewBiscuiti.SelectedRows[0];

                // Obținem codul biscuitului selectat
                int codBiscuit = Convert.ToInt32(selectedRow.Cells["cod_b"].Value);

                // Conectare la baza de date și ștergerea biscuitului
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    string deleteQuery = "DELETE FROM Biscuiti WHERE cod_b = @codBiscuit";
                    SqlCommand command = new SqlCommand(deleteQuery, connection);
                    command.Parameters.AddWithValue("@codBiscuit", codBiscuit);
                    command.ExecuteNonQuery();
                }

                // Actualizăm GridView-ul cu biscuiți
                int codProducator = Convert.ToInt32(dataGridViewProducatori.SelectedRows[0].Cells["cod_p"].Value);
                UpdateBiscuitiGridView(codProducator);
            }
            else
            {
                MessageBox.Show("Vă rugăm să selectați un biscuit.");
            }
        }

    }
}