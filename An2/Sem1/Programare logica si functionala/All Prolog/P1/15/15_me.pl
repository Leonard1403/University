%a. Sa se scrie un predicat care se va satisface daca o lista are numar
%par de elemente si va esua in caz contrar, fara sa se numere elementele
%listei.
%a--------------------------------

%elemPar([H|T],Ok):-

%(i,i)
elemPar([],0):-!.
elemPar([_|T],1):-
    !,
    elemPar(T,0).
elemPar([_|T],0):-
    elemPar(T,1).

%(i)
start([H|T]):-
    elemPar([H|T],0).



% b. Sa se elimine prima aparitie a elementului minim dintr-o lista de
% numere
%intregi.
%b--------------------------------

%(i,o)
minim([],999):-!.
minim([H|T],Rez):-
    minim(T,Rez),
    H > Rez,
    !.
minim([H|T],H):-
    minim(T,_).

eliminare([],_,0,[]):-!.
eliminare([H|T],Element,0,[H|T1]):-
    !,
    eliminare(T,Element,0,T1).
eliminare([H|T],Element,1,T1):-
    H=:=Element,
    !,
    eliminare(T,Element,0,T1).
eliminare([H|T],Element,1,[H|T1]):-
    not(H=:=Element),
    eliminare(T,Element,1,T1).

start2([H|T],Rezultat):-
    minim([H|T],Rez),
    eliminare([H|T],Rez,1,Rezultat).
