#include "GUI.h"

void ConsoleGUI::initializeGUIComponents() {
	QHBoxLayout* lyMain = new QHBoxLayout;
	this->setLayout(lyMain);

	//COMPONENTA LEFT
	QWidget* leftleft = new QWidget;
	QVBoxLayout* lyLeftleft = new QVBoxLayout;
	leftleft->setLayout(lyLeftleft);

	//adaugare
	QWidget* formleft = new QWidget;
	QFormLayout* lyFormleft = new QFormLayout;
	formleft->setLayout(lyFormleft);
	this->editDenumireW = new QLineEdit;

	lyFormleft->addRow(lblDenumireW, editDenumireW);
	btnAddWishlist = new QPushButton("Adauga oferta in wishlist");
	lyFormleft->addWidget(btnAddWishlist);

	lyLeftleft->addWidget(formleft);

	//adaugare random
	QWidget* formAddR = new QWidget;
	QFormLayout* lyFormAddR = new QFormLayout;
	formAddR->setLayout(lyFormAddR);
	this->editNr = new QLineEdit;

	lyFormAddR->addRow(lblNr, editNr);
	btnAddRandom = new QPushButton("Adauga oferta random in wishlist");
	lyFormAddR->addWidget(btnAddRandom);

	lyLeftleft->addWidget(formAddR);

	//export
	QWidget* formEx = new QWidget;
	QFormLayout* lyFormEx = new QFormLayout;
	formEx->setLayout(lyFormEx);
	this->editFile = new QLineEdit;

	lyFormEx->addRow(lblFile, editFile);
	btnExport = new QPushButton("Export");
	lyFormEx->addWidget(btnExport);

	lyLeftleft->addWidget(formEx);

	//goleste program
	btnGoleste = new QPushButton("Goleste lista oferte!");
	lyLeftleft->addWidget(btnGoleste);

	//CRUD
	btnCRUD = new QPushButton("ARATA CRUD");
	lyLeftleft->addWidget(btnCRUD);

	//DRAW
	btnDRAW = new QPushButton("ARATA DRAW");
	lyLeftleft->addWidget(btnDRAW);

	//*************************************************************************


	//COMPONENTA LEFT
	QWidget* left = new QWidget;
	QVBoxLayout* lyLeft = new QVBoxLayout;
	left->setLayout(lyLeft);

	//adaugare
	QWidget* form = new QWidget;
	QFormLayout* lyForm = new QFormLayout;
	form->setLayout(lyForm);
	this->editDenumire = new QLineEdit;
	this->editDestinatie = new QLineEdit;
	this->editTip = new QLineEdit;
	this->editPret = new QLineEdit;

	lyForm->addRow(lblDenumire, editDenumire);
	lyForm->addRow(lblDestinatie, editDestinatie);
	lyForm->addRow(lblTip, editTip);
	lyForm->addRow(lblPret, editPret);
	btnAddOferta = new QPushButton("Adauga Oferta");

	lyLeft->addWidget(form);
	lyLeft->addWidget(btnAddOferta);

	//stergere
	btnDellOferta = new QPushButton("Sterge oferta");
	lyLeft->addWidget(btnDellOferta);

	//modificare
	btnModifyOferta = new QPushButton("Modifica oferta");
	lyLeft->addWidget(btnModifyOferta);

	//cautare
	btnFindOferta = new QPushButton("Cauta oferta");
	lyLeft->addWidget(btnFindOferta);

	//undo
	btnUndo = new QPushButton("Undo");
	lyLeft->addWidget(btnUndo);

	//filtrare
	QWidget* formFilter = new QWidget;
	QFormLayout* lyFormFilter = new QFormLayout;
	formFilter->setLayout(lyFormFilter);
	editFilterDestinatie = new QLineEdit;
	lyFormFilter->addRow(lblFilterDestinatie, editFilterDestinatie);
	btnFilterDestinatie = new QPushButton("Filtreaza dupa destinatie");
	lyFormFilter->addWidget(btnFilterDestinatie);

	editFilterPret = new QLineEdit;
	lyFormFilter->addRow(lblFilterPret, editFilterPret);
	btnFilterPret = new QPushButton("Filtreaza dupa pret");
	lyFormFilter->addWidget(btnFilterPret);

	lyLeft->addWidget(formFilter);


	//sortare
	QVBoxLayout* lyRadioBox = new QVBoxLayout;
	this->groupBoxSort->setLayout(lyRadioBox);
	lyRadioBox->addWidget(radioSortDenumire);
	lyRadioBox->addWidget(radioSortDestinatie);
	lyRadioBox->addWidget(radioSortTipPret);

	btnSortOferte = new QPushButton("Sorteaza oferte");
	lyRadioBox->addWidget(btnSortOferte);
	lyRadioBox->addWidget(groupBoxSort);

	lyLeft->addWidget(groupBoxSort); //adaugam in partea stanga.

	//reload data
	btnReloadData = new QPushButton("Reload data");
	lyLeft->addWidget(btnReloadData);


	//COMPONENTA RIGHT
	QWidget* right = new QWidget;
	QVBoxLayout* lyRight = new QVBoxLayout;
	right->setLayout(lyRight);

	int noLines = 10;
	int noColums = 4;
	this->tableOferte = new QTableWidget(noLines, noColums);

	//setez header-ul
	QStringList tblHeaderList;
	
	tblHeaderList << "Denumire" << "Destinatie" << "Tip" << "Pret";
	this->tableOferte->setHorizontalHeaderLabels(tblHeaderList);

	//obtiune pentru a redimensiona celulele din tabel in functie de continut
	this->tableOferte->horizontalHeader()->setSectionResizeMode(QHeaderView::ResizeToContents);

	lyLeft->addWidget(tableOferte);


	lyMain->addWidget(left);
	lyMain->addWidget(right);

	//tip
	QWidget* btn_widget = new QWidget;
	btn_layout = new QVBoxLayout;
	btn_widget->setLayout(btn_layout);
	lyMain->addWidget(btn_widget);
	gui_addTip();

}

