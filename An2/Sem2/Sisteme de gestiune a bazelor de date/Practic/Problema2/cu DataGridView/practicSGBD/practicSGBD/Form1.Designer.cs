using System;
using System.Windows.Forms;

namespace practicSGBD
{
    public partial class Form1 : Form
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }

            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.dataGridView2 = new System.Windows.Forms.DataGridView();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.connectionButton = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.textFieldTitlu = new System.Windows.Forms.TextBox();
            this.textFieldAnLansare = new System.Windows.Forms.TextBox();
            this.textFieldDurata = new System.Windows.Forms.TextBox();
            this.textFieldID = new System.Windows.Forms.TextBox();
            this.addButton = new System.Windows.Forms.Button();
            this.updateButton = new System.Windows.Forms.Button();
            this.deleteButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView2)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridView1
            // 
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Location = new System.Drawing.Point(12, 139);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.RowTemplate.Height = 24;
            this.dataGridView1.Size = new System.Drawing.Size(673, 293);
            this.dataGridView1.TabIndex = 0;
            this.dataGridView1.SelectionChanged += new System.EventHandler(this.handleParentSelection);
            // 
            // dataGridView2
            // 
            this.dataGridView2.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView2.Location = new System.Drawing.Point(739, 139);
            this.dataGridView2.Name = "dataGridView2";
            this.dataGridView2.RowTemplate.Height = 24;
            this.dataGridView2.Size = new System.Drawing.Size(801, 238);
            this.dataGridView2.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.Location = new System.Drawing.Point(250, 103);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(100, 23);
            this.label1.TabIndex = 2;
            this.label1.Text = "Artisti";
            // 
            // label2
            // 
            this.label2.Location = new System.Drawing.Point(983, 103);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(100, 23);
            this.label2.TabIndex = 3;
            this.label2.Text = "Melodii";
            // 
            // connectionButton
            // 
            this.connectionButton.Location = new System.Drawing.Point(631, 23);
            this.connectionButton.Name = "connectionButton";
            this.connectionButton.Size = new System.Drawing.Size(197, 64);
            this.connectionButton.TabIndex = 4;
            this.connectionButton.Text = "Conectare";
            this.connectionButton.UseVisualStyleBackColor = true;
            this.connectionButton.Click += new System.EventHandler(this.handleConnectionButton);
            // 
            // label3
            // 
            this.label3.Location = new System.Drawing.Point(691, 420);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(137, 23);
            this.label3.TabIndex = 5;
            this.label3.Text = "Titlu";
            this.label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label4
            // 
            this.label4.Location = new System.Drawing.Point(691, 453);
            this.label4.Name = "label4";
            this.label4.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.label4.Size = new System.Drawing.Size(137, 23);
            this.label4.TabIndex = 6;
            this.label4.Text = "An lansare";
            this.label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label5
            // 
            this.label5.Location = new System.Drawing.Point(691, 488);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(137, 23);
            this.label5.TabIndex = 7;
            this.label5.Text = "Durata";
            this.label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label8
            // 
            this.label8.Location = new System.Drawing.Point(1048, 493);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(116, 23);
            this.label8.TabIndex = 10;
            this.label8.Text = "Cod artist";
            // 
            // textFieldTitlu
            // 
            this.textFieldTitlu.Location = new System.Drawing.Point(834, 421);
            this.textFieldTitlu.Name = "textFieldTitlu";
            this.textFieldTitlu.Size = new System.Drawing.Size(176, 22);
            this.textFieldTitlu.TabIndex = 11;
            // 
            // textFieldAnLansare
            // 
            this.textFieldAnLansare.Location = new System.Drawing.Point(834, 454);
            this.textFieldAnLansare.Name = "textFieldAnLansare";
            this.textFieldAnLansare.Size = new System.Drawing.Size(176, 22);
            this.textFieldAnLansare.TabIndex = 12;
            // 
            // textFieldDurata
            // 
            this.textFieldDurata.Location = new System.Drawing.Point(834, 493);
            this.textFieldDurata.Name = "textFieldDurata";
            this.textFieldDurata.Size = new System.Drawing.Size(176, 22);
            this.textFieldDurata.TabIndex = 13;
            // 
            // textFieldID
            // 
            this.textFieldID.Location = new System.Drawing.Point(1170, 493);
            this.textFieldID.Name = "textFieldID";
            this.textFieldID.Size = new System.Drawing.Size(176, 22);
            this.textFieldID.TabIndex = 16;
            // 
            // addButton
            // 
            this.addButton.Location = new System.Drawing.Point(509, 612);
            this.addButton.Name = "addButton";
            this.addButton.Size = new System.Drawing.Size(197, 34);
            this.addButton.TabIndex = 17;
            this.addButton.Text = "Add";
            this.addButton.UseVisualStyleBackColor = true;
            this.addButton.Click += new System.EventHandler(this.handleAddButton);
            // 
            // updateButton
            // 
            this.updateButton.Location = new System.Drawing.Point(785, 612);
            this.updateButton.Name = "updateButton";
            this.updateButton.Size = new System.Drawing.Size(197, 34);
            this.updateButton.TabIndex = 18;
            this.updateButton.Text = "Update";
            this.updateButton.UseVisualStyleBackColor = true;
            this.updateButton.Click += new System.EventHandler(this.handleUpdateButton);
            // 
            // deleteButton
            // 
            this.deleteButton.Location = new System.Drawing.Point(1080, 612);
            this.deleteButton.Name = "deleteButton";
            this.deleteButton.Size = new System.Drawing.Size(197, 34);
            this.deleteButton.TabIndex = 19;
            this.deleteButton.Text = "Delete";
            this.deleteButton.UseVisualStyleBackColor = true;
            this.deleteButton.Click += new System.EventHandler(this.handleDeleteButton);
            // 
            // Form1
            // 
            this.BackColor = System.Drawing.SystemColors.Control;
            this.ClientSize = new System.Drawing.Size(1583, 734);
            this.Controls.Add(this.deleteButton);
            this.Controls.Add(this.updateButton);
            this.Controls.Add(this.addButton);
            this.Controls.Add(this.textFieldID);
            this.Controls.Add(this.textFieldDurata);
            this.Controls.Add(this.textFieldAnLansare);
            this.Controls.Add(this.textFieldTitlu);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.connectionButton);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.dataGridView2);
            this.Controls.Add(this.dataGridView1);
            this.Location = new System.Drawing.Point(15, 15);
            this.Name = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();
        }

        private System.Windows.Forms.Button addButton;
        private System.Windows.Forms.Button updateButton;
        private System.Windows.Forms.Button deleteButton;

        private System.Windows.Forms.TextBox textFieldTitlu;
        private System.Windows.Forms.TextBox textFieldAnLansare;
        private System.Windows.Forms.TextBox textFieldDurata;
        private System.Windows.Forms.TextBox textFieldID;

        private System.Windows.Forms.Label label8;

        private System.Windows.Forms.Label label5;

        private System.Windows.Forms.Label label4;

        private System.Windows.Forms.Label label3;

        private System.Windows.Forms.Button connectionButton;

        private System.Windows.Forms.Label label1;

        private System.Windows.Forms.Label label2;

        private System.Windows.Forms.DataGridView dataGridView2;

        private System.Windows.Forms.DataGridView dataGridView1;

        private System.Windows.Forms.CheckBox checkBox1;

        #endregion


    }
}