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
	void run();
};