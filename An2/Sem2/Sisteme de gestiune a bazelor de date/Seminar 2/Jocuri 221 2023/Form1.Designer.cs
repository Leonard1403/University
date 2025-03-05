namespace Jocuri_221_2023
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
            this.dataGridViewParent = new System.Windows.Forms.DataGridView();
            this.dataGridViewChild = new System.Windows.Forms.DataGridView();
            this.labelParent = new System.Windows.Forms.Label();
            this.labelChild = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.labelNume = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridViewParent
            // 
            this.dataGridViewParent.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewParent.Location = new System.Drawing.Point(39, 65);
            this.dataGridViewParent.Name = "dataGridViewParent";
            this.dataGridViewParent.RowHeadersWidth = 51;
            this.dataGridViewParent.RowTemplate.Height = 29;
            this.dataGridViewParent.Size = new System.Drawing.Size(551, 268);
            this.dataGridViewParent.TabIndex = 0;
            this.dataGridViewParent.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridViewParent_CellContentClick);
            // 
            // dataGridViewChild
            // 
            this.dataGridViewChild.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewChild.Location = new System.Drawing.Point(608, 65);
            this.dataGridViewChild.Name = "dataGridViewChild";
            this.dataGridViewChild.RowHeadersWidth = 51;
            this.dataGridViewChild.RowTemplate.Height = 29;
            this.dataGridViewChild.Size = new System.Drawing.Size(806, 268);
            this.dataGridViewChild.TabIndex = 1;
            this.dataGridViewChild.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridViewChild_CellContentClick);
            // 
            // labelParent
            // 
            this.labelParent.AutoSize = true;
            this.labelParent.Font = new System.Drawing.Font("Segoe UI", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.labelParent.ForeColor = System.Drawing.Color.Blue;
            this.labelParent.Location = new System.Drawing.Point(39, 25);
            this.labelParent.Name = "labelParent";
            this.labelParent.Size = new System.Drawing.Size(201, 31);
            this.labelParent.TabIndex = 2;
            this.labelParent.Text = "Tabelul Magazine";
            // 
            // labelChild
            // 
            this.labelChild.AutoSize = true;
            this.labelChild.Font = new System.Drawing.Font("Segoe UI", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.labelChild.ForeColor = System.Drawing.Color.MediumBlue;
            this.labelChild.Location = new System.Drawing.Point(608, 25);
            this.labelChild.Name = "labelChild";
            this.labelChild.Size = new System.Drawing.Size(162, 31);
            this.labelChild.TabIndex = 3;
            this.labelChild.Text = "Tabelul Jocuri";
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(39, 396);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(325, 27);
            this.textBox1.TabIndex = 4;
            this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // labelNume
            // 
            this.labelNume.AutoSize = true;
            this.labelNume.Font = new System.Drawing.Font("Segoe UI", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.labelNume.ForeColor = System.Drawing.Color.Indigo;
            this.labelNume.Location = new System.Drawing.Point(39, 362);
            this.labelNume.Name = "labelNume";
            this.labelNume.Size = new System.Drawing.Size(325, 31);
            this.labelNume.TabIndex = 5;
            this.labelNume.Text = "Numele magazinului selectat";
            this.labelNume.Click += new System.EventHandler(this.labelNume_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Plum;
            this.ClientSize = new System.Drawing.Size(1426, 482);
            this.Controls.Add(this.labelNume);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.labelChild);
            this.Controls.Add(this.labelParent);
            this.Controls.Add(this.dataGridViewChild);
            this.Controls.Add(this.dataGridViewParent);
            this.Name = "Form1";
            this.Text = "Jocuri 221";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private DataGridView dataGridViewParent;
        private DataGridView dataGridViewChild;
        private Label labelParent;
        private Label labelChild;
        private TextBox textBox1;
        private Label labelNume;
    }
}