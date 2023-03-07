%a) Definiti un predicat care determina produsul unui numar reprezentat
% cifra cu cifra intr-o lista cu o anumita cifra. De ex: [1 9 3 5 9 9] *
% 2
%=> [3 8 7 1 9 8]

%produs(Lista,Cifra,Imprumut,Rezultat)
%----------------------------------------------------------
%produs([],_,_,[]):-!.
produs([],_,0,[]):-!.
produs([],_,Imprumut,[Imprumut2]):-
    Imprumut \== 0,
    Imprumut2 is Imprumut div 10,
    !.
%----------------------------------
produs([H|T],Element,0,[Val2|T2]):-
    Val is H*Element,
    Val < 10,
    Val2 is Val,
    !,
    %write([H|T]),nl,
    produs(T,Element,0,T2).
    %write(T2),nl.
produs([H|T],Element,Imprumut,[Val2|T2]):-
    Imprumut \== 0,
    %print(Imprumut),nl,
    Val is (H*Element+Imprumut div 10),
    Val < 10,
    %print(Imprumut),nl,
    Val2 is Val,
    !,
    %write([H|T]),nl,
    produs(T,Element,0,T2).
    %write(T2),nl.
produs([H|T],Element,Imprumut,[Val2|T2]):-
    Imprumut \== 0,
    %print(Imprumut),nl,
    Val is (H*Element+Imprumut div 10),
    Val >= 10,
    %write('Imprumut: '),nl,
    %print(Imprumut),nl,
    %print(Val),nl,
    Imprumut2 is (Val - Val mod 10),
    Val2 is Val mod 10,
    !,
    %write([H|T]),nl,
    produs(T,Element,Imprumut2,T2).
    %write(T2),nl.
produs([H|T],Element,0,[Val2|T2]):-
    Val is H*Element,
    Val >= 10,
    !,
    Imprumut is (Val-Val mod 10),
    Val2 is Val-Imprumut,
    %write(Val2),nl,
    produs(T,Element,Imprumut,T2).
    %write(T2),nl.
%----------------------------------------------------------
test(Val,Cat):-
    Cat is 15 mod 10,
    Val is (15-Cat).

invers([],Rezultat,Rezultat):-!.
invers([H|T],Lista,Rezultat):-
    invers(T,[H|Lista],Rezultat).

makeProdus([H|T],Element,Rezultat):-
    invers([H|T],[],Lista),
    %write(Lista),nl,
    produs(Lista,Element,0,Rezultat1),
    invers(Rezultat1,[],Rezultat).


%b) Se da o lista eterogena, formata din numere intregi si maximum 9
% liste de numere intregi. Sa se inlocuiasca fiecare sublista cu
% rezultatul inmultirii sublistei cu numarul de ordine al sublistei
% (prima sublista cu 1, a 2-a cu 2, etc.). De ex:
%[1, [2, 3], [4, 1, 4], 3, 6, [7, 5, 1, 3, 9], 5, [1, 1, 1], 7] =>
%[1, [2, 3], [8, 2, 8], 3, 6, [2, 2, 5, 4, 1, 7], 5, [4, 4, 4], 7]

%prodSublista(Lista,Pozitie,Rezultat)

prodSublista([],_,[]):-!.
prodSublista([H|T],Pozitie,[Val|T2]):-
    is_list(H),
    !,
    Pozitie2 is Pozitie + 1,
    makeProdus(H,Pozitie,Val),
    prodSublista(T,Pozitie2,T2).
prodSublista([H|T],Pozitie,[H|T2]):-
    prodSublista(T,Pozitie,T2).

start([H|T],Rezultat):-
    prodSublista([H|T],1,Rezultat).
