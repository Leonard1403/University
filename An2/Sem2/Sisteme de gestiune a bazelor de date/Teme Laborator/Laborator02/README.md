A simple .NET application that uses WinForms to manage orders placed by customers.
The database connection is configured in App.config, while the tables, the number of columns, and their names are set in appSettings.

When the form loads, data from both tables is loaded into a DataSet, the relationship between the tables is created, and a DataGridView is linked via a BindingSource. Additionally, controls are generated dynamically for each column in the child table (TextBox or DateTimePicker).

CRUD operations include:

Deleting a record for a client
Updating a record for a client
Adding a record for a client

After each operation, the data is reloaded into the DataSet.