#pragma once
#include "Wishlist.h"
#include "observer.h"
#include "Service.h"
#include <qwidget.h>
#include <qpushbutton.h>
#include <qtablewidget.h>
#include <qslider.h>
#include <qlayout.h>
#include <vector>

using std::vector;

class WishlistCRUD_GUI : public QWidget, public Observer {
private:
	Wishlist& wishlist;
	TurismStore& srv;
	QWidget* main;
	QHBoxLayout* layout;
	QSlider* slider;
	QTableWidget* table;
	QPushButton* btnAdd;
	QPushButton* btnEmpty;

	void initComponents();
	void connectSignals();

	void populateTable(QTableWidget* table, vector<Turism>& all);

public:
	explicit WishlistCRUD_GUI(Wishlist& wishlist, TurismStore& srv) : wishlist{ wishlist }, srv{ srv }{
		main = new QWidget;
		layout = new QHBoxLayout;
		btnAdd = new QPushButton("Generare oferte random");
		btnEmpty = new QPushButton("Goleste wishlist");
		slider = new QSlider;
		table = new QTableWidget(0, 4);
	};

	void run();

	void update() override;

	~WishlistCRUD_GUI() {
		this->wishlist.removeObserver(this);
	}
};