#include "Repository.h"
#include <fstream>
#include <sstream>
#include <iostream>
#include <functional>
#include <algorithm>
#include <assert.h>

bool TurismRepository::exists(const Turism& s) {
	try {
		//string denumire, string destinatie, string tip
		find(s.getDenumire());
		return true;
	}
	catch (RepoException) {
		return false;
	}
}

const Turism& TurismRepository::find(string denumire) {
	//for (const Turism& s : this->allTuristi) {
	//	if (s.getDenumire() == denumire && s.getDestinatie() == destinatie && s.getTip() == tip) {
	//		return s;
	//	}
	//}
	//std::cout << "Locatia de turism cu Denumirea: " + denumire + " Destinatia " + destinatie + " si Tipul " + tip + " nu se afla in lista\n";
	//throw RepoException("Locatia de turism cu Denumirea: " + denumire + " Destinatia " + destinatie + " si Tipul " + tip + " nu se afla in lista");
	
	vector <Turism>::iterator f = std::find_if(this->allTuristi.begin(), this->allTuristi.end(),
		[=](const Turism& a) {
			return a.getDenumire() == denumire;
		});
	if (f != this->allTuristi.end())
		return (*f);
	else
		throw RepoException("Oferta de turism cu dennumirea " + denumire + " nu exista!");
}

void TurismRepository::store(const Turism& s) {
	if (exists(s)) {
		/*
		* string getDenumire() const;
		* string getDestinatie() const;
		* string getTip() const;
		* int	   getPret() const;
		*/
		// find(s.getDestinatie(), s.getTip());
		//std::cout << "Locatia de turism  cu Destinatia: " + s.getDestinatie() + " si Tipul: " + s.getTip() + " exista deja\n";
		//cout << s.getDenumire() << " " << s.getDestinatie() << " " << s.getTip() << '\n';
		throw RepoException("Locatia de turism exista deja");
	}
	this->allTuristi.push_back(s);
}

void TurismRepository::sterge(Turism& a) {
	for (int i = 0; i < this->allTuristi.size(); i++) {
		if (a.eq(this->allTuristi[i]) == true)
		{
			this->allTuristi.erase(this->allTuristi.begin() + i);
			break;
		}
	}
}

void TurismRepository::modify(Turism& a) {

	Turism aux = find(a.getDenumire());
	if (!exists(a)) {
		//throw RepoException("Oferta cu denumirea " + aux.getDenumire() + " nu exista!");
		//cout << "Oferta nu exista";
	}
	else {
		for (int i = 0; i < this->allTuristi.size(); i++) {
			if (a.getDenumire() == allTuristi[i].getDenumire()) {
				this->allTuristi[i].setDenumire(a.getDenumire());
				this->allTuristi[i].setDestinatie(a.getDestinatie());
				this->allTuristi[i].setTip(a.getTip());
				this->allTuristi[i].setPret(a.getPret());
				break;
			}
		}
	}
}

size_t TurismRepository::get_dim() {
	return this->allTuristi.size();
}


const vector<Turism>& TurismRepository::getAllTurism() {
	return this->allTuristi;
}


//FISIER
void TurismRepositoryFile::loadFromFile() {
	std::ifstream in(fileName);
	if (!in.is_open()) { // verifica daca fisierul se poate deschide
		//throw RepoException("Fisierul nu se poate deschide!");
	}
	std::string line;
	while (getline(in, line)) {
		std::string denumire, destinatie, tip;
		double pret = 0;
		std::stringstream linestream(line);
		std::string current_item;
		int no = 0;
		while (std::getline(linestream, current_item, ';')) {
			if (no == 0)
				denumire = current_item;
			else if (no == 1)
				destinatie = current_item;
			else if (no == 2)
				tip = current_item;
			else if (no == 3) {
				pret = std::stod(current_item);
			}
			no++;
		}
		
		Turism a{ denumire, destinatie, tip, int(pret)};
		TurismRepository::store(a);
	}
	in.close();
}

void TurismRepositoryFile::saveToFile() {
	std::ofstream out(fileName);
	if (!out.is_open()) {
		//throw RepoException("Fisierul nu se poate deschide!");
	}
	for (auto& oferte : getAllTurism()) {
		out << oferte.getDenumire() << ";" << oferte.getDestinatie() << ";" << oferte.getTip() << ";" << oferte.getPret() << std::endl;
	}
	out.close();
}

void TurismRepositoryFile::store(const Turism& a) {
	TurismRepository::store(a);
	saveToFile();
}

void TurismRepositoryFile::sterge(Turism& a) {
	TurismRepository::sterge(a);
	saveToFile();
}

void TurismRepositoryFile::modify(Turism& a) {
	TurismRepository::modify(a);
	saveToFile();
}



