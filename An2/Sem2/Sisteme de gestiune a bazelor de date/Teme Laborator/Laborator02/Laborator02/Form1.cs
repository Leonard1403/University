using System.Data;
using System.Configuration;
using Microsoft.Data.SqlClient;

namespace Laborator01
{
    public partial class Form1 : Form
    {
        /*
        string connectionString = @"Data Source=DESKTOP-UIQ2NDG;
        Initial Catalog=Farmacie;Integrated Security=true;TrustServerCertificate=true;";
        */

        string connectionString = ConfigurationManager.ConnectionStrings["cn"].ConnectionString;

        DataSet ds = new DataSet();
        SqlDataAdapter parentAdapter = new SqlDataAdapter();
        SqlDataAdapter childAdapter = new SqlDataAdapter();
        BindingSource parentBS = new BindingSource();
        BindingSource childBS = new BindingSource();

        string ParentTableName = ConfigurationManager.AppSettings["ParentTableName"];
        string ChildTableName = ConfigurationManager.AppSettings["ChildTableName"];
        int n = int.Parse(ConfigurationManager.AppSettings["ParentNumberOfColumns"]);
        int m = int.Parse(ConfigurationManager.AppSettings["ChildNumberOfColumns"]);
        List<string> ChildColumnNames = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));
        List<string> ParentColumnNames = new List<string>(ConfigurationManager.AppSettings["ParentColumnNames"].Split(','));

        // Declaram dictionarul in care vom stoca valorile control-urilor
        Dictionary<string, object> controlValues = new Dictionary<string, object>();

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
                    //MessageBox.Show(ParentTableName);
                    //MessageBox.Show(ChildTableName);

                    connection.Open();
                    MessageBox.Show(connection.State.ToString());
                    parentAdapter.SelectCommand = new SqlCommand("SELECT * FROM " +
                        ParentTableName, connection);
                    parentAdapter.Fill(ds, ParentTableName);
                    childAdapter.SelectCommand = new SqlCommand("SELECT * FROM " +
                        ChildTableName, connection);
                    childAdapter.Fill(ds, ChildTableName);
                    DataRelation dr = new DataRelation("FK_"+ParentTableName+"_"+ChildTableName, ds.Tables[ParentTableName].Columns[ParentColumnNames[0]], ds.Tables[ChildTableName].Columns[ChildColumnNames[m-1]]);
                    ds.Relations.Add(dr);
                    parentBS.DataSource = ds.Tables[ParentTableName];
                    dataGridParent.DataSource = parentBS;
                    childBS.DataSource = parentBS;
                    childBS.DataMember = "FK_" + ParentTableName + "_" + ChildTableName;
                    dataGridChild.DataSource = childBS;

                    // Creăm câte un label și un control corespunzător pentru fiecare coloană din tabelul copil
                    for (int i = 1; i < m - 1; i++)
                    {
                        // Creăm label-ul
                        Label label = new Label();
                        label.Text = ChildColumnNames[i];
                        label.Location = new Point(20, 50 + i * 25);
                        label.AutoSize = true;

                        // Creăm control-ul corespunzător (TextBox sau DatePicker)
                        Control control;
                        if (ChildColumnNames[i].ToLower().Contains("data") || ChildColumnNames[i].ToLower().Contains("date"))
                        {
                            // Dacă numele coloanei conține cuvântul "data" sau "date", creăm un DatePicker
                            DateTimePicker datePicker = new DateTimePicker();
                            datePicker.Name = "DatePicker" + i;
                            datePicker.Location = new Point(140, 50 + i * 25);
                            datePicker.Width = 150;
                            control = datePicker;

                            // Adaugam valoarea datei in dictionarul controlValues
                            controlValues.Add(datePicker.Name, datePicker.Value);
                        }
                        else
                        {
                            // Altfel, creăm un TextBox
                            TextBox textBox = new TextBox();
                            textBox.Name = "TextBox" + i;
                            textBox.Location = new Point(140, 50 + i * 25);
                            textBox.Width = 150;
                            control = textBox;

                            // Adaugam valoarea textului in dictionarul controlValues
                            controlValues.Add(textBox.Name, textBox.Text);
                        }

                        // Adăugăm label-ul și control-ul la formular
                        panel1.Controls.Add(label);
                        panel1.Controls.Add(control);
                    }

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
                    string sql = "DELETE FROM "+ChildTableName+ " WHERE "+ ChildColumnNames[0] +" = @idComanda";
                    SqlCommand command = new SqlCommand(sql, connection);

                    //command.Parameters.AddWithValue("@DataLivrare", dateTimePicker1.Value);
                    //command.Parameters.AddWithValue("@numeComenzi", textBox1.Text);
                    command.Parameters.AddWithValue("@idComanda", dataGridChild.CurrentRow.Cells[ChildColumnNames[0]].Value);
                    int rowsAffected = command.ExecuteNonQuery();
                    if (rowsAffected > 0)
                    {
                        MessageBox.Show("Stergere efectuată cu succes!");
                        // Refacem interogarea și reîncărcăm datele în grid-uri
                        childAdapter.SelectCommand = new SqlCommand("SELECT * FROM "+ ChildTableName, connection);
                        ds.Tables[ChildTableName].Clear();
                        childAdapter.Fill(ds, ChildTableName);
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
        }


        private void dataGridChild_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void dataGridChild_CellEndEdit(object sender, DataGridViewCellEventArgs e)
        {
            try
            {
                childAdapter.Update(ds, ParentTableName);
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

        private void button3_Click(object sender, EventArgs e)
        {
            try
            {
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    foreach (Control control in panel1.Controls)
                    {
                        if (control is TextBox textBox)
                        {
                            controlValues[textBox.Name] = textBox.Text;
                        }
                        else if (control is DateTimePicker datePicker)
                        {
                            controlValues[datePicker.Name] = datePicker.Value;
                        }
                    }

                    connection.Open();
                    string sql = "UPDATE " + ChildTableName + " SET ";

                    for (int i = 1; i < m - 1; i++)
                    {
                        sql += ChildColumnNames[i] + " = @" + ChildColumnNames[i];

                        if (i < m - 2)
                        {
                            sql += ", ";
                        }
                    }

                    sql += " WHERE " + ChildColumnNames[0] + " = @" + ChildColumnNames[0];
                    //MessageBox.Show(sql);

                    SqlCommand command = new SqlCommand(sql, connection);
                    for (int i = 1; i < m - 1; i++)
                    {
                        if (ChildColumnNames[i].ToLower().Contains("data") || ChildColumnNames[i].ToLower().Contains("date"))
                        {
                            command.Parameters.AddWithValue("@" + ChildColumnNames[i], controlValues["DatePicker" + i]);
                            //MessageBox.Show(controlValues["DatePicker" + i].ToString());
                        }
                        else
                        {
                            command.Parameters.AddWithValue("@" + ChildColumnNames[i], controlValues["TextBox" + i]);
                            //MessageBox.Show(controlValues["TextBox" + i].ToString());
                        }
                    }
                    //MessageBox.Show(dataGridChild.CurrentRow.Cells[ChildColumnNames[0]].Value.ToString());
                    command.Parameters.AddWithValue("@"+ChildColumnNames[0], dataGridChild.CurrentRow.Cells[ChildColumnNames[0]].Value);
                    int rowsAffected = command.ExecuteNonQuery();


                    if (rowsAffected > 0)
                    {
                        MessageBox.Show("Actualizare efectuată cu succes!");
                        // Refacem interogarea și reîncărcăm datele în grid-uri
                        childAdapter.SelectCommand = new SqlCommand("SELECT * FROM "+ChildTableName, connection);
                        ds.Tables[ChildTableName].Clear();
                        childAdapter.Fill(ds, ChildTableName);
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
                foreach (Control control in panel1.Controls)
                {
                    if (control is TextBox textBox)
                    {
                        controlValues[textBox.Name] = textBox.Text;
                    }
                    else if (control is DateTimePicker datePicker)
                    {
                        controlValues[datePicker.Name] = datePicker.Value;
                    }
                }

                // obținem id-ul comenzii
                int idComanda = 0;
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    SqlCommand cmd = new SqlCommand("SELECT MAX("+ChildColumnNames[0]+") FROM "+ChildTableName, connection);
                    //SqlCommand cmd = new SqlCommand("SELECT MAX(idComanda) FROM Comenzi", connection);
                    object result = cmd.ExecuteScalar();
                    if (result != null && result != DBNull.Value)
                    {
                        idComanda = (int)result;
                    }
                }
                idComanda++;

                // obținem id-ul clientului din selecția curentă
                int idClient = (int)dataGridParent.CurrentRow.Cells[ParentColumnNames[0]].Value;

                // adăugăm o nouă înregistrare în DataSet
                DataRow newRow = ds.Tables[ChildTableName].NewRow();
                //MessageBox.Show(ChildColumnNames[0]);
                newRow[ChildColumnNames[0]] = idComanda;
                //MessageBox.Show(idComanda.ToString());

                for(int i = 1; i < m - 1; i++)
                {
                    if (ChildColumnNames[i].ToLower().Contains("data") || ChildColumnNames[i].ToLower().Contains("date")) {
                        newRow[ChildColumnNames[i]] = controlValues["DatePicker" + i];
                        //MessageBox.Show(controlValues["DatePicker" + i].ToString());
                    }
                    else
                    {
                        newRow[ChildColumnNames[i]] = controlValues["TextBox" + i];
                        //MessageBox.Show(controlValues["TextBox" + i].ToString());
                    }
                }
                
                newRow[ChildColumnNames[m-1]] = idClient;

                ds.Tables[ChildTableName].Rows.Add(newRow);

                // actualizăm baza de date
                // build the INSERT query dynamically
                string sql = "INSERT INTO " + ChildTableName + " (";

                for (int i = 0; i < m; i++)
                {
                    sql += ChildColumnNames[i];

                    if (i < m - 1)
                    {
                        sql += ", ";
                    }
                }

                sql += ") VALUES (";

                for (int i = 0; i < m; i++)
                {
                    sql += "@" + ChildColumnNames[i];

                    if (i < m - 1)
                    {
                        sql += ", ";
                    }
                }

                sql += ")";
                MessageBox.Show(sql);

                childAdapter.InsertCommand = new SqlCommand(sql, new SqlConnection(connectionString));

                childAdapter.InsertCommand.Parameters.Add("@" + ChildColumnNames[0], SqlDbType.Int).Value = idComanda;
                for (int i = 1; i < m-1; i++)
                {
                    if (ChildColumnNames[i].ToLower().Contains("data") || ChildColumnNames[i].ToLower().Contains("date"))
                    {
                        childAdapter.InsertCommand.Parameters.Add("@" + ChildColumnNames[i], SqlDbType.DateTime).Value = controlValues["DatePicker" + i];
                    }
                    else if (ChildColumnNames[i].ToLower().Contains("nr") || ChildColumnNames[i].ToLower().Contains("numar"))
                    {
                        childAdapter.InsertCommand.Parameters.Add("@" + ChildColumnNames[i], SqlDbType.Int).Value = controlValues["TextBox" + i];
                    }
                    else
                    {
                        childAdapter.InsertCommand.Parameters.Add("@" + ChildColumnNames[i], SqlDbType.VarChar, 60).Value = controlValues["TextBox" + i];
                    }
                }
                childAdapter.InsertCommand.Parameters.Add("@" + ChildColumnNames[m-1], SqlDbType.Int).Value = idClient;

                childAdapter.Update(ds, ChildTableName);



                // reîncărcăm selecția pentru a reflecta adăugarea noii înregistrări
                childBS.DataSource = parentBS;
                childBS.DataMember = "FK_"+ParentTableName+"_"+ChildTableName;
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

        private void panel1_Paint_1(object sender, PaintEventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }
    }
}
