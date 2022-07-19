#pragma once
#include "Service.h"

class ConsoleUI {
private:
	TurismStore& srv;
public:
	ConsoleUI(TurismStore& srv) :srv{ srv } {};
	ConsoleUI(const ConsoleUI& ot) = delete;
	void printMenu();
	void uiAdd();
	void uiSort();
	void uiFilter();
	void addDefaultTurism();
	void printAllTurism(const vector<Turism>& allTurism);
	void uiStergere();
	void uiModificare();
	void uiSearch();

	void ui_export();
	void ui_undo();

	void ui_adauga_wishlist();
	void ui_adauga_random();
	void ui_goleste_wishlist();
	void print_wishlist();

	void run();
};