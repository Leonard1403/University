#include "Wishlist.h"
#include <assert.h>
#include <exception>
#include "Repository.h"

using std::shuffle;

void Wishlist::valideaza_turism(const Turism& a) {
	vector <Turism> allTuristi = this->wishlist;
	std::string denumire = a.getDenumire();
	if (std::any_of(allTuristi.begin(), allTuristi.end(),
		[&](Turism& turisme) {return turisme.getDenumire() == denumire; }))
		throw std::exception();
}

void Wishlist::adauga_wishlist(const Turism& a) {
	this->wishlist.push_back(a);
}

void Wishlist::goleste_wishlist() {
	this->wishlist.clear();
}

void Wishlist::adauga_random(vector<Turism> allTuristi, int n) {
	//shuffle(allTuristi.begin(), allTuristi.end(), std::default_random_engine(std::random_device{}()));
	//size_t init_size = wishlist.size();
	//while (wishlist.size() < n + init_size && wishlist.size() > 0) {
	//	wishlist.push_back(wishlist.back());
	//	allTuristi.pop_back();
	//}
	size_t lst = allTuristi.size();
	while (n) {
		int nrdNr = rand() % lst;
		wishlist.push_back(allTuristi[nrdNr]);
		n--;
	}
}

const vector<Turism>& Wishlist::get_all_from_wishlist() {
	return this->wishlist;
}

void test_valideaza() {
	Wishlist wishlist;
	Turism turism1{ "Hotel Unirea","Roman","hotel",200 };
	Turism turism2{ "Hotel Unirea","Roman","hotel",200 };
	wishlist.adauga_wishlist(turism1);
	try {
		wishlist.valideaza_turism(turism2);
	}
	catch (std::exception&)
	{

	}
}

void test_adauga_wishlist() {
	Wishlist wishlist;
	Turism turism1{"Hotel Unirea","Roman","hotel",200};
	wishlist.adauga_wishlist(turism1);
	assert(wishlist.get_all_from_wishlist().size() == 1);

	Turism turism2{ "Casa lui Celibidache","Roman","casa",100 };
	wishlist.adauga_wishlist(turism2);
	assert(wishlist.get_all_from_wishlist().size() == 2);

	//try {
	//	wishlist.adauga_wishlist(turism2);
	//}
	//catch (std::exception) {
	//	assert(false);
	//}
	wishlist.goleste_wishlist();
	assert(wishlist.get_all_from_wishlist().size() == 0);
}

void test_adauga_random() {
	Wishlist wishlist;
	TurismRepository repo;
	Turism turism1{ "Hotel Unirea","Roman","hotel",200 };
	repo.store(turism1);

	Turism turism2{ "Casa lui Celibidache","Roman","casa",100 };
	repo.store(turism2);

	Turism turism3{ "Hotel Roman", "Roman", "hotel", 100 };
	vector<Turism> allTuristi;
	
	wishlist.adauga_random(allTuristi, 2);
	assert(wishlist.get_all_from_wishlist().size() == 0);

	wishlist.goleste_wishlist();
	assert(wishlist.get_all_from_wishlist().size() == 0);
}

void teste_wishlist() {
	test_adauga_wishlist();
	test_adauga_random();
	test_valideaza();
}


