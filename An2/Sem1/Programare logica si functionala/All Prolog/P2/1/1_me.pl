%a) Definiti un predicat care determina suma a doua numere scrise in
%reprezentare de lista.
%a-----------------------------------------

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



% b) Se da o lista eterogena, formata din numere intregi si liste de
% cifre. Sa se calculeze suma tuturor numerelor reprezentate de subliste.
% De ex:
%[1, [2, 3], 4, 5, [6, 7, 9], 10, 11, [1, 2, 0], 6] =>
%[8, 2, 2].
%b------------------------------------------

%(i,i,o)
start([],Rezultat,Rezultat):-!.
start([Cap|T],Lista,Rezultat):-
    is_list(Cap),
    %write('intrat'),nl,
    !,
    %write('intrat'),nl,
    adunare(Cap,Lista,Rez),!,
    %print(Rez),nl,
    start(T,Rez,Rezultat).
start([Cap|T],Lista,Rezultat):-
    not(is_list(Cap)),
    %write('intrat2'),nl,
    %print(Lista),nl,
    start(T,Lista,Rezultat).

start_aux([H|T],Rezultat):-
    start([H|T],[0],Rezultat).

sublistaSuma([],[0]).
sublistaSuma([Cap|Coada],Rez):-is_list(Cap),!,
    sublistaSuma(Coada,Rez1),
    adunare(Cap,Rez1,Rez),!.
sublistaSuma([_|Coada],Rez):-sublistaSuma(Coada,Rez).
