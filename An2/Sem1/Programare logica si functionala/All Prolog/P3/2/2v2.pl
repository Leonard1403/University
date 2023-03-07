prim(X):- X > 1,prim_aux(X,2).

prim_aux(X,C):- C > X div 2,!.
prim_aux(X,C):-D is X mod C, D \== 0,C1 is C +1,prim_aux(X,C1).

lista_prima([]):-!.
lista_prima([H|T]):-prim(H),!,lista_prima(T).

suma_prim(X,L):-suma_prim_aux(X,0,L),lista_prima(L).
suma_prim_aux(0,_,[]).
suma_prim_aux(X,C,Rez):- C=<X,C1 is C+1,suma_prim_aux(X,C1,Rez).
suma_prim_aux(X,C,[C|Rez]):-X1 is X-C,X1 >=0, C1 is C+1,suma_prim_aux(X1,C1,Rez).
