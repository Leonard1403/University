﻿using System;
using System.Configuration;
using System.Data.SqlClient;
using System.Threading;

namespace Lab4
{
    class Program
    {
        static string connectionString = ConfigurationManager.ConnectionStrings["connection"].ConnectionString;
        static int noRetries = 2;

        static void Main(string[] args)
        {
            Thread t1 = new Thread(new ThreadStart(Transaction1));
            Thread t2 = new Thread(new ThreadStart(Transaction2));

            t1.Start();
            t2.Start();
            t1.Join();
            t2.Join();

            Console.WriteLine("Press ENTER to quit...");
            Console.ReadKey();
        }

        static void Transaction1()
        {
            int noTries = 0;
            while (!Transaction1_Run())
            {
                noTries++;
                if (noTries >= noRetries)
                    break;
            }
            if (noTries == noRetries)
                Console.WriteLine("Deadlock_T1_C# aborted.");
        }

        static void Transaction2()
        {
            int noTries = 0;
            while (!Transaction2_Run())
            {
                noTries++;
                if (noTries >= noRetries)
                    break;
            }
            if (noTries == noRetries)
                Console.WriteLine("Deadlock_T2_C# aborted.");
        }

        static bool Transaction1_Run()
        {
            bool success = false;

            Console.WriteLine("Deadlock_T1_C# started...");

            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                SqlCommand command = connection.CreateCommand();
                try
                {
                    connection.Open();
                    command.Connection = connection;
                    command.CommandText = "EXECUTE Deadlock_T1_C#";
                    command.ExecuteNonQuery();
                    success = true;
                    Console.WriteLine("Deadlock_T1_C# complete!");
                }

                catch (SqlException ex)
                {
                    if (ex.Number == 1205)
                    {
                        Console.WriteLine("Deadlock_T1_C#: Commit exception type: {0}", ex.GetType());
                        Console.WriteLine("Message: {0}", ex.Message);
                    }

                }
                return success;
            }
        }

        static bool Transaction2_Run()
        {
            bool success = false;

            Console.WriteLine("Deadlock_T2_C# started...");

            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                SqlCommand command = connection.CreateCommand();
                try
                {
                    connection.Open();
                    command.Connection = connection;
                    command.CommandText = "EXECUTE Deadlock_T2_C#";
                    command.ExecuteNonQuery();
                    success = true;
                    Console.WriteLine("Deadlock_T2_C# complete!");
                }

                catch (SqlException ex)
                {
                    if (ex.Number == 1205)
                    {
                        Console.WriteLine("Deadlock_T2_C#: Commit exception type: {0}", ex.GetType());
                        Console.WriteLine("Message: {0}", ex.Message);
                    }

                }
                return success;
            }
        }
    }
}
