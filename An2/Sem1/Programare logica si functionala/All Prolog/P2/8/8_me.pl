%a) Definiti un predicat care determina succesorul unui numar
% reprezentat cifra cu cifra intr-o lista. De ex: [1 9 3 5 9 9] => [1 9 3
% 6 0 0]

%(i,i,i,o)
suma([],[],1,[1]):-!.
%Best Cas cazul in care sunt egale si nu avem imprumut
suma([],[],0,[]):-!.

%---------------------------------
suma([H|T],[],1,[Val|T1]):-
    Val is H+1,
    Val < 10,
    !,
    suma(T,[],0,T1).
suma([H|T],[],1,[Val2|T1]):-
    Val is H+1,
    Val >= 10,
    !,
    Val2 is Val - 10,
    suma(T,[],1,T1).

suma([],[H|T],1,[Val|T1]):-
    Val is H+1,
    Val < 10,
    !,
    suma([],T,0,T1).
suma([],[H|T],1,[Val2|T1]):-
    Val is H+1,
    Val >= 10,
    !,
    Val2 is Val - 10,
    suma([],T,1,T1).

%----------------------------------
suma([],[H|T],0,[H|T]):-!.
suma([H|T],[],0,[H|T]):-!.

%Cazul in care in continuare trebuie sa ne imprumutam
suma([H|T],[H1|T1],1,[Val2|T2]):-
    Val is H+H1+1,
    Val >= 10,
    !,
    Val2 is H+H1+1-10,
    suma(T,T1,1,T2).
%Cazul in care nu mai este nevoie sa ne imprumutam pe mai departe
suma([H|T],[H1|T1],1,[Val2|T2]):-
    Val is H+H1+1,
    Val < 10,
    !,
    Val2 is H+H1+1,
    suma(T,T1,0,T2).
%Cazul in care trebuie sa ne imprumutam pe mai departe
suma([H|T],[H1|T1],0,[Val2|T2]):-
    Val is H+H1,
    Val < 10,
    !,
    Val2 is H+H1,
    suma(T,T1,0,T2).
%Cazul in care nu trebuie sa ne imprumutam
suma([H|T],[H1|T1],0,[Val2|T2]):-
    Val is H+H1,
    Val>=10,
    !,
    %write('intrat'),nl,
    Val2 is H+H1-10,
    suma(T,T1,1,T2).

%(i,i,o)
invers([],Rezultat,Rezultat):-!.
invers([H|T],Lista,Rezultat):-
    invers(T,[H|Lista],Rezultat).

%(i,i,o)
adunare(A,B,Rezultat):-
    invers(A,[],Ra),
    invers(B,[],Rb),
    suma(Ra,Rb,0,Rez),
    invers(Rez,[],Rezultat).

rezolvare([H|T],Rez):-
    adunare([H|T],[1],Rez).

% b) Se da o lista eterogena, formata din numere intregi si liste de
% cifre. Pentru fiecare sublista sa se determine succesorul numarului
% reprezentat cifra cu cifra de lista respectiva. De ex:
%[1, [2, 3], 4, 5, [6, 7, 9], 10, 11, [1, 2, 0], 6] =>
%[1, [2, 4], 4, 5, [6, 8, 0], 10, 11, [1, 2, 1], 6]

start([],[]):-!.
start([H|T],[Val|T2]):-
    is_list(H),
    !,
    rezolvare(H,Val),
    start(T,T2).
start([H|T],[H|T2]):-
    start(T,T2).
