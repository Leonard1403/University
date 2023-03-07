using Laborator8.domain;
using Laborator8.domain.validator;
using Laborator8.repository;
using Laborator8.service;
using Laborator8.validator;

using System;
using System.Linq;
using System.Collections.Generic;

namespace Laborator8
{
    class Program
    {
        static void Main(string[] args)
        {
//create repository for teams
            var echipaRepo =
                new EchipaFileRepository(new EchipaValidator(), "..\\..\\..\\data\\echipe.txt", EntityToFileMapping.CreateEchipa);
            //create repository for elevi
            var elevRepo = new EleviFileRepository(new ElevValidator(), "..\\..\\..\\data\\elevi.txt");

            //create repository for jucatori
            var jucatorRepo = new JucatorFileRepository(new JucatorValidator(), "..\\..\\..\\data\\jucator.txt", EntityToFileMapping.CreateJucator);

            //create services
            var echipaService = new EchipaService(echipaRepo);
            var elevService = new ElevService(elevRepo);
            var jucatorService = new JucatorService(jucatorRepo);

            //populate teams
            Echipa e1 = new Echipa(1, "Echipa1");
            echipaService.AddEchipa(e1);
            Echipa e2 = new Echipa(2, "Echipa2");
            echipaService.AddEchipa(e2);
            //echipaRepo.Save(e1);
            //echipaRepo.Save(e2);
            
            //populate elevi
            elevService.AddElev(9, "Elev 9", "Scoala 9");
            elevService.AddElev(2, "Elev 2", "Scoala 2");
            elevService.AddElev(3, "Elev 3", "Scoala 3");
            
            //populate echipa
            Jucator j1 = new Jucator(1,elevService.GetElev(9), e1);
            Jucator j2 = new Jucator(2, elevService.GetElev(2), e1);
            Jucator j3 = new Jucator(3, elevService.GetElev(3), e2);
            jucatorService.AddJucator(j1);
            jucatorService.AddJucator(j2);
            jucatorService.AddJucator(j3);
            jucatorRepo.Save(j1);

            Console.WriteLine("Elevii sunt: ");
            foreach(Elev elev in elevService.GetAllElevi())
            {
                Console.WriteLine(elev);
            }
            
            Console.WriteLine("Echipele sunt: ");
            foreach (Echipa echipa in echipaService.FindAll())
            {
                Console.WriteLine(echipa);
            }

            Console.WriteLine("Jucatorii sunt: ");
            foreach (Jucator jucator in jucatorService.FindAll())
            {
                Console.WriteLine(jucator);
            }

            //--------Sa se afiseze toti jucatorii unei echipe dată-------------------------------

            Console.WriteLine("--------Sa se afiseze toti jucatorii unei echipe dată----------");
            
            Console.Write("Id = ");
            int id1 = Convert.ToInt32(Console.ReadLine());
            
            foreach (Jucator jucator in jucatorService.FindAll())
            {
                if(jucator.Echipa.ID == id1)
                    Console.WriteLine(jucator);
            }
            
            //--------Sa se afiseze toti jucatorii activi ai unei echipe de la un anumit meci-----
            
            var meciRepo = new MeciFileRepository("..\\..\\..\\data\\meci.txt");
            var meciList = meciRepo.GetAll();
            
            meciList.Add(new Meci(1, 2, new DateTime(2022, 12, 24))); 
            meciList.Add(new Meci(10, 11, new DateTime(2022, 12, 25)));
            meciRepo.SaveAll(meciList);

            //Afisare meciuri
            Console.WriteLine("Meciurile sunt:");
            foreach (var meci in meciList)
            {
                Console.WriteLine(meci);
            }
            
            //Afisare jucatori
            var repo = new JucatorActiveFileRepository("..\\..\\..\\data\\jucatorActiv.txt");

            // Populare date
            repo.Add(new JucatorActiv(1, 1, 12, JucatorActiv.TipJucator.Participat));
            repo.Add(new JucatorActiv(2, 1, 8, JucatorActiv.TipJucator.Rezerva));
            repo.Add(new JucatorActiv(3, 2, 14, JucatorActiv.TipJucator.Participat));
            repo.Add(new JucatorActiv(3, 3, 14, JucatorActiv.TipJucator.Participat));
            repo.Add(new JucatorActiv(4, 2, 5, JucatorActiv.TipJucator.Rezerva));
            
            // Afisare date
            var jucatori = repo.GetAll();
            
            Console.Write("idMeci = ");
            id1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Jucatorii Activi sunt: ");
            foreach (var j in repo.GetAll())
            {
                if(j.IdMeci == id1)
                    Console.WriteLine(j);
            }
            
            
            Console.WriteLine("--------Sa se afiseze toti jucatorii activi ai unei echipe de la un anumit meci-----");
            int idMeci = 2;
            
            Console.Write("idMeci = ");
            id1 = Convert.ToInt32(Console.ReadLine());
            Console.Write("idEchipa = ");
            int id2 = Convert.ToInt32(Console.ReadLine());
            foreach (var j in jucatori)
            {
                if (j.IdMeci == id1 && j.Tip == JucatorActiv.TipJucator.Participat)
                {
                    foreach(var i in jucatorService.FindAll()){
                        if(i.ID == j.IdJucator && i.Echipa.ID == id2)
                            Console.WriteLine(i);
                    }
                    //Console.WriteLine(jucatorService.FindOne(j.IdJucator));
                }
            }
            Console.WriteLine("//--------Sa se afiseze toate meciurile dintr-o anumita perioada calendaristica-------");
            
            //DateTime timp = new DateTime(2022, 12, 24);
            DateTime myDate;
            Console.WriteLine("Introduceti o data (mm/dd/yyyy): ");
            myDate = DateTime.Parse(Console.ReadLine());
            Console.WriteLine("Data introdusa este: " + myDate);
            
            List<Meci> allMeci = new List<Meci>();
            allMeci = meciRepo.GetAll();
            var eveniment = from eveniment_Select in allMeci
                            where eveniment_Select.Data == myDate
                            select eveniment_Select;
            foreach (var j in eveniment)
            {
                if (j.Data == myDate)
                {
                    Console.WriteLine(j);
                }
            }
            
            Console.WriteLine("----------Sa se determine si sa se afiseze scorul de la un anumit meci----------------");
            id1 = Convert.ToInt32(Console.ReadLine());
            id2 = Convert.ToInt32(Console.ReadLine());
            int scor1 = 0, scor2 = 0;
            foreach (var j in meciRepo.GetAll())
            {
                
                if (j.Data == myDate && j.Echipa1 == id1 && j.Echipa2 == id2)
                {
                    foreach (Jucator jucator in jucatorService.FindAll())
                    {
                        if (jucator.Echipa.ID == j.Echipa1)
                        {
                            foreach (var al in repo.GetAll())
                            {
                                if (al.IdJucator == jucator.ID)
                                {
                                    scor1 = scor1 + al.NrPuncteInscrise;
                                    break;
                                }
                            }
                        }
                        else if (jucator.Echipa.ID == j.Echipa2)
                        {
                            foreach (var al in repo.GetAll())
                            {
                                if (al.IdJucator == jucator.ID)
                                {
                                    scor2 = scor2 + al.NrPuncteInscrise;
                                    break;
                                }
                            }
                        }
                    }
                }
            }
            Console.WriteLine("Scorul final este: " + scor1 + " " + scor2);

            //repo.DeleteAll();
            //jucatorService.DeleteJucator(j1.ID);
            //jucatorService.DeleteJucator(j2.ID);
            //jucatorService.DeleteJucator(j3.ID);
        }
    }
}
            