#include "Iterator.h"
#include "DO.h"
#include <iostream>

//using namespace std;

const std :: pair<int, int > NIL(-1, -1);
/*
Iterator DO::iterator() const {
	return Iterator(*this);
}
*/

//void Iterator::deplasare() {
	
//	while ((curent < dict.m) && dict.e[curent].second == -1)
//		curent++;
//}

vector<TElem> Iterator::interclasare(vector<TElem> v1, vector<TElem> v2, Relatie r) {
	auto i = v1.begin();
	auto j = v2.begin();
	vector<TElem> rez;
	while (i != v1.end() && j != v2.end()) {
		if (r(i->first, j->first)) {
			rez.push_back(pair<int, int>(i->first, i->second));
			i++;
		}
		else {
			rez.push_back(pair<int, int>(j->first, j->second));
			j++;
		}
	}
	while (i < v1.end()) {
		rez.push_back(pair<int, int>(i->first, i->second));
		i++;
	}
	while (j != v2.end()) {
		rez.push_back(pair<int, int>(j->first, j->second));
		j++;
	}
	return rez;
}

Iterator::Iterator(const DO& d) : dict(d){
	/* de adaugat */
	
	//curent = 0;
	//deplasare();
	//pair < int, int > NIL(-1, -1);
	bool viz[500];
	for (int i = 0; i < dict.m; i++)
		viz[i] = false;
	vector < vector <TElem>> matr;
	for (int j = 0; j < dict.m; j++) {
		vector <TElem> v;
		for (int i = 0; i < dict.m; i++) {
			TElem crt = pair<int, int>(dict.e[j].first, 0);
			int k = dict.d(crt.first);
			if (dict.e[k] != NIL && !viz[k]) {
				if (!v.empty()) {
					auto last = v.front();
					if ((Relatie)(last.first, dict.e[k].first) && dict.d(last.first) == dict.d(dict.e[k].first)) {
						v.push_back(dict.e[k]);
						viz[k] = true;
					}
					else
						break;
				}
				else {
					v.push_back(dict.e[k]);
					viz[k] = true;
				}
			}
			if (dict.e[k] == NIL)
				break;
		}
		if (!v.empty())
			matr.push_back(v);
	}

	vector <TElem> ordonat;

	for (int i = 0; i < matr.size(); i++) {
		auto v1 = matr[i];
		ordonat = interclasare(v1, ordonat, dict.relatie);
	}

	elems = ordonat;
	pozcrt = elems.begin();
}

void Iterator::prim(){
	/* de adaugat */
	
	//curent = 0;
	//deplasare();
	
	pozcrt = elems.begin();
}

void Iterator::urmator(){
	/* de adaugat */
	
	//curent++;
	//deplasare();
	
	pozcrt++;
}

bool Iterator::valid() const{
	/* de adaugat */

	//return (curent < dict.m);
	//return false;
	return pozcrt != elems.end();
}

TElem Iterator::element() const{
	/* de adaugat */
	
	//return pair <TCheie, TValoare>(dict.e[curent].first, dict.e[curent].second);
	return pair<int, int>(pozcrt->first, pozcrt->second);
	//return pair <TCheie, TValoare>  (-1, -1);
}


