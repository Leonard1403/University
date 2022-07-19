#pragma once

#include "Turism.h"
//#include <vector>
#include <string>
#include "Vector.h"

using std::string;
//using std::vector;

class ValidationException {
	VectorDinamic<string> errorMsg;
public:
	ValidationException(VectorDinamic<string> errorMessages) :errorMsg{ errorMessages } {};

	string getErrorMessages() {
		string fullMsg = "";
		for (const string e : errorMsg)
		{
			fullMsg += e + "\n";
		}
		return fullMsg;
	}
};

class TurismValidator {
public:
	void valideaza(const Turism& m) {
		VectorDinamic <string> errors;
		if (m.getTip().length() < 2)
			errors.push_back("Tipul locatiei trebuie sa fie mai lung decat 2");
		if (m.getDenumire().length() < 5)
			errors.push_back("Denumirea locatiei este prea scurta");
		if (m.getPret() < 10)
			errors.push_back("Pretul locatiei de turism este de pomana");

		if (errors.size() > 0)
			throw ValidationException(errors);
	}
};