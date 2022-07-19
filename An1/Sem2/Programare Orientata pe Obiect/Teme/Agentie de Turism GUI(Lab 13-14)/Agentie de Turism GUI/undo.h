#pragma once
//#include "domain.h"
#include "repository.h"

class ActiuneUndo {
public:
	virtual void doUndo() = 0;

	virtual ~ActiuneUndo() = default;
};

class UndoAdd : public ActiuneUndo {
	Turism turism;
	TurismRepository& repo;
public:
	UndoAdd(TurismRepository& repo, const Turism a) : repo{ repo }, turism{ a }{}

	void doUndo() override {
		repo.sterge(turism);
	}

};

class UndoDelete : public ActiuneUndo {
	Turism turism;
	TurismRepository& repo;
public:
	UndoDelete(TurismRepository& repo, const Turism& a) : repo{ repo }, turism{ a }{};

	void doUndo() override {
		repo.store(turism);
	}
};

class UndoModify : public ActiuneUndo {
	Turism a1, a2;
	TurismRepository& repo;

public:
	UndoModify(TurismRepository& repo, const Turism& noua, const Turism& veche) :repo{ repo }, a1{ noua }, a2{ veche }{};

	void doUndo() override {
		repo.sterge(a1);
		repo.store(a2);
	}
};

