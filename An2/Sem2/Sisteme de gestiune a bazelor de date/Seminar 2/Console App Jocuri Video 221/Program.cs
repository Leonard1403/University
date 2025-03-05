using Microsoft.Data.SqlClient;
namespace Console_App_Jocuri_Video_221
{
    internal class Program
    {
        static void Main(string[] args)
        {
            
            try
            {
                Console.BackgroundColor = ConsoleColor.DarkBlue;
                Console.Clear();
                Console.WriteLine("Hello Console App C#!");
                string connectionString = @"Server=DESKTOP-01E0F0G\SQLEXPRESS;Database=Seminar1SGBD2212023;
                Integrated Security=true;TrustServerCertificate=true;";
                using(SqlConnection connection = new SqlConnection(connectionString))
                {
                    Console.WriteLine("Starea conexiunii: {0}", connection.State);
                    connection.Open();
                    Console.WriteLine("Starea conexiunii: {0}", connection.State);
                    SqlCommand insertCommand = new SqlCommand("INSERT INTO JocuriVideo (nume, pret, producator) VALUES " +
                        "(@nume1,@pret1,@producator1),(@nume2,@pret2,@producator2);", connection);
                    insertCommand.Parameters.AddWithValue("@nume1", "Hearthstone");
                    insertCommand.Parameters.AddWithValue("@pret1", 0.0F);
                    insertCommand.Parameters.AddWithValue("@producator1", "Blizzard");
                    insertCommand.Parameters.AddWithValue("@nume2", "Starcraft");
                    insertCommand.Parameters.AddWithValue("@pret2", 0.0F);
                    insertCommand.Parameters.AddWithValue("@producator2", "Blizzard");
                    int insertRowCount = insertCommand.ExecuteNonQuery();
                    Console.WriteLine("Insert Row Count: {0}",insertRowCount);
                    SqlCommand selectCommand = new SqlCommand("SELECT nume, pret, producator FROM JocuriVideo;",connection);    
                    SqlDataReader reader = selectCommand.ExecuteReader();
                    if (reader.HasRows)
                    {
                        Console.WriteLine("Citirea si afisarea datelor din tabelul JocuriVideo");
                        while (reader.Read())
                        {
                            Console.WriteLine("{0}\t{1}\t{2}", reader.GetString(0), reader.GetFloat(1),
                                reader.GetString(2));
                        }
                    }
                    reader.Close();
                    SqlCommand updateCommand = new SqlCommand("UPDATE JocuriVideo SET pret=@pret WHERE " +
                        "nume=@nume;",connection);
                    updateCommand.Parameters.AddWithValue("pret", 10.0F);
                    updateCommand.Parameters.AddWithValue("nume", "Hearthstone");
                    int updateRowCount = updateCommand.ExecuteNonQuery();
                    Console.WriteLine("Update Row Count: {0}", updateRowCount);
                    SqlCommand deleteCommand = new SqlCommand("DELETE FROM JocuriVideo WHERE nume=@nume;", connection);
                    deleteCommand.Parameters.AddWithValue("@nume", "Starcraft");
                    int deleteRowCount = deleteCommand.ExecuteNonQuery();
                    Console.WriteLine("Delete Row Count: {0}", deleteRowCount);
                    reader = selectCommand.ExecuteReader();
                    if(reader.HasRows)
                    {
                        Console.WriteLine("Dupa actualizare si stergere, citim si afisam datele din tabelul " +
                            "JocuriVideo");
                        while(reader.Read())
                        {
                            Console.WriteLine("{0}\t{1}\t{2}", reader.GetString(0), reader.GetFloat(1),
                                reader.GetString(2));
                        }
                    }
                    reader.Close();
                }
            }
            catch(Exception ex)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine(ex.Message);
            }
        }
    }
}