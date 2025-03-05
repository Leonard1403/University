namespace Problema_3
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dataGridViewFacultate = new System.Windows.Forms.DataGridView();
            this.dataGridViewProfesori = new System.Windows.Forms.DataGridView();
            this.textBoxNume = new System.Windows.Forms.TextBox();
            this.textBoxPrenume = new System.Windows.Forms.TextBox();
            this.textBoxTitulatura = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.buttonAdd = new System.Windows.Forms.Button();
            this.buttonUpdate = new System.Windows.Forms.Button();
            this.buttonDelete = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.textBoxGen = new System.Windows.Forms.TextBox();
            this.dateTimePicker = new System.Windows.Forms.DateTimePicker();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewFacultate)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewProfesori)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridViewFacultate
            // 
            this.dataGridViewFacultate.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewFacultate.Location = new System.Drawing.Point(12, 12);
            this.dataGridViewFacultate.Name = "dataGridViewFacultate";
            this.dataGridViewFacultate.RowHeadersWidth = 51;
            this.dataGridViewFacultate.RowTemplate.Height = 29;
            this.dataGridViewFacultate.Size = new System.Drawing.Size(360, 252);
            this.dataGridViewFacultate.TabIndex = 0;
            this.dataGridViewFacultate.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridViewFacultate_CellContentClick);
            this.dataGridViewFacultate.SelectionChanged += new System.EventHandler(this.dataGridViewProducatori_SelectionChanged);
            // 
            // dataGridViewProfesori
            // 
            this.dataGridViewProfesori.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewProfesori.Location = new System.Drawing.Point(412, 12);
            this.dataGridViewProfesori.Name = "dataGridViewProfesori";
            this.dataGridViewProfesori.RowHeadersWidth = 51;
            this.dataGridViewProfesori.RowTemplate.Height = 29;
            this.dataGridViewProfesori.Size = new System.Drawing.Size(376, 252);
            this.dataGridViewProfesori.TabIndex = 1;
            this.dataGridViewProfesori.SelectionChanged += new System.EventHandler(this.dataGridViewBiscuiti_SelectionChanged);
            // 
            // textBoxNume
            // 
            this.textBoxNume.Location = new System.Drawing.Point(247, 285);
            this.textBoxNume.Name = "textBoxNume";
            this.textBoxNume.Size = new System.Drawing.Size(125, 27);
            this.textBoxNume.TabIndex = 2;
            // 
            // textBoxPrenume
            // 
            this.textBoxPrenume.Location = new System.Drawing.Point(247, 318);
            this.textBoxPrenume.Name = "textBoxPrenume";
            this.textBoxPrenume.Size = new System.Drawing.Size(125, 27);
            this.textBoxPrenume.TabIndex = 3;
            // 
            // textBoxTitulatura
            // 
            this.textBoxTitulatura.Location = new System.Drawing.Point(247, 351);
            this.textBoxTitulatura.Name = "textBoxTitulatura";
            this.textBoxTitulatura.Size = new System.Drawing.Size(125, 27);
            this.textBoxTitulatura.TabIndex = 4;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(140, 285);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(49, 20);
            this.label1.TabIndex = 5;
            this.label1.Text = "Nume";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(140, 318);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(67, 20);
            this.label2.TabIndex = 6;
            this.label2.Text = "Prenume";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(140, 351);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(72, 20);
            this.label3.TabIndex = 7;
            this.label3.Text = "Titulatura";
            // 
            // buttonAdd
            // 
            this.buttonAdd.Location = new System.Drawing.Point(412, 285);
            this.buttonAdd.Name = "buttonAdd";
            this.buttonAdd.Size = new System.Drawing.Size(94, 29);
            this.buttonAdd.TabIndex = 8;
            this.buttonAdd.Text = "Add";
            this.buttonAdd.UseVisualStyleBackColor = true;
            this.buttonAdd.Click += new System.EventHandler(this.buttonAdd_Click);
            // 
            // buttonUpdate
            // 
            this.buttonUpdate.Location = new System.Drawing.Point(412, 320);
            this.buttonUpdate.Name = "buttonUpdate";
            this.buttonUpdate.Size = new System.Drawing.Size(94, 29);
            this.buttonUpdate.TabIndex = 9;
            this.buttonUpdate.Text = "Update";
            this.buttonUpdate.UseVisualStyleBackColor = true;
            this.buttonUpdate.Click += new System.EventHandler(this.buttonUpdate_Click);
            // 
            // buttonDelete
            // 
            this.buttonDelete.Location = new System.Drawing.Point(412, 355);
            this.buttonDelete.Name = "buttonDelete";
            this.buttonDelete.Size = new System.Drawing.Size(94, 29);
            this.buttonDelete.TabIndex = 10;
            this.buttonDelete.Text = "Delete";
            this.buttonDelete.UseVisualStyleBackColor = true;
            this.buttonDelete.Click += new System.EventHandler(this.buttonDelete_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(140, 384);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(35, 20);
            this.label4.TabIndex = 11;
            this.label4.Text = "Gen";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(140, 421);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(96, 20);
            this.label5.TabIndex = 12;
            this.label5.Text = "Data Nastere";
            // 
            // textBoxGen
            // 
            this.textBoxGen.Location = new System.Drawing.Point(247, 384);
            this.textBoxGen.Name = "textBoxGen";
            this.textBoxGen.Size = new System.Drawing.Size(125, 27);
            this.textBoxGen.TabIndex = 13;
            // 
            // dateTimePicker
            // 
            this.dateTimePicker.Location = new System.Drawing.Point(256, 421);
            this.dateTimePicker.Name = "dateTimePicker";
            this.dateTimePicker.Size = new System.Drawing.Size(250, 27);
            this.dateTimePicker.TabIndex = 15;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.dateTimePicker);
            this.Controls.Add(this.textBoxGen);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.buttonDelete);
            this.Controls.Add(this.buttonUpdate);
            this.Controls.Add(this.buttonAdd);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textBoxTitulatura);
            this.Controls.Add(this.textBoxPrenume);
            this.Controls.Add(this.textBoxNume);
            this.Controls.Add(this.dataGridViewProfesori);
            this.Controls.Add(this.dataGridViewFacultate);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewFacultate)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewProfesori)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private DataGridView dataGridViewFacultate;
        private DataGridView dataGridViewProfesori;
        private TextBox textBoxNume;
        private TextBox textBoxPrenume;
        private TextBox textBoxTitulatura;
        private Label label1;
        private Label label2;
        private Label label3;
        private Button buttonAdd;
        private Button buttonUpdate;
        private Button buttonDelete;
        private Label label4;
        private Label label5;
        private TextBox textBoxGen;
        private DateTimePicker dateTimePicker;
    }
}