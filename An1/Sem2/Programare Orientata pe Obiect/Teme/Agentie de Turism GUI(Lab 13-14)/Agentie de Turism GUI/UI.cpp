#pragma once
#include "UI.h"
#include <iostream>
using namespace std;

void ConsoleUI::printMenu() {
	cout << "Comenzi disponibile:" << endl;
	cout << "1.Adaugare turism\n2.Stergere\n3.Modificare" << endl;
	cout << "4.Cautare oferta" << endl;
	cout << "5.Filtrare oferta(destinatie,pret)" << endl;
	cout << "6.Sortare turism dupa:denumire,destinatie,tip si pret" << endl;
	cout << "7.Adauga oferta in wishlist" << endl;
	cout << "8.Adauga oferta random in wishlist" << endl;
	cout << "9.Goleste toate ofertele din wishlist" << endl;
	cout << "10.Export. Salveaza lista de elemente in fisier" << endl;
	
	cout << "11.Reface ultima operatie" << endl;
	
	cout << "12.Afiseaza toate ofertele din wishlist" << endl;
	cout << "13.Afisare tuturor ofertelor" << endl;
	
	cout << "14.Exit" << endl;
}

void ConsoleUI::uiAdd() {
	string denumire;
	string destinatie;
	string tip;
	int pret;
	cout << "Denumire: ";
	getline(cin >> ws, denumire);
	cout << "Destinatie: ";
	getline(cin >> ws, destinatie);
	cout << "Tip: ";
	getline(cin >> ws, tip);
	cout << "Pret: ";
	cin >> pret;
	try {
		srv.addTurism(denumire, destinatie, tip, pret);
	}
	catch (RepoException& re) {
		cout << re.getErrorMessage();
	}
	catch (ValidationException& ve) {
		cout << "Oferta de turism nu este valida!" << endl;
		cout << ve.getErrorMessages();
	}
}

void ConsoleUI::uiSort() {
	cout << "Criteriul de sortare pe care doriti sa-l aplicati:(denumire destinatie tip+pret)>";
	string criteriu;
	cin >> criteriu;
	if (criteriu == "denumire") {
		printAllTurism(srv.sortByDenumire());
	}
	if (criteriu == "destinatie") {
		printAllTurism(srv.sortByDestinatie());
	}
	if (criteriu == "tip+pret") {
		printAllTurism(srv.sortByTipAndPret());
	}
}

void ConsoleUI::uiFilter() {
	cout << "Criterile de filtrare sunt destinatie si pret: ";
	string criteriu;
	cin >> criteriu;
	if (criteriu == "destinatie") {
		cout << "Destinatia pe care o cautati: ";
		string destinatie;
		cin >> destinatie;
		printAllTurism(srv.filtrareDestinatie(destinatie));
	}
	if (criteriu == "pret") {
		cout << "Oferta turistica cu pretul pe care doriti sa o cautati: ";
		int pret;
		cin >> pret;
		printAllTurism(srv.filtrarePret(pret));
	}
}

void ConsoleUI::printAllTurism(const vector<Turism>& allTurism) {
	if (allTurism.size() == 0) {
		cout << "Nu exista oferte\n";
	}
	else {
		for (const auto& turism : allTurism) {
			cout << "Denumire: " << turism.getDenumire() << "| Destinatie: " << turism.getDestinatie() << "| Tip: " << turism.getTip() << "| Pret: " << turism.getPret() << endl;
		}
	}
}

void ConsoleUI::ui_undo() {
	try {
		srv.undo();
		cout << "Undo realizat cu succes" << endl;
	}
	catch (std::exception()) {
		cout << "Nu se mai poate face undo!" << endl;
	}
}

void ConsoleUI::ui_adauga_wishlist() {
	string denumire;
	cout << "Introduceti denumirea: ";
	getline(cin >> ws, denumire);
	try {
		this->srv.storeWishlist(denumire);
		cout << "Oferta a fost adaugata in wishlist" << endl;
	}
	catch (RepoException& re) {
		cout << re.getErrorMessage();
	}
	catch (std::exception()) {
		cout << "Oferta se afla deja in wishlist!" << endl;
	}
}

void ConsoleUI::ui_adauga_random() {
	string n;
	int nr;
	cout << "Introduceti nr de oferte de adaugat";
	getline(cin >> ws, n);
	try {
		nr = stoi(n);
		this->srv.storeRandom(nr);
		cout << "Ofertele au fost adaugate cu succes in wishlist!" << endl;
	}
	catch (RepoException& re) {
		cout << re.getErrorMessage();
	}
}