void ConsoleGUI::reloadOferteList(vector<Turism> oferte) {
	this->tableOferte->clearContents();
	this->tableOferte->setRowCount((int)oferte.size());

	int lineNumber = 0;
	for (auto& oferta : oferte) {
		this->tableOferte->setItem(lineNumber, 0, new QTableWidgetItem(QString::fromStdString(oferta.getDenumire())));
		this->tableOferte->setItem(lineNumber, 1, new QTableWidgetItem(QString::fromStdString(oferta.getDestinatie())));
		this->tableOferte->setItem(lineNumber, 2, new QTableWidgetItem(QString::fromStdString(oferta.getTip())));
		this->tableOferte->setItem(lineNumber, 3, new QTableWidgetItem(QString::number(oferta.getPret())));
		lineNumber++;
	}
}

void ConsoleGUI::connectSignalsSlots() {
	QObject::connect(btnAddOferta, &QPushButton::clicked, this, &ConsoleGUI::gui_AddOferta);

	QObject::connect(btnDellOferta, &QPushButton::clicked, this, &ConsoleGUI::gui_DellOferta);

	QObject::connect(btnModifyOferta, &QPushButton::clicked, this, &ConsoleGUI::gui_ModifyOferta);

	QObject::connect(btnUndo, &QPushButton::clicked, this, &ConsoleGUI::gui_undo);

	QObject::connect(btnFindOferta, &QPushButton::clicked, [&]() {
		string find = this->editDenumire->text().toStdString();
		Turism oferta = srv.search(find);
		vector<Turism> foundTurism;
		foundTurism.push_back(oferta);
		reloadOferteList(foundTurism);
		editDenumire->clear();
		});

	QObject::connect(btnFilterDestinatie, &QPushButton::clicked, [&]() {
		string filterC = this->editFilterDestinatie->text().toStdString();
		reloadOferteList(srv.filtrareDestinatie(filterC));
		editFilterDestinatie->clear();
		});

	QObject::connect(btnFilterPret, &QPushButton::clicked, [&]() {
		string filterC = this->editFilterPret->text().toStdString();
		reloadOferteList(srv.filtrarePret(stoi(filterC)));
		editFilterPret->clear();
		});

	QObject::connect(btnSortOferte, &QPushButton::clicked, [&]() {
		if (radioSortDenumire->isChecked())
			reloadOferteList(srv.sortByDenumire());
		else if (radioSortDestinatie->isChecked())
			reloadOferteList(srv.sortByDestinatie());
		else if (radioSortTipPret->isChecked())
			reloadOferteList(srv.sortByTipAndPret());
		});

	QObject::connect(btnReloadData, &QPushButton::clicked, [&]() {
		reloadOferteList(srv.getAllTurism());
		});

}

void ConsoleGUI::gui_AddOferta() {
	try {
		string denumire = editDenumire->text().toStdString();
		string destinatie = editDestinatie->text().toStdString();
		string tip = editTip->text().toStdString();
		int pret = editPret->text().toDouble();

		editDenumire->clear();
		editDestinatie->clear();
		editTip->clear();
		editPret->clear();

		srv.addTurism(denumire, destinatie, tip, pret);
		reloadOferteList(this->srv.getAllTurism());
		
		QMessageBox::information(this, "Info", QString::fromStdString("Oferta adaugata cu succes!"));
		gui_addTip();
	}
	catch (RepoException& re) {
		QMessageBox::warning(this, "Warning", QString::fromStdString(re.getErrorMessage()));
	}
	catch (ValidationException& ve) {
		QMessageBox::warning(this, "Warning", QString::fromStdString("Oferta este invalida!"));
		QMessageBox::warning(this, "Warning", QString::fromStdString(ve.getErrorMessages()));
	}
}

