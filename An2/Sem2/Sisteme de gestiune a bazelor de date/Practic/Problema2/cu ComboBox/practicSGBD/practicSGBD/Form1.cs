using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace practicSGBD
{
    public partial class Form1 : Form
    {
        
        SqlConnection connectionString = new SqlConnection("Data Source=DESKTOP-EP7U088\\SQLEXPRESS;Initial Catalog=Problema2;Integrated Security=True");
        SqlDataAdapter dataAdapter = new SqlDataAdapter();
        DataSet dataSet = new DataSet();
        DataSet dataSet2 = new DataSet();
        BindingSource bindingSource = new BindingSource();
        
        public Form1()
        {
            InitializeComponent();
        }
        
        
        
        private void handleConnectionButton(object sender, EventArgs e)
        {
            dataAdapter.SelectCommand = new SqlCommand("select * from Artisti", connectionString);
            dataSet.Clear();
            dataAdapter.Fill(dataSet);

            // dataGridView1.DataSource = dataSet.Tables[0];
            // bindingSource.DataSource = dataSet.Tables[0];
            comboBox1.DataSource = dataSet.Tables[0];
            comboBox1.DisplayMember="nume_artist";
            comboBox1.ValueMember="cod_artist";
        }
        
        
        private void getChildrenByParentId(int idParinte)
        {
            dataAdapter.SelectCommand = new SqlCommand("select * from Melodii where cod_artist=@id", connectionString);
            dataAdapter.SelectCommand.Parameters.AddWithValue("@id", idParinte);
            dataSet2.Clear();

            dataAdapter.Fill(dataSet2);
            dataGridView2.DataSource = dataSet2.Tables[0];
        }
        
        
        private void handleParentSelection(object sender, EventArgs e)
        {
            // if (dataGridView1.SelectedRows.Count != 1) return;
            // int idParinte = Int32.Parse(dataGridView1.SelectedRows[0].Cells[0].Value.ToString());
            int idParinte=(int)comboBox1.SelectedValue;
            textFieldID.Text = idParinte.ToString();
            getChildrenByParentId(idParinte);
        }
        
        
        
        private void handleAddButton(object sender, EventArgs e)
        { 
            try
            {
                connectionString.Open();
                dataAdapter.InsertCommand = new SqlCommand(
                    "insert into Melodii(titlu,an_lansare,durata,cod_artist)" +
                    "values(@titlu,@an_lansare,@durata,@idParinte)", connectionString);
                dataAdapter.InsertCommand.Parameters.AddWithValue("@titlu", textFieldTitlu.Text);
                dataAdapter.InsertCommand.Parameters.AddWithValue("@an_lansare", textFieldAnLansare.Text);
                dataAdapter.InsertCommand.Parameters.AddWithValue("@durata", textFieldDurata.Text);
                dataAdapter.InsertCommand.Parameters.AddWithValue("@idParinte", textFieldID.Text);

                if (textFieldTitlu.Text != "" && textFieldAnLansare.Text != "" && textFieldDurata.Text!="")
                {
                    dataAdapter.InsertCommand.ExecuteNonQuery();
                    getChildrenByParentId(Int32.Parse(textFieldID.Text));
                    MessageBox.Show("A fost adaugata o noua melodie.");
                }
                else 
                    MessageBox.Show("Nu am putut adauga melodia. :(");
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            finally
            {
                connectionString.Close();
                textFieldTitlu.Clear();
                textFieldAnLansare.Clear();
                textFieldDurata.Clear();
            }
        }

        
        
        private void handleDeleteButton(object sender, EventArgs e)
        {
            if (dataGridView2.SelectedRows.Count!= 1) return;
            try
            {
                connectionString.Open();
                dataAdapter.DeleteCommand = new SqlCommand("delete from Melodii where cod_melodie=@idCopil", connectionString);

                if (dataGridView2.SelectedRows.Count != 1) return;
                int idCopil=Int32.Parse(dataGridView2.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.DeleteCommand.Parameters.AddWithValue("@idCopil", idCopil);
                dataAdapter.DeleteCommand.ExecuteNonQuery();
                getChildrenByParentId(Int32.Parse(textFieldID.Text)); 
                MessageBox.Show("A fost stearsa o melodie.");
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            finally
            {
                connectionString.Close();
            }
        }
        
        
        
        private void handleUpdateButton(object sender, EventArgs e)
        { 
            if (dataGridView2.SelectedRows.Count!=1) return;
            {
                try
                {
                    connectionString.Open();
                    dataAdapter.UpdateCommand = new SqlCommand(
                        "update Melodii set titlu=@titlu, an_lansare=@anLansare, durata=@durata " +
                        "where cod_melodie=@idCopil", connectionString);

                    dataAdapter.UpdateCommand.Parameters.AddWithValue("@titlu", textFieldTitlu.Text);
                    dataAdapter.UpdateCommand.Parameters.AddWithValue("@anLansare", textFieldAnLansare.Text);
                    dataAdapter.UpdateCommand.Parameters.AddWithValue("@durata", textFieldDurata.Text);
                    int idCopil=Int32.Parse(dataGridView2.SelectedRows[0].Cells[0].Value.ToString());
                    dataAdapter.UpdateCommand.Parameters.AddWithValue("@idCopil", idCopil);

                    if (textFieldTitlu.Text != "" && textFieldAnLansare.Text != "" && textFieldDurata.Text!="")
                    {
                        dataAdapter.UpdateCommand.ExecuteNonQuery();
                        getChildrenByParentId(Int32.Parse(textFieldID.Text));
                        MessageBox.Show("A fost actualizata o melodie.");
                    }
                    else 
                        MessageBox.Show("Nu am putut actualiza melodia. :(");
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
                finally
                {
                    connectionString.Close();
                    textFieldTitlu.Clear();
                    textFieldAnLansare.Clear();
                    textFieldDurata.Clear();
                }
            }
        }
    }
}