from domain.entities import Clienti
from domain.entities import Carti
from domain.entities import Perioada
from exceptions.exception import ValidationException


def num_there(s):
    """
    Functia cauta intr-un sir s daca se afla o cifra
    :param s: Sirul s in care cautam cifrele
    :return: returneaza valoarea de adevar sau fals daca se afla o cifra in sirul s
    """
    return any(i.isdigit() for i in s)

def let_there(s):
    """
    Functia cauta intr-un sir s daca se afla o litera
    :param s: Sirul s in care cautam litera
    :return: returneaza valoarea de adevar sau fals daca se afla o litera in sirul s
    """
    return any(i.isalpha() for i in s)

class ClientiValidator:
    """
    Clasa ClientiValidator ne valideaza clientii pe care urmeaza sa ii introducem
    in lista noastra
    """
    def validate(self,clienti):
        errors = []

        if let_there(clienti.getCNP()) == True:
            errors.append("CNP-ul contine litere")
        if len(clienti.getCNP()) != 13:
            errors.append("CNP-ul nu are destule cifre")
        if clienti.getId() < 1:
            errors.append("Id-ul nu este valid")
        if num_there(clienti.getNume()) == True:
            errors.append("Numele contine cifre")

        if len(errors) > 0:
            raise ValidationException(errors)

class CartiValidator:
    def validate(self,carti):
        errors = []
        if int(carti.getId()) < 1:
            errors.append("Id-ul nu are destule caractere")
        if num_there(carti.getAutor()) == True:
            errors.append("Numele contine cifre")

        if len(errors) > 0:
            raise ValidationException(errors)

class InchiriereValidator:
    def validate(self,inchiriere):
        perioada = inchiriere.getPerioada()
        errors = []
        if perioada.getStart() < 1900 or perioada.getStop() > 2100:
            errors.append("Anul nu este valid")

        if len(errors)>0:
            # errors_string = '\n'.join(errors)
            raise ValidationException(errors)