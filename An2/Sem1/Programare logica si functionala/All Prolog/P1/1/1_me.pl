
%diferenta (i,i,o) - determinist

%a.Sa se scrie un predicat care intoarce diferenta a doua multimi.
%a-----------------------------

%(i,o)
contine([H|_],O):-
    H is O,
    !.
contine([_|T],O):-
    contine(T,O).


%(i,i,o)
diferenta([],_,[]):-!.
diferenta([H|T],L,Rez):-
    contine(L,H),
    !,
    diferenta(T,L,Rez).
diferenta([H|T],L,[H|Rez]):-
    diferenta(T,L,Rez).

% b.Sa se scrie un predicat care adauga intr-o lista dupa fiecare
% element par valoarea 1. (i,o)
%b-----------------------

%(i,o)
adauga_unu([],[]):-!.
adauga_unu([H|T],[H,1|Rez]):-
    U is H mod 2,
    U =:= 0,
    !,
    adauga_unu(T,Rez).
adauga_unu([H|T],[H|Rez]):-
    adauga_unu(T,Rez).
