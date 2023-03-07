%a) Sa se interclaseze fara pastrarea dublurilor doua liste sortate.
%a------------------------------------------------------

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

%(i,i)
membru([H|_],H):-!.
membru([_|T],Element):-
    membru(T,Element).

%(i,i,o)
%interclasareListe([H|T],[H1|T1],Rezultat)
interclasareListe([],[],[]):-!.
interclasareListe([H|T],[],[H|T]):-!.
interclasareListe([],[H1|T1],[H1|T1]):-!.

%interclasareListe([H|T],T1,T2):-
%    membru(T2,H),
    %print([H|T]),nl,print(T1),nl,
    %write('se afla deja in Lista'),nl,
%    !,
%    interclasareListe(T,T1,T2).
%interclasareListe(T,[H1|T1],T2):-
%    membru(T2,H1),
    %print([H1|T1]),nl,print(T1),nl,
    %write('se afla deja in Lista'),nl,
%    !,
%    interclasareListe(T,T1,T2).

interclasareListe([H|T],[H1|T1],[H|T2]):-
    H < H1,
    !,
    eliminaElement([H|T],H,Lista1),
    %membru(T2,H),!,
    interclasareListe(Lista1,[H1|T1],T2).
interclasareListe([H|T],[H1|T1],[H1|T2]):-
    H > H1,
    !,
    eliminaElement([H1|T1],H1,Lista2),
    %membru(T2,H1),!,
    interclasareListe([H|T],Lista2,T2).
interclasareListe([H|T],[H1|T1],[H1|T2]):-
    H =:= H1,
    !,
    eliminaElement([H|T],H,Lista1),
    eliminaElement([H1|T1],H1,Lista2),
    interclasareListe(Lista1,Lista2,T2).


%b) Se da o lista eterogena, formata din numere intregi si liste de
% numere sortate. Sa se interclaseze fara pastrarea dublurilor toate
% sublistele. De ex :
%[1, [2, 3], 4, 5, [1, 4, 6], 3, [1, 3, 7, 9, 10], 5, [1, 1, 11], 8] =>
%[1, 2, 3, 4, 6, 7, 9, 10, 11].
%b--------------------------------------------

%(i,o)
start([],[]):-!.
start([H|T],Rezultat):-
    start(T,Rezultat2),
    is_list(H),
    !,
    interclasareListe(H,Rezultat2,Rezultat).
start([_|T],Rezultat):-
    start(T,Rezultat).

