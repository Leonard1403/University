%Sa se genereze lista aranjamentelor de Kelemente, cu elementele unei liste date. Ex: [2,3,4] K=2 => [[2,3], [3,2], [2,4], [4,2], [3,4], [4,3]] (nu neaparat in aceastaordine)

%(o,i,i)
%functie de verificare daca exista un element
insereaza([E|L],E,L).
insereaza([H|T],E,[H|L]):- insereaza(T,E,L).

%(i,o)
%functie de calculare lungimii
lungime([],0):-!.
lungime([_|T],N):-lungime(T,N1), N is N1+1.


subm([],[]):-!.
subm([_|T],R):-subm(T,R).
subm([H|T],R):-subm(T,P), insereaza(R,H,P).

aranjament(L,K,R):-subm(L,R),print(R),nl,lungime(R,K).

lista_aranjamente(L,K,R):-findall(Colectat,aranjament(L,K,Colectat),R).

