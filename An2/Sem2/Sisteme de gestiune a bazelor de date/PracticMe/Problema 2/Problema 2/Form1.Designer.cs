namespace Problema_2
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
            this.listBoxArtisti = new System.Windows.Forms.ListBox();
            this.dataGridMelodii = new System.Windows.Forms.DataGridView();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.textBoxTitlu = new System.Windows.Forms.TextBox();
            this.textBoxAn = new System.Windows.Forms.TextBox();
            this.textBoxDurata = new System.Windows.Forms.TextBox();
            this.buttonAdd = new System.Windows.Forms.Button();
            this.buttonUpdate = new System.Windows.Forms.Button();
            this.buttonDelete = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridMelodii)).BeginInit();
            this.SuspendLayout();
            // 
            // listBoxArtisti
            // 
            this.listBoxArtisti.FormattingEnabled = true;
            this.listBoxArtisti.ItemHeight = 20;
            this.listBoxArtisti.Location = new System.Drawing.Point(12, 25);
            this.listBoxArtisti.Name = "listBoxArtisti";
            this.listBoxArtisti.Size = new System.Drawing.Size(317, 104);
            this.listBoxArtisti.TabIndex = 0;
            this.listBoxArtisti.SelectedIndexChanged += new System.EventHandler(this.listBoxArtisti_SelectedIndexChanged);
            // 
            // dataGridMelodii
            // 
            this.dataGridMelodii.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridMelodii.Location = new System.Drawing.Point(351, 25);
            this.dataGridMelodii.Name = "dataGridMelodii";
            this.dataGridMelodii.RowHeadersWidth = 51;
            this.dataGridMelodii.RowTemplate.Height = 29;
            this.dataGridMelodii.Size = new System.Drawing.Size(437, 237);
            this.dataGridMelodii.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 141);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(38, 20);
            this.label1.TabIndex = 2;
            this.label1.Text = "Titlu";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 175);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(78, 20);
            this.label2.TabIndex = 3;
            this.label2.Text = "An lansare";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 206);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(54, 20);
            this.label3.TabIndex = 4;
            this.label3.Text = "Durata";
            // 
            // textBoxTitlu
            // 
            this.textBoxTitlu.Location = new System.Drawing.Point(130, 141);
            this.textBoxTitlu.Name = "textBoxTitlu";
            this.textBoxTitlu.Size = new System.Drawing.Size(125, 27);
            this.textBoxTitlu.TabIndex = 5;
            // 
            // textBoxAn
            // 
            this.textBoxAn.Location = new System.Drawing.Point(130, 175);
            this.textBoxAn.Name = "textBoxAn";
            this.textBoxAn.Size = new System.Drawing.Size(125, 27);
            this.textBoxAn.TabIndex = 6;
            // 
            // textBoxDurata
            // 
            this.textBoxDurata.Location = new System.Drawing.Point(130, 206);
            this.textBoxDurata.Name = "textBoxDurata";
            this.textBoxDurata.Size = new System.Drawing.Size(125, 27);
            this.textBoxDurata.TabIndex = 7;
            // 
            // buttonAdd
            // 
            this.buttonAdd.Location = new System.Drawing.Point(12, 253);
            this.buttonAdd.Name = "buttonAdd";
            this.buttonAdd.Size = new System.Drawing.Size(94, 29);
            this.buttonAdd.TabIndex = 8;
            this.buttonAdd.Text = "Add";
            this.buttonAdd.UseVisualStyleBackColor = true;
            this.buttonAdd.Click += new System.EventHandler(this.buttonAdd_Click);
            // 
            // buttonUpdate
            // 
            this.buttonUpdate.Location = new System.Drawing.Point(112, 253);
            this.buttonUpdate.Name = "buttonUpdate";
            this.buttonUpdate.Size = new System.Drawing.Size(94, 29);
            this.buttonUpdate.TabIndex = 9;
            this.buttonUpdate.Text = "Update";
            this.buttonUpdate.UseVisualStyleBackColor = true;
            this.buttonUpdate.Click += new System.EventHandler(this.buttonUpdate_Click);
            // 
            // buttonDelete
            // 
            this.buttonDelete.Location = new System.Drawing.Point(212, 253);
            this.buttonDelete.Name = "buttonDelete";
            this.buttonDelete.Size = new System.Drawing.Size(94, 29);
            this.buttonDelete.TabIndex = 10;
            this.buttonDelete.Text = "Delete";
            this.buttonDelete.UseVisualStyleBackColor = true;
            this.buttonDelete.Click += new System.EventHandler(this.buttonDelete_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.buttonDelete);
            this.Controls.Add(this.buttonUpdate);
            this.Controls.Add(this.buttonAdd);
            this.Controls.Add(this.textBoxDurata);
            this.Controls.Add(this.textBoxAn);
            this.Controls.Add(this.textBoxTitlu);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.dataGridMelodii);
            this.Controls.Add(this.listBoxArtisti);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridMelodii)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private ListBox listBoxArtisti;
        private DataGridView dataGridMelodii;
        private Label label1;
        private Label label2;
        private Label label3;
        private TextBox textBoxTitlu;
        private TextBox textBoxAn;
        private TextBox textBoxDurata;
        private Button buttonAdd;
        private Button buttonUpdate;
        private Button buttonDelete;
    }
}