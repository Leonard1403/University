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
            this.dataGridViewProducatori = new System.Windows.Forms.DataGridView();
            this.dataGridViewBiscuiti = new System.Windows.Forms.DataGridView();
            this.textBoxNume = new System.Windows.Forms.TextBox();
            this.textBoxCalorii = new System.Windows.Forms.TextBox();
            this.textBoxPret = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.buttonAdd = new System.Windows.Forms.Button();
            this.buttonUpdate = new System.Windows.Forms.Button();
            this.buttonDelete = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewProducatori)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewBiscuiti)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridViewProducatori
            // 
            this.dataGridViewProducatori.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewProducatori.Location = new System.Drawing.Point(12, 12);
            this.dataGridViewProducatori.Name = "dataGridViewProducatori";
            this.dataGridViewProducatori.RowHeadersWidth = 51;
            this.dataGridViewProducatori.RowTemplate.Height = 29;
            this.dataGridViewProducatori.Size = new System.Drawing.Size(360, 252);
            this.dataGridViewProducatori.TabIndex = 0;
            this.dataGridViewProducatori.SelectionChanged += new System.EventHandler(this.dataGridViewProducatori_SelectionChanged);
            // 
            // dataGridViewBiscuiti
            // 
            this.dataGridViewBiscuiti.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewBiscuiti.Location = new System.Drawing.Point(412, 12);
            this.dataGridViewBiscuiti.Name = "dataGridViewBiscuiti";
            this.dataGridViewBiscuiti.RowHeadersWidth = 51;
            this.dataGridViewBiscuiti.RowTemplate.Height = 29;
            this.dataGridViewBiscuiti.Size = new System.Drawing.Size(376, 252);
            this.dataGridViewBiscuiti.TabIndex = 1;
            this.dataGridViewBiscuiti.SelectionChanged += new System.EventHandler(this.dataGridViewBiscuiti_SelectionChanged);
            // 
            // textBoxNume
            // 
            this.textBoxNume.Location = new System.Drawing.Point(247, 285);
            this.textBoxNume.Name = "textBoxNume";
            this.textBoxNume.Size = new System.Drawing.Size(125, 27);
            this.textBoxNume.TabIndex = 2;
            // 
            // textBoxCalorii
            // 
            this.textBoxCalorii.Location = new System.Drawing.Point(247, 318);
            this.textBoxCalorii.Name = "textBoxCalorii";
            this.textBoxCalorii.Size = new System.Drawing.Size(125, 27);
            this.textBoxCalorii.TabIndex = 3;
            // 
            // textBoxPret
            // 
            this.textBoxPret.Location = new System.Drawing.Point(247, 351);
            this.textBoxPret.Name = "textBoxPret";
            this.textBoxPret.Size = new System.Drawing.Size(125, 27);
            this.textBoxPret.TabIndex = 4;
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
            this.label2.Size = new System.Drawing.Size(101, 20);
            this.label2.TabIndex = 6;
            this.label2.Text = "Numar Calorii";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(140, 351);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(35, 20);
            this.label3.TabIndex = 7;
            this.label3.Text = "Pret";
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
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.buttonDelete);
            this.Controls.Add(this.buttonUpdate);
            this.Controls.Add(this.buttonAdd);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textBoxPret);
            this.Controls.Add(this.textBoxCalorii);
            this.Controls.Add(this.textBoxNume);
            this.Controls.Add(this.dataGridViewBiscuiti);
            this.Controls.Add(this.dataGridViewProducatori);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewProducatori)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewBiscuiti)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private DataGridView dataGridViewProducatori;
        private DataGridView dataGridViewBiscuiti;
        private TextBox textBoxNume;
        private TextBox textBoxCalorii;
        private TextBox textBoxPret;
        private Label label1;
        private Label label2;
        private Label label3;
        private Button buttonAdd;
        private Button buttonUpdate;
        private Button buttonDelete;
    }
}