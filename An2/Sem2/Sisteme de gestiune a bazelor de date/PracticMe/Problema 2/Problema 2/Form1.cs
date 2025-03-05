using System.Data;
using System.Data.SqlClient;

namespace Problema_2
{
    public partial class Form1 : Form
    {
        string connectionString = @"Data Source=DESKTOP-UIQ2NDG;
        Initial Catalog=Problema2;Integrated Security=true;TrustServerCertificate=true;";

        DataSet ds = new DataSet();
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                string query = "SELECT cod_artist, nume_artist FROM Artisti";

                SqlCommand command = new SqlCommand(query, connection);

                try
                {
                    connection.Open();

                    SqlDataAdapter adapter = new SqlDataAdapter(command);
                    DataTable dt = new DataTable();
                    adapter.Fill(dt);

                    listBoxArtisti.DataSource = dt;
                    listBoxArtisti.DisplayMember = "nume_artist";
                    listBoxArtisti.ValueMember = "cod_artist";
                }
                catch (Exception ex)
                {
                    MessageBox.Show("A apărut o eroare: " + ex.Message);
                }
            }
        }

        private void listBoxArtisti_SelectedIndexChanged(object sender, EventArgs e)
        {
            int codArtist = 0;

            if (listBoxArtisti.SelectedItem != null)
            {
                DataRowView selectedRow = (DataRowView)listBoxArtisti.SelectedItem;
                codArtist = Convert.ToInt32(selectedRow.Row["cod_artist"]);
            }

            IncarcaMelodiiArtist(codArtist);
        }

        private void IncarcaMelodiiArtist(int codArtist)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                string query = @"SELECT cod_melodie, titlu, an_lansare, durata
                        FROM Melodii
                        WHERE cod_artist = @codArtist";

                SqlCommand command = new SqlCommand(query, connection);
                command.Parameters.AddWithValue("@codArtist", codArtist);

                try
                {
                    connection.Open();

                    SqlDataAdapter adapter = new SqlDataAdapter(command);
                    DataTable dt = new DataTable();
                    adapter.Fill(dt);

                    dataGridMelodii.DataSource = dt;
                }
                catch (Exception ex)
                {
                    MessageBox.Show("A apărut o eroare: " + ex.Message);
                }
            }
        }

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            // Verificăm dacă un artist este selectat
            if (listBoxArtisti.SelectedItem != null)
            {
                int codArtist = 0;
                DataRowView selectedRow = (DataRowView)listBoxArtisti.SelectedItem;
                codArtist = Convert.ToInt32(selectedRow.Row["cod_artist"]);

                // Obținem valorile din TextBox-uri
                string titlu = textBoxTitlu.Text;
                int anLansare = Convert.ToInt32(textBoxAn.Text);
                TimeSpan durata = TimeSpan.Parse(textBoxDurata.Text);

                // Conectare la baza de date și inserarea melodiei
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    string insertQuery = "INSERT INTO Melodii (titlu, an_lansare, durata, cod_artist) VALUES (@titlu, @anLansare, @durata, @codArtist)";
                    SqlCommand command = new SqlCommand(insertQuery, connection);
                    command.Parameters.AddWithValue("@titlu", titlu);
                    command.Parameters.AddWithValue("@anLansare", anLansare);
                    command.Parameters.AddWithValue("@durata", durata);
                    command.Parameters.AddWithValue("@codArtist", codArtist);
                    command.ExecuteNonQuery();
                }

                // Actualizăm GridView-ul cu melodii
                UpdateMelodiiGridView(codArtist);
            }
            else
            {
                MessageBox.Show("Vă rugăm să selectați un artist.");
            }
        }

        private void UpdateMelodiiGridView(int codArtist)
        {
            if (ds.Tables.Contains("Melodii"))
            {
                ds.Tables["Melodii"].Clear(); // Curățăm setul de date existent
            }
            else
            {
                DataTable melodiiTable = new DataTable("Melodii");
                ds.Tables.Add(melodiiTable);
            }

            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();
                string selectQuery = "SELECT cod_melodie, titlu, an_lansare, durata FROM Melodii WHERE cod_artist = @codArtist";
                SqlCommand command = new SqlCommand(selectQuery, connection);
                command.Parameters.AddWithValue("@codArtist", codArtist);
                SqlDataAdapter adapter = new SqlDataAdapter(command);
                adapter.Fill(ds.Tables["Melodii"]); // Umplem tabela "Melodii" în setul de date
                dataGridMelodii.DataSource = ds.Tables["Melodii"];
            }
        }

        private void buttonUpdate_Click(object sender, EventArgs e)
        {
            if (dataGridMelodii.SelectedRows.Count > 0)
            {
                // Verificați dacă o melodie este selectată în DataGridView
                DataGridViewRow selectedRow = dataGridMelodii.SelectedRows[0];
                int codMelodie = Convert.ToInt32(selectedRow.Cells["cod_melodie"].Value);

                // Obțineți valorile din TextBox-uri
                string titlu = textBoxTitlu.Text;
                int anLansare = Convert.ToInt32(textBoxAn.Text);
                TimeSpan durata = TimeSpan.Parse(textBoxDurata.Text);

                // Conectați-vă la baza de date și actualizați melodia
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    string updateQuery = @"UPDATE Melodii
                                   SET titlu = @titlu, an_lansare = @anLansare, durata = @durata
                                   WHERE cod_melodie = @codMelodie";
                    SqlCommand command = new SqlCommand(updateQuery, connection);
                    command.Parameters.AddWithValue("@titlu", titlu);
                    command.Parameters.AddWithValue("@anLansare", anLansare);
                    command.Parameters.AddWithValue("@durata", durata);
                    command.Parameters.AddWithValue("@codMelodie", codMelodie);
                    command.ExecuteNonQuery();
                }

                // Actualizați GridView-ul cu melodiile
                int codArtist = Convert.ToInt32(listBoxArtisti.SelectedValue);
                UpdateMelodiiGridView(codArtist);
            }
            else
            {
                MessageBox.Show("Vă rugăm să selectați o melodie din GridView.");
            }
        }

        private void buttonDelete_Click(object sender, EventArgs e)
        {
            if (dataGridMelodii.SelectedRows.Count > 0)
            {
                // Verificați dacă o melodie este selectată în DataGridView
                DataGridViewRow selectedRow = dataGridMelodii.SelectedRows[0];
                int codMelodie = Convert.ToInt32(selectedRow.Cells["cod_melodie"].Value);

                // Conectați-vă la baza de date și ștergeți melodia
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    string deleteQuery = "DELETE FROM Melodii WHERE cod_melodie = @codMelodie";
                    SqlCommand command = new SqlCommand(deleteQuery, connection);
                    command.Parameters.AddWithValue("@codMelodie", codMelodie);
                    command.ExecuteNonQuery();
                }

                // Actualizați GridView-ul cu melodiile
                int codArtist = Convert.ToInt32(listBoxArtisti.SelectedValue);
                UpdateMelodiiGridView(codArtist);
            }
            else
            {
                MessageBox.Show("Vă rugăm să selectați o melodie din GridView.");
            }
        }

    }
}