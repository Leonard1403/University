%a. Sa se scrie un predicat care substituie intr-o lista un element prin
%altul.
%a-------------------------------------------

%(i,i,i,o)
substituie([],_,_,[]):-
    !.
substituie([H|T],Element,Modif,[Modif|T1]):-
    H =:= Element,
    !,
    substituie(T,Element,Modif,T1).
substituie([H|T],Element,Modif,[H|T1]):-
    H \== Element,
    substituie(T,Element,Modif,T1).


%b. Sa se construiasca sublista (lm, ..., ln) a listei (l1, ..., lk).
%b-----------------------------------

%sublista(Lista,Pozitie,M,N,Rezultat)
%(i,i,i,i,o)
sublista([],_,_,_,[]):-!.

sublista([H|T],Pozitie,M,N,[H|T1]):-
    M =< Pozitie,
    Pozitie =< N,
    !,
    Pozitie1 is Pozitie + 1,
    sublista(T,Pozitie1,M,N,T1).
sublista([_|T],Pozitie,M,N,Rezultat):-
    Pozitie1 is Pozitie + 1,
    sublista(T,Pozitie1,M,N,Rezultat).

%(i,i,i,o)
start([H|T],M,N,Rezultat):-
    sublista([H|T],1,M,N,Rezultat).
