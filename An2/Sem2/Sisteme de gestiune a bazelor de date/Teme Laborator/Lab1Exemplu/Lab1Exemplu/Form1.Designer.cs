﻿namespace Lab1Exemplu
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
            this.GridArtist = new System.Windows.Forms.DataGridView();
            this.GridCasaDiscuri = new System.Windows.Forms.DataGridView();
            this.button2 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.GridArtist)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.GridCasaDiscuri)).BeginInit();
            this.SuspendLayout();
            // 
            // GridArtist
            // 
            this.GridArtist.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.GridArtist.Location = new System.Drawing.Point(46, 42);
            this.GridArtist.Name = "GridArtist";
            this.GridArtist.RowHeadersWidth = 51;
            this.GridArtist.RowTemplate.Height = 29;
            this.GridArtist.Size = new System.Drawing.Size(300, 188);
            this.GridArtist.TabIndex = 0;
            this.GridArtist.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.GridArtist_CellContentClick);
            // 
            // GridCasaDiscuri
            // 
            this.GridCasaDiscuri.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.GridCasaDiscuri.Location = new System.Drawing.Point(46, 250);
            this.GridCasaDiscuri.Name = "GridCasaDiscuri";
            this.GridCasaDiscuri.RowHeadersWidth = 51;
            this.GridCasaDiscuri.RowTemplate.Height = 29;
            this.GridCasaDiscuri.Size = new System.Drawing.Size(300, 188);
            this.GridCasaDiscuri.TabIndex = 1;
            this.GridCasaDiscuri.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.GridCasaDiscuri_CellContentClick);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(555, 339);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(94, 29);
            this.button2.TabIndex = 2;
            this.button2.Text = "Update DB";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(555, 91);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(94, 29);
            this.button1.TabIndex = 3;
            this.button1.Text = "Connect";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.GridCasaDiscuri);
            this.Controls.Add(this.GridArtist);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.GridArtist)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.GridCasaDiscuri)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private DataGridView GridArtist;
        private DataGridView GridCasaDiscuri;
        private Button button2;
        private Button button1;
    }
}