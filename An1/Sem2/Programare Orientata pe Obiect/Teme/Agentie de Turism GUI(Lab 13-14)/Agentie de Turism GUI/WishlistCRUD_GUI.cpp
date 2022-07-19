#include "WishlistCRUD_GUI.h"

void WishlistCRUD_GUI::run(){
	this->wishlist.addObserver(this);
		
	this->initComponents();
	this->connectSignals();
	this->update();
	main->show();
}

void WishlistCRUD_GUI::initComponents() {
	main->setLayout(layout);

	table->setSelectionMode(QAbstractItemView::SingleSelection);
	layout->addWidget(table);

	slider->setMinimum(0);
	slider->setMaximum(40);
	slider->setOrientation(Qt::Horizontal);
	slider->setTickPosition(QSlider::TicksAbove);
	layout->addWidget(slider);

	layout->addWidget(btnAdd);
	layout->addWidget(btnEmpty);
}

void WishlistCRUD_GUI::connectSignals() {
	QObject::connect(btnAdd, &QPushButton::clicked, [this]() {
		int number = slider->value();
		srv.storeRandom(number);
		wishlist.notify();
		});

	QObject::connect(btnEmpty, &QPushButton::clicked, [this]() {
		wishlist.goleste_wishlist();
		wishlist.notify();
		});
}

void WishlistCRUD_GUI::populateTable(QTableWidget* table, vector<Turism>& all) {
	this->table->clearContents();
	this->table->setRowCount(static_cast<int>(all.size()));

	int lineNumber = 0;
	for (Turism& oferta : all) {
		this->table->setItem(lineNumber, 0, new QTableWidgetItem(QString::fromStdString(oferta.getDenumire())));
		this->table->setItem(lineNumber, 1, new QTableWidgetItem(QString::fromStdString(oferta.getDestinatie())));
		this->table->setItem(lineNumber, 2, new QTableWidgetItem(QString::fromStdString(oferta.getTip())));
		this->table->setItem(lineNumber, 3, new QTableWidgetItem(QString::number(oferta.getPret())));

		lineNumber++;
	}
}

void WishlistCRUD_GUI::update() {
	this->populateTable(table, this->wishlist.get_all());
}