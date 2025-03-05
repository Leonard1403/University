using System.Data;
using System.Data.SqlClient;

namespace Problema_3
{
    public partial class Form1 : Form
    {
        string connectionString = @"Data Source=DESKTOP-UIQ2NDG;
        Initial Catalog=S1;Integrated Security=true;TrustServerCertificate=true;";

        DataSet ds = new DataSet();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                string query = "SELECT * FROM Facultati";

                SqlCommand command = new SqlCommand(query, connection);

                try
                {
                    connection.Open();

                    SqlDataAdapter adapter = new SqlDataAdapter(command);
                    DataTable dt = new DataTable();
                    adapter.Fill(dt);

                    dataGridViewFacultate.DataSource = dt;
                }
                catch (Exception ex)
                {
                    MessageBox.Show("A apărut o eroare: " + ex.Message);
                }
            }
        }

        private void IncarcaProfesoriFacultate(int codFacultate)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                string query = "SELECT * FROM Profesori WHERE Fid = @Fid";

                SqlCommand command = new SqlCommand(query, connection);
                command.Parameters.AddWithValue("@Fid", codFacultate);

                try
                {
                    connection.Open();

                    SqlDataAdapter adapter = new SqlDataAdapter(command);
                    DataTable dt = new DataTable();
                    adapter.Fill(dt);

                    dataGridViewProfesori.DataSource = dt;
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
            if (dataGridViewFacultate.SelectedRows.Count > 0)
            {
                DataGridViewRow selectedRow = dataGridViewFacultate.SelectedRows[0];
                int codProducator = Convert.ToInt32(selectedRow.Cells["Fid"].Value);

                IncarcaProfesoriFacultate(codProducator);
            }
        }

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            // Verificați dacă un producător este selectat în dataGridViewProducatori
            if (dataGridViewFacultate.SelectedRows.Count > 0)
            {
                // Obțineți codul producătorului selectat
                int Fid = Convert.ToInt32(dataGridViewFacultate.SelectedRows[0].Cells["Fid"].Value);

                // Obțineți valorile din TextBox-uri
                string Nume = textBoxNume.Text;
                string Prenume = textBoxPrenume.Text;
                string Titulatura = textBoxTitulatura.Text;
                string Gen = textBoxGen.Text;
                DateTime DataNastere = dateTimePicker.Value;

                // Conectați-vă la baza de date și inserați biscuitul
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    string insertQuery = "INSERT INTO Profesori (Nume, Prenume, Titulatura, Gen, DataNastere, Fid) VALUES (@Nume, @Prenume, @Titulatura, @Gen, @DataNastere, @Fid)";
                    SqlCommand command = new SqlCommand(insertQuery, connection);
                    command.Parameters.AddWithValue("@Nume", Nume);
                    command.Parameters.AddWithValue("@Prenume", Prenume);
                    command.Parameters.AddWithValue("@Titulatura", Titulatura);
                    command.Parameters.AddWithValue("@Gen", Gen);
                    command.Parameters.AddWithValue("@DataNastere", DataNastere);
                    command.Parameters.AddWithValue("@Fid", Fid);
                    command.ExecuteNonQuery();
                }

                // Actualizați dataGridViewBiscuiti cu biscuiții actualizați
                UpdateProfesoriGridView(Fid);
            }
            else
            {
                MessageBox.Show("Vă rugăm să selectați un producător în dataGridViewFacultati.");
            }
        }

        private void UpdateProfesoriGridView(int Fid)
        {
            if (ds == null)
            {
                ds = new DataSet();
            }

            if (!ds.Tables.Contains("Profesori"))
            {
                ds.Tables.Add("Profesori");
            }

            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();
                string selectQuery = "SELECT Pid, Nume, Prenume, Titulatura, Gen, DataNastere FROM Profesori WHERE Fid = @Fid";
                SqlCommand command = new SqlCommand(selectQuery, connection);
                command.Parameters.AddWithValue("@Fid", Fid);
                SqlDataAdapter adapter = new SqlDataAdapter(command);
                ds.Tables["Profesori"].Clear();
                adapter.Fill(ds, "Profesori");
                dataGridViewProfesori.DataSource = ds.Tables["Profesori"];
            }
        }

        private void buttonUpdate_Click(object sender, EventArgs e)
        {
            // Verificăm dacă un biscuit este selectat
            if (dataGridViewProfesori.SelectedRows.Count > 0)
            {
                DataGridViewRow selectedRow = dataGridViewProfesori.SelectedRows[0];

                // Obținem valorile din TextBox-uri

                string Nume = textBoxNume.Text;
                string Prenume = textBoxPrenume.Text;
                string Titulatura = textBoxTitulatura.Text;
                string Gen = textBoxGen.Text;
                DateTime DataNastere = dateTimePicker.Value;

                // Obținem codul biscuitului selectat
                int codProfesor = Convert.ToInt32(selectedRow.Cells["Pid"].Value);

                // Conectare la baza de date și actualizarea biscuitului
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    string updateQuery = "UPDATE Profesori SET Nume = @Nume, Prenume = @Prenume, Titulatura = @Titulatura, Gen = @Gen, DataNastere = @DataNastere WHERE Pid = @Pid";
                    SqlCommand command = new SqlCommand(updateQuery, connection);
                    command.Parameters.AddWithValue("@Nume", Nume);
                    command.Parameters.AddWithValue("@Prenume", Prenume);
                    command.Parameters.AddWithValue("@Titulatura", Titulatura);
                    command.Parameters.AddWithValue("@Gen", Gen);
                    command.Parameters.AddWithValue("@DataNastere", DataNastere);
                    command.Parameters.AddWithValue("@Pid", codProfesor);
                    command.ExecuteNonQuery();
                }

                // Actualizăm GridView-ul cu biscuiți
                int codProducator = Convert.ToInt32(dataGridViewFacultate.SelectedRows[0].Cells["Fid"].Value);
                UpdateProfesoriGridView(codProducator);
            }
            else
            {
                MessageBox.Show("Vă rugăm să selectați un profesor.");
            }
        }

        private void buttonDelete_Click(object sender, EventArgs e)
        {
            // Verificăm dacă un biscuit este selectat
            if (dataGridViewProfesori.SelectedRows.Count > 0)
            {
                DataGridViewRow selectedRow = dataGridViewProfesori.SelectedRows[0];

                // Obținem codul biscuitului selectat
                int codProfesor = Convert.ToInt32(selectedRow.Cells["Pid"].Value);

                // Conectare la baza de date și ștergerea biscuitului
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    string deleteQuery = "DELETE FROM Profesori WHERE Pid = @Pid";
                    SqlCommand command = new SqlCommand(deleteQuery, connection);
                    command.Parameters.AddWithValue("@Pid", codProfesor);
                    command.ExecuteNonQuery();
                }

                // Actualizăm GridView-ul cu biscuiți
                int codFacultate = Convert.ToInt32(dataGridViewFacultate.SelectedRows[0].Cells["Fid"].Value);
                UpdateProfesoriGridView(codFacultate);
            }
            else
            {
                MessageBox.Show("Vă rugăm să selectați un profesor.");
            }
        }

        private void dataGridViewFacultate_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}