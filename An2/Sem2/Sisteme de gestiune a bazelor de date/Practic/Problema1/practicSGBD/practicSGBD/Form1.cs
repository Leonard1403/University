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
        
        SqlConnection connectionString = new SqlConnection("Data Source=DESKTOP-EP7U088\\SQLEXPRESS;Initial Catalog=Problema1;Integrated Security=True");
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
            dataAdapter.SelectCommand = new SqlCommand("select * from Cofetarii", connectionString);
            dataSet.Clear();
            dataAdapter.Fill(dataSet);

            dataGridView1.DataSource = dataSet.Tables[0];
            bindingSource.DataSource = dataSet.Tables[0];
        }
        
        
        private void getChildrenByParentId(int idCofetarie)
        {
            dataAdapter.SelectCommand = new SqlCommand("select * from Briose where cod_cofetarie=@id", connectionString);
            dataAdapter.SelectCommand.Parameters.AddWithValue("@id", idCofetarie);
            dataSet2.Clear();

            dataAdapter.Fill(dataSet2);
            dataGridView2.DataSource = dataSet2.Tables[0];
        }
        
        
        private void handleParentSelection(object sender, EventArgs e)
        {
            if (dataGridView1.SelectedRows.Count != 1) return;
            int idCofetarie = Int32.Parse(dataGridView1.SelectedRows[0].Cells[0].Value.ToString());
            textFieldID.Text = idCofetarie.ToString();
            getChildrenByParentId(idCofetarie);
        }
        
        
        
        private void handleAddButton(object sender, EventArgs e)
        { 
            try
            {
                connectionString.Open();
                dataAdapter.InsertCommand = new SqlCommand(
                    "insert into Briose(nume_briosa,descriere,pret,cod_cofetarie)" +
                    "values(@nume,@descriere,@pret,@idCofetarie)", connectionString);
                dataAdapter.InsertCommand.Parameters.AddWithValue("@nume", textFieldNume.Text);
                dataAdapter.InsertCommand.Parameters.AddWithValue("@descriere", textFieldDescriere.Text);
                dataAdapter.InsertCommand.Parameters.AddWithValue("@pret", Int32.Parse(textFieldPret.Text));
                dataAdapter.InsertCommand.Parameters.AddWithValue("@idCofetarie", textFieldID.Text);

                if (textFieldNume.Text != "" && textFieldDescriere.Text != "" && Int32.Parse(textFieldPret.Text)>0)
                {
                    dataAdapter.InsertCommand.ExecuteNonQuery();
                    getChildrenByParentId(Int32.Parse(textFieldID.Text)); //refresh
                    MessageBox.Show("A fost adaugata o noua briosa.");
                }
                else 
                    MessageBox.Show("Nu am putut adauga briosa. :(");
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            finally
            {
                connectionString.Close();
                textFieldNume.Clear();
                textFieldDescriere.Clear();
                textFieldPret.Clear();
            }
        }

        
        
        private void handleDeleteButton(object sender, EventArgs e)
        {
            if (dataGridView2.SelectedRows.Count!= 1) return;
            try
            {
                connectionString.Open();
                dataAdapter.DeleteCommand = new SqlCommand("delete from Briose where cod_briosa=@idBriosa", connectionString);

                if (dataGridView2.SelectedRows.Count != 1) return;
                int idBriosa=Int32.Parse(dataGridView2.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.DeleteCommand.Parameters.AddWithValue("@idBriosa", idBriosa);
                dataAdapter.DeleteCommand.ExecuteNonQuery();
                getChildrenByParentId(Int32.Parse(dataGridView1.SelectedRows[0].Cells[0].Value.ToString())); 
                MessageBox.Show("A fost stearsa o briosa.");
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
                        "update Briose set nume_briosa=@nume, descriere=@descriere, pret=@pret " +
                        "where cod_briosa=@idBriosa", connectionString);

                    dataAdapter.UpdateCommand.Parameters.AddWithValue("@nume", textFieldNume.Text);
                    dataAdapter.UpdateCommand.Parameters.AddWithValue("@descriere", textFieldDescriere.Text);
                    dataAdapter.UpdateCommand.Parameters.AddWithValue("@pret", textFieldPret.Text);
                    int idBriosa = Int32.Parse(dataGridView2.SelectedRows[0].Cells[0].Value.ToString());
                    dataAdapter.UpdateCommand.Parameters.AddWithValue("@idBriosa", idBriosa);

                    if (textFieldNume.Text != "" && textFieldDescriere.Text != "" && Int32.Parse(textFieldPret.Text) > 0)
                    {
                        dataAdapter.UpdateCommand.ExecuteNonQuery();
                        getChildrenByParentId(Int32.Parse(dataGridView1.SelectedRows[0].Cells[0].Value.ToString()));
                        MessageBox.Show("A fost actualizata o briosa.");
                    }
                    else 
                        MessageBox.Show("Nu am putut actualiza briosa. :(");
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
                finally
                {
                    connectionString.Close();
                    textFieldNume.Clear();
                    textFieldDescriere.Clear();
                    textFieldPret.Clear();
                }
            }
        }
    }
}