#include "UI.h"
#include "Service.h"
#include <iostream>
using std::cout;
using std::endl;

void testAll() {
	//Turism.cpp
	testeDomain();
	cout << "Finished domain tests." << endl;
	testeRepo();
	cout << "Finished repo tests." << endl;
	testAddService();
	testService();
	cout << "Finished service test." << endl;
}

void startApp() {
	TurismRepository repo;
	TurismValidator val;
	TurismStore srv{ repo,val };
	ConsoleUI ui{ srv };
	
	ui.run();
}

int main() {
	testAll();
	startApp();
}
