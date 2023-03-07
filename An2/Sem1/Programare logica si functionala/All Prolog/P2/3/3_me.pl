%a) Sa se sorteze o lista cu eliminarea dublurilor. De ex: [4 2 6 2 3 4]
% => [2 3 4 6]
%a---------------------------------------

%(i,i,o)
%eliminaElement([H|T],Element,Rezultat).

%(i,i,o)
eliminaElement([],_,[]):-!.
eliminaElement([H|T],Element,T2):-
    H =:= Element,
    !,
    eliminaElement(T,Element,T2).
eliminaElement([H|T],Element,[H|T2]):-
    eliminaElement(T,Element,T2).

%(i,o)
minim([],9999):-!.
minim([H|T],Rezultat):-
    minim(T,Rezultat),
    Rezultat < H,
    !.
minim([H|_],H).

sortareLista([],[]):-!.
sortareLista([H|T],[Val|T1]):-
    minim([H|T],Val),
    eliminaElement([H|T],Val,ListaNoua),
    sortareLista(ListaNoua,T1).






% b) Se da o lista eterogena, formata din numere intregi si liste de
% numere. Sa se sorteze fiecare sublista fara pastrarea dublurilor. De
% ex:
%[1, 2, [4, 1, 4], 3, 6, [7, 10, 1, 3, 9], 5, [1, 1, 1], 7] =>
%[1, 2, [1, 4], 3, 6, [1, 3, 7, 9, 10], 5, [1], 7].
%b---------------------------------------


subListSort([],[]):-!.
subListSort([H|T],[Val|T1]):-
    is_list(H),
    !,
    sortareLista(H,Val),
    subListSort(T,T1).
subListSort([H|T],[H|T1]):-
    subListSort(T,T1).
