#pragma once
#include "Turism.h"
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>
#include "observer.h"

using std::vector;

class Wishlist : public Observable{
private:
	vector<Turism> wishlist;
public:
	Wishlist() = default;

	vector <Turism>& get_all() {
		return wishlist;
	}
	//adauga o oferta de turism
	void adauga_wishlist(const Turism& a);

	//goleste wishlist
	void goleste_wishlist();

	//adauga random agentii de turism
	void adauga_random(vector<Turism> allTuristi, int n);

	//vector cu toate agentiile de turism
	const vector<Turism>& get_all_from_wishlist();

	void valideaza_turism(const Turism& a);
};

void teste_wishlist();