#pragma once
#define INIT_CAPACITY 100

template <typename TElem>
class IteratorVectorA;

template <typename TElem>

class VectorDinamic {
private:
	TElem* elems;
	int n;
	int cp;


public:

	
	VectorDinamic() {
		this->n = 0;
		this->cp = INIT_CAPACITY;
		this->elems = new TElem[cp];
	}
	
	VectorDinamic(const VectorDinamic < TElem>& v) {
		n = v.n;
		cp = v.cp;
		elems = new TElem[cp];
		for (int i = 0; i < n; i++)
			elems[i] = v.elems[i];
	}


	void add(const TElem& el) {
		ensureCapacity();
		elems[n++] = el;
	}

	TElem& get(int poz) const {
		return elems[poz];
	}

	void set(int poz, const TElem& el) {
		elems[poz] = el;
	}

	void ensureCapacity() {
		if (n < cp) {
			return; 
		}
		cp *= 2;
		TElem* aux = new TElem[cp];
		for (int i = 0; i < n; i++) {
			aux[i] = elems[i];
		}
		delete[] elems;
		elems = aux;
	}

	void resize() {
		TElem* new_elems = new TElem[cp * 2];
		for (int i = 0; i < n; i++) {
			new_elems[i] = this->elems[i];
		}
		delete[] this->elems;
		this->elems = new_elems;
		this->cp = 2 * cp;
	}

	friend class IteratorVectorA<TElem>;

	IteratorVectorA<TElem> begin()
	{
		return IteratorVectorA<TElem>(*this);
	}

	IteratorVectorA<TElem> end()
	{
		return IteratorVectorA<TElem>(*this, n);
	}

	
	int size() {
		return n;
	}

	
	//void clear() {
	//	if (n != 0) {
	//		delete elems;
	//		this->n = 0;
	//		this->cap = INIT_CAPACITY;
	//		this->elems = new TElem[cp];
	//	}
	//}

	
	void push_back(TElem el) {
		if (this->n == this->cp)
			resize();
		this->elems[n++] = el;
	}

	
	TElem& operator[](int i) {
		return elems[i];
	}

	
	void erase(int poz) {
		for (int i = poz; i < n; i++)
			elems[i] = elems[i + 1];
		n--;
	}

	
	void operator=(const VectorDinamic<TElem>& v) {
		this->n = v.n;
		this->cp = v.cp;
		delete[] this->elems;
		this->elems = new TElem[cp];
		for (int i = 0; i < n; i++)
			this->elems[i] = v.elems[i];
	}


	
	~VectorDinamic() {
		if (elems)
			delete[] elems;
	}

};


template<typename TElem>
class IteratorVectorA {
private:
	const VectorDinamic<TElem>& v;
	int poz = 0;
public:
	IteratorVectorA(const VectorDinamic<TElem>& v) noexcept;

	IteratorVectorA(const VectorDinamic<TElem>& v, int poz)noexcept;

	bool valid()const {
		return poz < v.lg;
	}

	TElem& element() const {
		return v.elems[poz];
	}

	void next() {
		poz++;
	}

	TElem& operator*() {
		return element();
	}

	IteratorVectorA& operator++() {
		next();
		return *this;
	}

	bool operator==(const IteratorVectorA& ot)noexcept {
		return poz == ot.poz;
	}

	bool operator!=(const IteratorVectorA& ot)noexcept {
		return !(*this == ot);
	}
};

template<typename TElem>
IteratorVectorA<TElem>::IteratorVectorA(const VectorDinamic<TElem>& v) noexcept :v{ v } {}

template<typename TElem>
IteratorVectorA<TElem>::IteratorVectorA(const VectorDinamic<TElem>& v, int poz)noexcept : v{ v }, poz{ poz } {}