void ConsoleUI::print_wishlist() {
	printAllTurism(srv.getAllWishlist());
}

void ConsoleUI::ui_goleste_wishlist() {
	this->srv.golesteWishlist();
	cout << "Wishlistul a fost golit!" << endl;
}

void ConsoleUI::ui_export() {
	cout << "Introduceti numele fisierului:";
	string fileName;
	cin >> fileName;
	try {
		srv.saveWishlistToFile(fileName);
		cout << "Oferta a fost adaugata in fisier" << endl;
	}
	catch (RepoException&) {
		cout << "Fisierul nu se poate deschide" << endl;
	}
}

void ConsoleUI::addDefaultTurism() {
	srv.addTurism("La prapastia din vale", "Floresti", "munte", 200);
	srv.addTurism("La Veriku", "Cluj-Napoca", "atelier auto", 500);
	srv.addTurism("Belvedere", "Cluj-Napoca", "hotel", 500);
	srv.addTurism("Gradina botanica", "Cluj-Napoca", "munte", 9800);
}

void ConsoleUI::uiStergere() {
	string tip, denumire, destinatie;
	//int pret;
	cout << "Stergere oferte turistice pentru denumire, destinatie si tip dat\n";
	cout << "denumire: ";
	getline(cin >> ws, denumire);
	cout << "destinatie: ";
	getline(cin >> ws, destinatie);
	cout << "tip: ";
	getline(cin >> ws, tip);
	try {
		Turism oferta = srv.search(denumire);
		srv.stergereTurism(denumire);
		cout << "Denumire: " << oferta.getDenumire() << "| Destinatie: " << oferta.getDestinatie() << "| Tip: " << oferta.getTip() << "| Pret: " << oferta.getPret() << endl;
	}
	catch (RepoException& re) {
		cout << "Oferta nu este valabila sau nu exista\n";
		cout << re.getErrorMessage();
	}
}

void ConsoleUI::uiModificare() {
	string tip, denumire, destinatie;
	int pret;
	cout << "Modificarea acesteia: ";
	cout << "denumire: ";
	getline(cin >> ws, denumire);
	cout << "destinatie: ";
	getline(cin >> ws, destinatie);
	cout << "tip: ";
	getline(cin >> ws, tip);
	cout << "pret: ";
	cin >> pret;
	try {
		Turism oferta = srv.search(denumire);
		cout << "Denumire: " << oferta.getDenumire() << "| Destinatie: " << oferta.getDestinatie() << "| Tip: " << oferta.getTip() << "| Pret: " << oferta.getPret() << endl;
		srv.modifyTurism(denumire, destinatie, tip, pret);
	}
	catch (RepoException) {
		cout << "Oferta nu este disponibila sau nu exista\n";
	}
}

void ConsoleUI::uiSearch() {
	string tip , denumire, destinatie;
	/*
	* string denumire;
	* string destinatie;
	* string tip;
	* int pret;
	*/
	cout << "Cautare oferte turistice pentru denumire, destinatie si tip dat\n";
	cout << "denumire: ";
	getline(cin >> ws, denumire);
	try {
		Turism oferta = srv.search(denumire);
		cout << "Denumire: " << oferta.getDenumire() << "| Destinatie: " << oferta.getDestinatie() << "| Tip: " << oferta.getTip() << "| Pret: " << oferta.getPret() << endl;
	}
	catch(RepoException) {
		cout << "Oferta nu este disponibila sau nu exista\n";
	}
}

void ConsoleUI::run() {
	int runing = 1;
	int cmd;
	addDefaultTurism();
	while (runing) {
		printMenu();
		cout << "Comanda este: ";
		cin >> cmd;
		//cout << cmd << '\n';
		switch (cmd) {
		case 1:
			uiAdd();
			break;
		case 2:
			uiStergere();
			break;
		case 3:
			uiModificare();
			break;
		case 4:
			uiSearch();
			break;
		case 5:
			uiFilter();
			break;
		case 6:
			uiSort();
			break;
		case 7:
			ui_adauga_wishlist();
			break;
		case 8:
			ui_adauga_random();
			break;
		case 9:
			ui_goleste_wishlist();
			break;
		case 10:
			ui_export();
			break;
		case 11:
			ui_undo();
			break;
		case 12:
			print_wishlist();
			break;
		case 13:
			printAllTurism(srv.getAllTurism());
			break;
		case 14:
			runing = 0;
			break;
		default:
			cout << "Comanda indisponibila" << endl;
		}
		cout << "Oferte: " << srv.getSizeOfTurism() << endl;
		cout << "Wishlist: " << srv.getSizeOfWishlist() << endl;
	}
}