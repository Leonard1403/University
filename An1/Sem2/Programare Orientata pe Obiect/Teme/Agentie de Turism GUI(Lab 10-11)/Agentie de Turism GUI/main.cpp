#include "UI.h"
#include "GUI.h"
#include <iostream>
#include <filesystem>

#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

#include "AgentiedeTurismGUI.h"
#include <QtWidgets/QApplication>

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
	teste_wishlist();
	cout << "Finished wishlist test." << endl;
	
}

/*
void startApp() {
	TurismRepository repo;
	//TurismRepositoryFile repo{ "E:\\Facultate\\An1\\Sem2\\Programare orientata pe obiect\\Teme\\Agentie de turism\\Problema 6\\Problema 6\\oferte.txt" };
	TurismValidator val;
	Wishlist wishlist;
	TurismStore srv{ repo,val, wishlist };
	ConsoleUI ui{ srv };
	
	ui.run();
}

int main() {
	testAll();
	startApp();
	//cout << "im here";
}
*/

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
	TurismRepositoryFile repo{ "oferte.txt" };
	TurismValidator val;
	Wishlist wishlist;
	TurismStore srv{ repo, val , wishlist };
	ConsoleGUI gui{ srv };
	gui.show();

	ConsoleGUIWishlist guiWishlist{ srv };
	guiWishlist.show();

    return a.exec();
}
