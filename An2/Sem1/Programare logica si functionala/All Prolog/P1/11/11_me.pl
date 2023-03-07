%a. Sa se scrie un predicat care sa testeze daca o lista formata din
%numere
%intregi are aspect de "vale"(o multime se spune ca are aspect de "vale"
%daca elementele descresc pana la un moment dat, apoi cresc. De ex.
%10 8 6 9 11 13).
%a-----------------------------------------

%daca este full crescatoare
%(i)
verificare([H1,H2]):-
    H1 < H2,
    !.
verificare([H1,H2|T]):-
    H1 < H2,
    verificare([H2|T]).

%vale(Lista,Stare)
%0 descreste 1 creste
%(i,i)
vale([_],1):-
    !.
vale([H1,H2|T],1):-
    verificare([H1,H2|T]),
    !.
    %write('ultimul intrat'),nl.
vale([H1,H2|T],0):-
    H1 < H2,
    %write('alt intrat'),nl,
    !,
    vale([H2|T],1).
vale([H1,H2|T],0):-
    H1 > H2,
    %write('intrat'),nl,
    !,
    vale([H2|T],0).

%(i)
start([H|T]):-
    not(verificare([H|T])),
    vale([H|T],0).

%b. Sa se calculeze suma alternanta a elementelor unei liste
%(l1 - l2 + l3 ...).
%b--------------------------------------------

%suma(Lista,Simbol,Rezultat)
%0 - plus | 1 - minus

suma([],_,0):-!.
suma([H|T],1,Rez):-
    !,
    suma(T,0,Rez2),
    Rez is Rez2 - H.
suma([H|T],0,Rez):-
    %Rez is Rez2 + H,
    suma(T,1,Rez2),
    Rez is Rez2 + H.

start_aux([H|T],Rezultat):-
    suma([H|T],0,Rezultat).
