using System.Data;
using System.Data.SqlClient;

namespace Problema_1
{
    public partial class Form1 : Form
    {
        string connectionString = @"Data Source=DESKTOP-UIQ2NDG;
        Initial Catalog=Problema1;Integrated Security=true;TrustServerCertificate=true;";

        Dictionary<int, string> cofetariiDictionary = new Dictionary<int, string>();

        DataSet ds = new DataSet();
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                string query = "SELECT cod_cofetarie, nume_cofetarie FROM Cofetarii";

                SqlCommand command = new SqlCommand(query, connection);

                try
                {
                    connection.Open();
                    SqlDataReader reader = command.ExecuteReader();

                    while (reader.Read())
                    {
                        int codCofetarie = reader.GetInt32(0);
                        string numeCofetarie = reader.GetString(1);
                        cofetariiDictionary.Add(codCofetarie, numeCofetarie);
                        comboBoxCofetarii.Items.Add(numeCofetarie);
                    }

                    reader.Close();
                }
                catch (Exception ex)
                {
                    MessageBox.Show("A apărut o eroare: " + ex.Message);
                }
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void comboBoxCofetarii_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBoxCofetarii.SelectedItem != null)
            {
                int selectedCodCofetarie = cofetariiDictionary.FirstOrDefault(x => x.Value == comboBoxCofetarii.SelectedItem.ToString()).Key;

                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    string query = "SELECT cod_briosa, nume_briosa, descriere, pret FROM Briose WHERE cod_cofetarie = @cod_cofetarie";

                    SqlCommand command = new SqlCommand(query, connection);
                    command.Parameters.AddWithValue("@cod_cofetarie", selectedCodCofetarie);

                    try
                    {
                        connection.Open();
                        SqlDataAdapter adapter = new SqlDataAdapter(command);
                        DataTable dataTable = new DataTable();
                        adapter.Fill(dataTable);

                        dataGridBriose.DataSource = dataTable;
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show("A apărut o eroare: " + ex.Message);
                    }
                }
            }
        }

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            if (comboBoxCofetarii.SelectedItem != null)
            {
                int selectedCodCofetarie = cofetariiDictionary.FirstOrDefault(x => x.Value == comboBoxCofetarii.SelectedItem.ToString()).Key;
                string numeBriosa = textBoxNume.Text;
                string descriere = textBoxDescriere.Text;
                decimal pret;
                if (decimal.TryParse(textBoxPret.Text, out pret))
                {
                    // Executați codul pentru a adăuga briosa în baza de date
                    AdaugaBriosa(selectedCodCofetarie, numeBriosa, descriere, pret);
                }
                else
                {
                    MessageBox.Show("Pretul trebuie sa fie un numar valid.");
                }
            }
            else
            {
                MessageBox.Show("Selectati o cofetarie.");
            }
        }

        private void AdaugaBriosa(int codCofetarie, string numeBriosa, string descriere, decimal pret)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                string query = "INSERT INTO Briose (nume_briosa, descriere, pret, cod_cofetarie) VALUES (@nume_briosa, @descriere, @pret, @cod_cofetarie)";

                SqlCommand command = new SqlCommand(query, connection);
                command.Parameters.AddWithValue("@nume_briosa", numeBriosa);
                command.Parameters.AddWithValue("@descriere", descriere);
                command.Parameters.AddWithValue("@pret", pret);
                command.Parameters.AddWithValue("@cod_cofetarie", codCofetarie);

                try
                {
                    connection.Open();
                    int rowsAffected = command.ExecuteNonQuery();

                    if (rowsAffected > 0)
                    {
                        MessageBox.Show("Briosa a fost adaugata cu succes la cofetarie.");
                        LoadBrioseByCofetarie(codCofetarie); // Reîncarcă briosele pentru cofetaria selectată
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show("A apărut o eroare: " + ex.Message);
                }
            }
        }

        private void LoadBrioseByCofetarie(int codCofetarie)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                string query = "SELECT cod_briosa, nume_briosa, descriere, pret FROM Briose WHERE cod_cofetarie = @cod_cofetarie";

                SqlCommand command = new SqlCommand(query, connection);
                command.Parameters.AddWithValue("@cod_cofetarie", codCofetarie);

                try
                {
                    connection.Open();
                    SqlDataAdapter adapter = new SqlDataAdapter(command);
                    DataTable dataTable = new DataTable();
                    adapter.Fill(dataTable);

                    dataGridBriose.DataSource = dataTable;
                }
                catch (Exception ex)
                {
                    MessageBox.Show("A apărut o eroare: " + ex.Message);
                }
            }
        }

        private void buttonUpdate_Click(object sender, EventArgs e)
        {
            if (dataGridBriose.SelectedRows.Count > 0)
            {
                int rowIndex = dataGridBriose.SelectedRows[0].Index;
                DataGridViewRow selectedRow = dataGridBriose.Rows[rowIndex];

                int codBriosa = Convert.ToInt32(selectedRow.Cells["cod_briosa"].Value);
                string numeBriosa = textBoxNume.Text;
                string descriere = textBoxDescriere.Text;
                decimal pret;
                if (decimal.TryParse(textBoxPret.Text, out pret))
                {
                    // Executați codul pentru a actualiza briosa în baza de date
                    ActualizeazaBriosa(codBriosa, numeBriosa, descriere, pret);
                }
                else
                {
                    MessageBox.Show("Pretul trebuie sa fie un numar valid.");
                }
            }
            else
            {
                MessageBox.Show("Selectati o briosa pentru a o actualiza.");
            }
        }

        private void ActualizeazaBriosa(int codBriosa, string numeBriosa, string descriere, decimal pret)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                string query = "UPDATE Briose SET nume_briosa = @nume_briosa, descriere = @descriere, pret = @pret WHERE cod_briosa = @cod_briosa";

                SqlCommand command = new SqlCommand(query, connection);
                command.Parameters.AddWithValue("@nume_briosa", numeBriosa);
                command.Parameters.AddWithValue("@descriere", descriere);
                command.Parameters.AddWithValue("@pret", pret);
                command.Parameters.AddWithValue("@cod_briosa", codBriosa);

                try
                {
                    connection.Open();
                    int rowsAffected = command.ExecuteNonQuery();

                    if (rowsAffected > 0)
                    {
                        MessageBox.Show("Briosa a fost actualizata cu succes.");
                        // Reîmprospătați datagridview sau alte acțiuni necesare după actualizarea cu succes a briosei
                        int codCofetarie = cofetariiDictionary.FirstOrDefault(x => x.Value == comboBoxCofetarii.SelectedItem.ToString()).Key;
                        LoadBrioseByCofetarie(codCofetarie);
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show("A apărut o eroare: " + ex.Message);
                }
            }
        }

        private void buttonDelete_Click(object sender, EventArgs e)
        {
            if (dataGridBriose.SelectedRows.Count > 0)
            {
                int rowIndex = dataGridBriose.SelectedRows[0].Index;
                DataGridViewRow selectedRow = dataGridBriose.Rows[rowIndex];

                int codBriosa = Convert.ToInt32(selectedRow.Cells["cod_briosa"].Value);

                StergeBriosa(codBriosa);
            }
            else
            {
                MessageBox.Show("Selectați o prăjitură pentru a o șterge.");
            }
        }

        private void StergeBriosa(int codBriosa)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                string query = "DELETE FROM Briose WHERE cod_briosa = @cod_briosa";

                SqlCommand command = new SqlCommand(query, connection);
                command.Parameters.AddWithValue("@cod_briosa", codBriosa);

                try
                {
                    connection.Open();
                    int rowsAffected = command.ExecuteNonQuery();

                    if (rowsAffected > 0)
                    {
                        MessageBox.Show("Prăjitura a fost ștearsă cu succes.");
                        int codCofetarie = cofetariiDictionary.FirstOrDefault(x => x.Value == comboBoxCofetarii.SelectedItem.ToString()).Key;
                        LoadBrioseByCofetarie(codCofetarie);
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show("A apărut o eroare: " + ex.Message);
                }
            }
        }

    }
}