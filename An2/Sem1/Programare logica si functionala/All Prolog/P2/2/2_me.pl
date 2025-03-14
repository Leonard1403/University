%a) Sa se sorteze o lista cu pastrarea dublurilor. De ex: [4 2 6 2 3 4]
% => [2 2 3 4 4 6]
%a--------------------------------------------------

%(i,o)
minim([],9999):-!.
minim([H|T],Rez):-
    minim(T,Rez),
    H > Rez,
    !.
minim([H|_],H):-!.

%(i,i,o)
eliminaElement([H|T],_,0,[H|T]):-!.
eliminaElement([],_,_,[]):-!.
eliminaElement([H|T],Element,1,T1):-
    H =:= Element,
    !,
    eliminaElement(T,Element,0,T1).
eliminaElement([H|T],Element,1,[H|T1]):-
    eliminaElement(T,Element,1,T1).

%(i,o)
start([],[]):-!.
start([H|T],[Val|T1]):-
    %print([H|T]),nl,
    minim([H|T],Rezultat),
    Val is Rezultat,
    eliminaElement([H|T],Rezultat,1,ListaNoua),
    start(ListaNoua,T1).



% b) Se da o lista eterogena, formata din numEre Intregi Si liste de
% numere. Sa se sorteze fiecare sublista cu pastrarea dublurilor. De ex:
%[1, 2, [4, 1, 4], 3, 6, [7, 10, 1, 3, 9], 5, [1, 1, 1], 7] =>
%[1, 2, [1, 4, 4], 3, 6, [1, 3, 7, 9, 10], 5, [1, 1, 1], 7].
%b---------------------------------------------------

%(i,o)
start2([],[]):-!.
start2([H|T],[Val|T1]):-
    is_list(H),
    !,
    start(H,Val),
    start2(T,T1).
start2([H|T],[H|T1]):-
    not(is_list(H)),
    start2(T,T1).