void ConsoleGUI::gui_DellOferta() {
	try {
		//QMessageBox::information(this, "Info", QString::fromStdString("Introduceti titul activitatii pe care doriti sa o stergeti!"));
		string denumire = editDenumire->text().toStdString();

		editDenumire->clear();

		srv.stergereTurism(denumire);
		reloadOferteList(srv.getAllTurism());
		
		QMessageBox::information(this, "Info", QString::fromStdString("Oferta stearsa cu succes!"));
		gui_addTip();
	}
	catch (RepoException& re) {
		QMessageBox::warning(this, "Warning", QString::fromStdString("Oferta cu aceasta denumire nu se gaseste in lista!"));
		QMessageBox::warning(this, "Warning", QString::fromStdString(re.getErrorMessage()));
	}

}

void ConsoleGUI::gui_ModifyOferta() {
	try {
		string denumire = editDenumire->text().toStdString();
		string destinatie = editDestinatie->text().toStdString();
		string tip = editTip->text().toStdString();
		int pret = editPret->text().toDouble();

		editDenumire->clear();
		editDestinatie->clear();
		editTip->clear();
		editPret->clear();

		srv.modifyTurism(denumire, destinatie, tip, pret);
		reloadOferteList(srv.getAllTurism());
		
		QMessageBox::information(this, "Info", QString::fromStdString("Oferta modificata cu succes!"));
		gui_addTip();
	}
	catch (RepoException& re) {
		QMessageBox::warning(this, "Warning", QString::fromStdString("Activitatea cu acest titlu nu se gaseste in lista!"));
		QMessageBox::warning(this, "Warning", QString::fromStdString(re.getErrorMessage()));
	}
}

void ConsoleGUI::gui_undo() {
	try {
		srv.undo();
		reloadOferteList(srv.getAllTurism());
		QMessageBox::information(this, "Info", QString::fromStdString("Undo realizat cu succes!"));
		gui_addTip();
	}
	catch (std::exception()) {
		QMessageBox::warning(this, "Warning", QString::fromStdString("Nu se mai poate face undo!"));
	}
}

void ConsoleGUI::gui_addTip() {
	vector<Turism> oferte = srv.getAllTurism();
	vector<std::pair<string, int>> tipuri;
	for (const auto& a : oferte) {
		bool ok = false;
		int i = 1;
		for (const auto& t : tipuri) {
			if (t.first == a.getTip()) {
				ok = true;
				break;
			}
		}
		if (ok == true)
			tipuri[i].second++;
		else tipuri.emplace_back(a.getTip(), 1);
	}
	QLayoutItem* item;
	while ((item = btn_layout->takeAt(0)) != NULL)
	{
		delete item->widget();
		delete item;
	}


	for (const auto& t : tipuri) {
		const string& tip = t.first;
		const int& nr = t.second;
		auto item1 = new QPushButton(QString::fromStdString(tip));

		QObject::connect(item1, &QPushButton::clicked, [nr] {
			string n = std::to_string(nr);
			auto* lbl = new QLabel(QString::fromStdString(n));
			lbl->show();
			//QMessageBox::information(this, "Info", QString::fromStdString(n));
			});
		btn_layout->addWidget(item1);
	}
}


//PROGRAM*********************************************************************************