//TESTE

void testGet_Dim() {
	TurismRepository test;
	test.get_dim();
}

void test_load_save() {

	TurismRepositoryFile test_repo{ "E:\\Facultate\\An1\\Sem2\\Programare orientata pe obiect\\Teme\\Agentie de turism\\Problema 6\\Problema 6\\test.txt" };

	Turism turism1{ "Muzica stradala","Floresti","munte",600 };
	Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	test_repo.store(turism1);
	test_repo.store(turism2);

	vector <Turism> all_Turisti = test_repo.getAllTurism();
	assert(all_Turisti.size() == 2);

	Turism turism3{ "Muzica stradala","Cluj-Napoca","hotel", 100 };
	test_repo.modify(turism3);
	vector<Turism> lista = test_repo.getAllTurism();
	assert(lista[0].getDenumire()=="Muzica stradala");
	assert(lista[0].getTip()=="hotel");

	test_repo.sterge(turism2);
	test_repo.sterge(lista[0]);
	all_Turisti = test_repo.getAllTurism();
	assert(all_Turisti.size() == 0);
}

void testGetAllTurism() {
	TurismRepository test_repo;
	vector<Turism> lista = test_repo.getAllTurism();
	assert(lista.size() == 0);
}

void testAddRepo() {
	TurismRepository testRepo;
	//string denumire, string destinatie, string tip, int pret
	Turism turism1{"La prapastia din vale","Floresti","munte",200};
	testRepo.store(turism1);
	assert(testRepo.getAllTurism().size() == 1);

	Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	Turism turism3{ "La prapastia din vale","Floresti","munte",9800 };
	//testRepo.store(turism3);
	try {
		testRepo.store(turism3);
		//modif ->
		//assert(false);
	}
	catch (RepoException) {
		assert(true);
	}
}

void testFindRepo() {
	//
	TurismRepository testRepo;
	Turism turism1{ "La prapastia din vale","Floresti","munte",200 };
	Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	Turism turism3{ "In campul de lalele","Cluj-Napoca","deal",9800 };

	testRepo.store(turism1);
	testRepo.store(turism2);

	assert(testRepo.exists(turism1));
	assert(!testRepo.exists(turism3));

	auto foundTurism = testRepo.find("La prapastia din vale");
	assert(foundTurism.getDenumire() == "La prapastia din vale");
	assert(foundTurism.getDestinatie() == "Floresti");
	assert(foundTurism.getPret() == 200);
	assert(foundTurism.getTip() == "munte");

	try {
		testRepo.find("nowhere");
		//modif ->
		//assert(false);
	}
	catch (RepoException& ve) {
		//cout << ve.getErrorMessage() << '\n';
		assert(ve.getErrorMessage() == "Oferta de turism cu dennumirea nowhere nu exista!");
	}
}

void testStergeRepo() {
	TurismRepository testRepo;
	Turism turism1{ "La prapastia din vale","Floresti","munte",200 };
	Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	Turism turism3{ "In campul de lalele","Cluj-Napoca","deal",9800 };
	testRepo.store(turism1);
	testRepo.store(turism2);
	testRepo.store(turism3);
	
	testRepo.sterge(turism1);
	try {
		testRepo.find("La prapastia din vale");
		//modif ->
		//assert(false);
	}
	catch (RepoException& ve) {
		//cout << ve.getErrorMessage() << '\n';
		assert(ve.getErrorMessage() == "Oferta de turism cu dennumirea La prapastia din vale nu exista!");
	}
}

void testModifyRepo() {
	//cout << "Test\n";
	TurismRepository test_repo;
	Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	Turism turism1{ "La prapastia din vale","Floresti","munte",200 };
	test_repo.store(turism2);
	test_repo.store(turism1);
	//cout << "Test2\n";

	Turism turism3{ "La Veriku","Floresti","munte",200};
	test_repo.modify(turism3);
	vector <Turism> lista = test_repo.getAllTurism();

	//cout << lista[0].getDenumire();
	assert(lista[0].getDenumire() == "La Veriku");
	assert(lista[0].getDestinatie() == "Floresti");
	assert(lista[0].getTip() == "munte");
	assert(lista[0].getPret() == 200);
	//cout << "Test3\n";

	Turism turism4{ "In campul de lalele","Cluj-Napoca","deal",9800 };
	try {
		test_repo.modify(turism4);
	}
	catch (RepoException&) {
		assert(true);
	}
	//cout << "Test4\n";
}

void testeRepo() {
	testAddRepo();
	testFindRepo();
	testStergeRepo();
	
	test_load_save();
	testModifyRepo();
	testGetAllTurism();
	testGet_Dim();
}