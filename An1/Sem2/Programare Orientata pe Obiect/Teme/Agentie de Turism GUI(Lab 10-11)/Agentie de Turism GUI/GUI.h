#include <vector>
#include <string>
#include <QtWidgets/QApplication>
#include <QLabel>
#include <QPushButton>
#include <QHBoxLayout>
#include <QFormLayout>
#include <QLineEdit>
#include <QTableWidget>
#include <QMessageBox>
#include <QHeaderView>
#include <QGroupBox>
#include <QRadioButton>
#include "Service.h"
#include <QListWidget>
#include "WishlistCRUD_GUI.h"
#include "WishlistREAD_GUI.h"

using std::vector;
using std::string;

class ConsoleGUI : public QWidget , public Observable{
private:
	QVBoxLayout* btn_layout;
	TurismStore& srv;

	//add
	//QGroupBox* groupBoxAdd = new QGroupBox(tr("Adaugare"));

	QLabel* lblDenumire = new QLabel("Denumire: ");
	QLabel* lblDestinatie = new QLabel("Destinatie: ");
	QLabel* lblTip = new QLabel("Tip: ");
	QLabel* lblPret = new QLabel("Pret: ");

	QLineEdit* editDenumire;
	QLineEdit* editDestinatie;
	QLineEdit* editTip;
	QLineEdit* editPret;

	QPushButton* btnAddOferta;

	//dell
	QPushButton* btnDellOferta;

	//modify
	QPushButton* btnModifyOferta;

	//find
	QPushButton* btnFindOferta;

	//filter
	QGroupBox* groupBoxFilter = new QGroupBox(tr("Filtrare"));

	QLabel* lblFilterDestinatie = new QLabel{ "Destinatia dupa care se filtreaza:" };
	QLineEdit* editFilterDestinatie;
	QLabel* lblFilterPret = new QLabel{ "Pretul dupa care se filtreaza:" };
	QLineEdit* editFilterPret;

	QPushButton* btnFilterDestinatie;
	QPushButton* btnFilterPret;

	//sort
	//ok
	QGroupBox* groupBoxSort = new QGroupBox(tr("Tip sortare"));

	QRadioButton* radioSortDenumire = new QRadioButton(QString::fromStdString("Denumire"));
	QRadioButton* radioSortDestinatie = new QRadioButton(QString::fromStdString("Destinatie"));
	QRadioButton* radioSortTipPret= new QRadioButton(QString::fromStdString("Tip+Pret"));
	QPushButton* btnSortOferte;

	QPushButton* btnReloadData;

	QTableWidget* tableOferte;

	//undo
	QPushButton* btnUndo;

	//tip
	QPushButton* btnTip;

	//OBSERVER
	//add
	QLabel* lblDenumireW = new QLabel("Denumire:");
	QLineEdit* editDenumireW;
	QPushButton* btnAddWishlist;

	//add random
	QLabel* lblNr = new QLabel("Numar:");
	QLineEdit* editNr;
	QPushButton* btnAddRandom;

	//goleste program
	QPushButton* btnGoleste;

	//export
	QLabel* lblFile = new QLabel("Fisier:");
	QLineEdit* editFile;
	QPushButton* btnExport;

	//program crud
	QPushButton* btnCRUD;

	//program draw
	QPushButton* btnDRAW;

	void initializeGUIComponents();

	void connectSignalsSlots();

	void reloadOferteList(vector<Turism> Oferte);

	void gui_AddWishlist();
	void gui_AddWishlistmRandom();
	void gui_Export();
	void reloadOfertaListFromWishlist(vector<Turism> oferte);

public:
	ConsoleGUI(TurismStore& srv) : srv{ srv } {
		initializeGUIComponents();
		connectSignalsSlots();
		reloadOferteList(srv.getAllTurism());
	}

	void gui_AddOferta();
	void gui_DellOferta();
	void gui_ModifyOferta();
	void gui_undo();
	void gui_addTip();
};


class ConsoleGUIWishlist :public QWidget {
private:
	TurismStore& srv;

	//add
	//
	QLabel* lblDenumireW = new QLabel("Denumire:");
	QLineEdit* editDenumireW;
	QPushButton* btnAddWishlist;

	//add random
	//
	QLabel* lblNr = new QLabel("Numar:");
	QLineEdit* editNr;
	QPushButton* btnAddRandom;


	//goleste program
	//
	QPushButton* btnGoleste;

	//export
	//
	QLabel* lblFile = new QLabel("Fisier:");
	QLineEdit* editFile;
	QPushButton* btnExport;


	QTableWidget* tableWishlist;


	void initializeGUIWishlistComponents();
	void connectSignalsSlotsProg();
	void reloadOferteListFromWishlist(vector<Turism> oferte);

public:
	ConsoleGUIWishlist(TurismStore& srv) : srv{ srv } {
		initializeGUIWishlistComponents();
		connectSignalsSlotsProg();
		reloadOferteListFromWishlist(srv.getAllWishlist());
	}

	void gui_AddWishlist();
	void gui_AddWishlistRandom();
	void gui_Export();
};