void ConsoleGUIWishlist::initializeGUIWishlistComponents() {
	QHBoxLayout* lyMain = new QHBoxLayout;
	this->setLayout(lyMain);


	//COMPONENTA LEFT
	QWidget* left = new QWidget;
	QVBoxLayout* lyLeft = new QVBoxLayout;
	left->setLayout(lyLeft);

	//adaugare
	QWidget* form = new QWidget;
	QFormLayout* lyForm = new QFormLayout;
	form->setLayout(lyForm);
	this->editDenumireW = new QLineEdit;

	lyForm->addRow(lblDenumireW, editDenumireW);
	btnAddWishlist = new QPushButton("Adauga oferta in wishlist");
	lyForm->addWidget(btnAddWishlist);

	lyLeft->addWidget(form);

	//adaugare random
	QWidget* formAddR = new QWidget;
	QFormLayout* lyFormAddR = new QFormLayout;
	formAddR->setLayout(lyFormAddR);
	this->editNr = new QLineEdit;

	lyFormAddR->addRow(lblNr, editNr);
	btnAddRandom = new QPushButton("Adauga oferta random in program");
	lyFormAddR->addWidget(btnAddRandom);

	lyLeft->addWidget(formAddR);

	//export
	QWidget* formEx = new QWidget;
	QFormLayout* lyFormEx = new QFormLayout;
	formEx->setLayout(lyFormEx);
	this->editFile = new QLineEdit;

	lyFormEx->addRow(lblFile, editFile);
	btnExport = new QPushButton("Export");
	lyFormEx->addWidget(btnExport);

	lyLeft->addWidget(formEx);

	//goleste program
	btnGoleste = new QPushButton("Goleste lista de oferte!");
	lyLeft->addWidget(btnGoleste);

	//COMPONENTA RIGHT
	QWidget* right = new QWidget;
	QVBoxLayout* lyRight = new QVBoxLayout;
	right->setLayout(lyRight);

	int noLines = 10;
	int noColums = 4;
	this->tableWishlist = new QTableWidget(noLines, noColums);

	//setez header-ul
	QStringList tblHeaderList;
	tblHeaderList << "Denumire" << "Destinatie" << "Tip" << "Pret";
	this->tableWishlist->setHorizontalHeaderLabels(tblHeaderList);

	//obtiune pentru a redimensiona celulele din tabel in functie de continut
	this->tableWishlist->horizontalHeader()->setSectionResizeMode(QHeaderView::ResizeToContents);

	lyRight->addWidget(tableWishlist);

	lyMain->addWidget(left);
	lyMain->addWidget(right);

}

void ConsoleGUIWishlist::reloadOferteListFromWishlist(vector<Turism> oferte) {
	this->tableWishlist->clearContents();
	this->tableWishlist->setRowCount((int)oferte.size());

	int lineNumber = 0;
	for (auto& oferta : oferte) {
		this->tableWishlist->setItem(lineNumber, 0, new QTableWidgetItem(QString::fromStdString(oferta.getDenumire())));
		this->tableWishlist->setItem(lineNumber, 1, new QTableWidgetItem(QString::fromStdString(oferta.getDestinatie())));
		this->tableWishlist->setItem(lineNumber, 2, new QTableWidgetItem(QString::fromStdString(oferta.getTip())));
		this->tableWishlist->setItem(lineNumber, 3, new QTableWidgetItem(QString::number(oferta.getPret())));
		lineNumber++;
	}
}

void ConsoleGUIWishlist::connectSignalsSlotsProg() {
	QObject::connect(btnAddWishlist, &QPushButton::clicked, this, &ConsoleGUIWishlist::gui_AddWishlist);
	QObject::connect(btnAddRandom, &QPushButton::clicked, this, &ConsoleGUIWishlist::gui_AddWishlistRandom);

	QObject::connect(btnGoleste, &QPushButton::clicked, [&]() {
		srv.golesteWishlist();
		QMessageBox::information(this, "Info", QString::fromStdString("Lista de oferte din wishlist a fost golita!"));
		reloadOferteListFromWishlist(srv.getAllWishlist());
		});

	QObject::connect(btnExport, &QPushButton::clicked, this, &ConsoleGUIWishlist::gui_Export);
}


void ConsoleGUIWishlist::gui_AddWishlist() {
	try {
		string denumire = editDenumireW->text().toStdString();

		editDenumireW->clear();
		srv.storeWishlist(denumire);
		reloadOferteListFromWishlist(this->srv.getAllWishlist());

		QMessageBox::information(this, "Info", QString::fromStdString("Oferta adaugata cu succes in wishlist!"));
	}
	catch (RepoException& re) {
		QMessageBox::warning(this, "Warning", QString::fromStdString(re.getErrorMessage()));
	}
	catch (std::exception) {
		QMessageBox::warning(this, "Warning", QString::fromStdString("Oferta se afla deja in wishlist!"));
	}
}

void ConsoleGUIWishlist::gui_AddWishlistRandom() {
	try {
		string n = editNr->text().toStdString();
		int nr;

		editNr->clear();

		nr = stoi(n);
		srv.storeRandom(nr);
		reloadOferteListFromWishlist(this->srv.getAllWishlist());

		QMessageBox::information(this, "Info", QString::fromStdString("Oferte adaugate random cu succes in wishlist!"));
	}
	catch (RepoException& re) {
		QMessageBox::warning(this, "Warning", QString::fromStdString(re.getErrorMessage()));
	}
}

void ConsoleGUIWishlist::gui_Export() {
	try {
		string fileName = editFile->text().toStdString();

		editFile->clear();
		srv.saveWishlistToFile(fileName);
		reloadOferteListFromWishlist(this->srv.getAllWishlist());

		QMessageBox::information(this, "Info", QString::fromStdString("Wishlistul a fost adaugat in fisier!"));
	}
	catch (RepoException&) {
		QMessageBox::warning(this, "Warning", QString::fromStdString("Fisierul nu se poate deschide"));
	}
}