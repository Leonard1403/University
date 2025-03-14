%a) Dandu-se o lista liniara numerica, sa se stearga toate secventele de
% valori consecutive. Ex: sterg([1, 2, 4, 6, 7, 8, 10], L) va produce
% L=[4, 10].

%(i,i,o)
eliminaElement([],_,[]):-!.
eliminaElement([H|T],Element,T2):-
    H =:= Element,
    !,
    eliminaElement(T,Element,T2).
eliminaElement([H|T],Element,[H|T2]):-
    eliminaElement(T,Element,T2).

%(i,o)
%secvConsec(Lista,Rezult)

secvConsec([],_,[]):-!.
secvConsec([H],Last,[H]):-
    H3 is Last + 1,
    H =:= H3,
    !.
secvConsec([H1,H2|T],_,[H1|T2]):-
    H3 is H1 + 1,
    H2 =:= H3,
    %write('intrat'),nl,
    %write([H2|T]),nl,
    !,
    Last2 is H1,
    %write(Last),nl,
    %write('intrat'),
    secvConsec([H2|T],Last2,T2).
secvConsec([H|_],Last,[H|T2]):-
    H3 is Last + 1,
    H3 =:= H,
    !,
    secvConsec([],Last,T2).
secvConsec(_,Last,T2):-
    secvConsec([],Last,T2).

marime([],0):-!.
marime([_|T],Nr):-
    marime(T,Nr2),
    Nr is Nr2 + 1.

eliminaToate(Lista,[],Lista):-!.
eliminaToate([H|T],[H1|T1],Rez):-
    eliminaElement([H|T],H1,Lista),
    eliminaToate(Lista,T1,Rez).

%sterg(Lista,Last,Rezultat)
%sterg([H|T],Last,Rez)

sterg([],[]):-!.
sterg([H|T],[H|Rez]):-
    secvConsec([H|T],0,Lista),
    marime(Lista,Nr),
    %write(Lista),nl,
    Nr =:= 0,
    %write([H|T]),nl,
    !,
    sterg(T,Rez).
sterg([H|T],Rez):-
    %write('Lista: '),
    %write([H|T]),nl,
    secvConsec([H|T],0,Lista),
    eliminaToate([H|T],Lista,ListaNoua),
    sterg(ListaNoua,Rez).


% b) Se da o lista eterogena, formata din numere intregi si liste de
% numere intregi. Din fiecare sublista sa se stearga toate secventele de
% valori consecutive. De ex:
%[1, [2, 3, 5], 9, [1, 2, 4, 3, 4, 5, 7, 9], 11, [5, 8, 2], 7] =>
%[1, [5], 9, [4, 7, 9], 11, [5, 8, 2], 7]

start([],[]):-!.
start([H|T],[Val|T2]):-
    is_list(H),
    !,
    sterg(H,Val),
    start(T,T2).
start([H|T],[H|T2]):-
    start(T,T2).

