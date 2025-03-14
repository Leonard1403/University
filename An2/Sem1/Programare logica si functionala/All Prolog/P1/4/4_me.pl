%a. Sa se scrie un predicat care substituie intr-o lista un element
% printr-o
%alta lista.
%a----------------------------------------

%(i,i,i,o)
%(lista,subsLista,val,Rez)
substituieLista([],_,_,[]):-!.
substituieLista([H|T],List,Val,[List|T2]):-
    H =:= Val,
    !,
    substituieLista(T,List,Val,T2).
substituieLista([H|T],List,Val,[H|T2]):-
    substituieLista(T,List,Val,T2).




%b. Sa se elimine elementul de pe pozitia a n-a a unei liste liniare.
%b----------------------------------------

%(i,i,o)
eliminaLista([],_,[]):-!.
eliminaLista([H|T],0,[H|Rez]):-
    !,
    eliminaLista(T,0,Rez).
eliminaLista([_|T],1,Rez):-
    !,
    eliminaLista(T,0,Rez).
eliminaLista([H|T],N,[H|Rez]):-
    !,
    N2 is N - 1,
    eliminaLista(T,N2,Rez).


