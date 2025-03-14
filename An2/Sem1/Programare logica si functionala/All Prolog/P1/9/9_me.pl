%a. Sa se scrie un predicat care intoarce intersectia a doua multimi.
%a------------------------------------------

%(i,i)
apare([H|_],H):-!.
apare([_|T],Element):-
    apare(T,Element).

%(i,i,o)
elimina([],_,[]):-!.
elimina([H|T],Element,T1):-
    H =:= Element,
    !,
    elimina(T,Element,T1).
elimina([H|T],Element,[H|T1]):-
    elimina(T,Element,T1).

%(i,i,o)
intersectia([],[],[]):-!.
intersectia([],[H1|T1],[H1|T2]):-
    not(apare(T2,H1)),
    intersectia([],T1,T2).
intersectia([],[_|T1],T2):-
    intersectia([],T1,T2).
intersectia([H|T],[H1|T1],[H|T2]):-
    apare([H1|T1],H),
    !,
    intersectia(T,[H1|T1],T2).
intersectia([_|T],[H1|T1],T2):-
    intersectia(T,[H1|T1],T2).

%b. Sa se construiasca lista (m, ..., n), adica multimea numerelor
% intregi
%din intervalul [m, n].
%b---------------------------------------------

%(i,i,o)
creeaza(Nr,Nr,[Nr]):-!.
creeaza(Mr,Nr,[Mr|T]):-
    %write('intrat'),
    M1 is Mr + 1,
    %print(M1),
    creeaza(M1,Nr,T).
