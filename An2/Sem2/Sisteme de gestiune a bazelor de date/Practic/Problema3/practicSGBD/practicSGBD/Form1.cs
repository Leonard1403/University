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
        
        SqlConnection connectionString = new SqlConnection("Data Source=DESKTOP-EP7U088\\SQLEXPRESS;Initial Catalog=Problema3;Integrated Security=True");
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
            dataAdapter.SelectCommand = new SqlCommand("select * from Producatori", connectionString);
            dataSet.Clear();
            dataAdapter.Fill(dataSet);

            // dataGridView1.DataSource = dataSet.Tables[0];
            // bindingSource.DataSource = dataSet.Tables[0];
            comboBox1.DataSource = dataSet.Tables[0];
            comboBox1.DisplayMember="nume_p";
            comboBox1.ValueMember="cod_p";
            comboBox1.DropDownStyle = ComboBoxStyle.DropDownList;
        }
        
        
        
        private void getChildrenByParentId(int idParinte)
        {
            dataAdapter.SelectCommand = new SqlCommand("select * from Biscuiti where cod_p=@id", connectionString);
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
                    "insert into Biscuiti(nume_b,nr_calorii,pret,cod_p)" +
                    "values(@numeB,@nrCalorii,@pret,@idParinte)", connectionString);
                dataAdapter.InsertCommand.Parameters.AddWithValue("@numeB", textFieldNume.Text);
                dataAdapter.InsertCommand.Parameters.AddWithValue("@nrCalorii", textFieldNrCalorii.Text);
                dataAdapter.InsertCommand.Parameters.AddWithValue("@pret", textFieldPret.Text);
                dataAdapter.InsertCommand.Parameters.AddWithValue("@idParinte", textFieldID.Text);

                if (textFieldNume.Text != "" && Int32.Parse(textFieldNrCalorii.Text)>0 && Int32.Parse(textFieldPret.Text)>0)
                {
                    dataAdapter.InsertCommand.ExecuteNonQuery();
                    getChildrenByParentId(Int32.Parse(textFieldID.Text));
                    MessageBox.Show("A fost adaugat un nou biscuite.");
                }
                else 
                    MessageBox.Show("Nu am putut adauga biscuitele. :(");
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            finally
            {
                connectionString.Close();
                textFieldNume.Clear();
                textFieldNrCalorii.Clear();
                textFieldPret.Clear();
            }
        }

        
        
        private void handleDeleteButton(object sender, EventArgs e)
        {
            if (dataGridView2.SelectedRows.Count!= 1) return;
            try
            {
                connectionString.Open();
                dataAdapter.DeleteCommand = new SqlCommand("delete from Biscuiti where cod_b=@idCopil", connectionString);

                if (dataGridView2.SelectedRows.Count != 1) return;
                int idCopil=Int32.Parse(dataGridView2.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.DeleteCommand.Parameters.AddWithValue("@idCopil", idCopil);
                dataAdapter.DeleteCommand.ExecuteNonQuery();
                getChildrenByParentId(Int32.Parse(textFieldID.Text)); 
                MessageBox.Show("A fost sters un biscuit.");
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
                        "update Biscuiti set nume_b=@numeB, nr_calorii=@nrCalorii, pret=@pret " +
                        "where cod_b=@idCopil", connectionString);
                    dataAdapter.UpdateCommand.Parameters.AddWithValue("@numeB", textFieldNume.Text);
                    dataAdapter.UpdateCommand.Parameters.AddWithValue("@nrCalorii", textFieldNrCalorii.Text);
                    dataAdapter.UpdateCommand.Parameters.AddWithValue("@pret", textFieldPret.Text);
                    int idCopil=Int32.Parse(dataGridView2.SelectedRows[0].Cells[0].Value.ToString());
                    dataAdapter.UpdateCommand.Parameters.AddWithValue("@idCopil", idCopil);
                    if (textFieldNume.Text != "" && Int32.Parse(textFieldNrCalorii.Text)>0 && Int32.Parse(textFieldPret.Text)>0)
                    {
                        dataAdapter.UpdateCommand.ExecuteNonQuery();
                        getChildrenByParentId(Int32.Parse(textFieldID.Text));
                        MessageBox.Show("A fost actualizat un biscuit.");
                    }
                    else 
                        MessageBox.Show("Nu am putut actualiza biscuitele. :(");
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
                finally
                {
                    connectionString.Close();
                    textFieldNume.Clear();
                    textFieldNrCalorii.Clear();
                    textFieldPret.Clear();
                }
            }
        }
    }
}