%a) Sa se determine cea mai lunga secventa de numere pare consecutive
% dintr-o lista (daca sunt mai multe secvente de lungime maxima, una
% dintre ele).
%a-----------------------------------------------------------------

maxim([],0):-!.
maxim([H|T],Rez):-
    maxim(T,Rez),
    H < Rez,
    !.
maxim([H|_],H).

consecvPar([],0,[]):-!.
consecvPar([H|T],Cont,[H|T2]):-
    Val is H mod 2,
    Val =:= 0,
    !,
    consecvPar(T,Cont2,T2),
    Cont is Cont2 + 1.
consecvPar(_,Cont,List):-
    consecvPar([],Cont,List).

secvLista([],0,_):-!.
secvLista([H|T],Nr,Lista):-
    secvLista(T,Nr,Lista),
    consecvPar([H|T],Nr2,_),
    Nr2 < Nr,
    !.
    %Lista is Lista2.
secvLista([H|T],Nr2,Lista2):-
    consecvPar([H|T],Nr2,Lista2).

% b) Se da o lista eterogena, formata din numere intregi si liste de
% numere intregi. Sa se inlocuiasca fiecare sublista cu cea mai lunga
% secventa de numere pare consecutive din sublista respectiva. De ex: [1,
% [2, 1, 4, 6, 7], 5, [1, 2, 3, 4], 2, [1, 4, 6, 8, 3], 2, [1, 5], 3] =>
% [1, [4, 6], 5, [2], 2, [4, 6, 8], 2, [], 3]
% b-----------------------------------------------------------------

secvSublista([],[]):-!.
secvSublista([H|T],[Val|T2]):-
    is_list(H),
    !,
    secvLista(H,_,Val),
    secvSublista(T,T2).
secvSublista([H|T],[H|T2]):-
    secvSublista(T,T2).
