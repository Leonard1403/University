%a. Sa se scrie un predicat care transforma o lista intr-o multime, in
%ordinea primei aparitii. Exemplu: [1,2,3,1,2] e transformat in [1,2,3].
%a----------------------

%(i,i)
nu_membru([],_):-!.
nu_membru([H|T],Val):-
    H \== Val,
    nu_membru(T,Val).

%(i,i,o)
invers([],List,List):-!.
invers([H|T],T1,Rez):-
    %write('intrat\n'),
    invers(T,[H|T1],Rez).


%(i,o)
elimina_dubluri([],[]):-!.
elimina_dubluri([H|T],[H|T1]):-
    nu_membru(T,H),
    !,
    elimina_dubluri(T,T1).
elimina_dubluri([H|T],T1):-
    not(nu_membru(T,H)),
    elimina_dubluri(T,T1).

%(i,o)
start(List,Rez):-
    invers(List,[],Rez2),
    elimina_dubluri(Rez2,Rez3),
    invers(Rez3,[],Rez).

%b. Sa se scrie o functie care descompune o lista de numere intr-o lista
% de forma [ lista-de-numere-pare lista-de-numere-impare] (deci lista cu
% doua elemente care sunt liste de intregi), si va intoarce si numarul
% elementelor pare si impare.
%b-----------------------

%descompunere(Lista,Lista_pare,Lista_impare,nr_pare,nr_impare)
%(i,o,o,i,i,o,o)

descompunere([],[],[],Nr_pare,Nr_impare,Nr_pare,Nr_impare):-
    !.

descompunere([H|T],[H|T1],T2,Nr_pare,Nr_impare,Nr_pare3,Nr_impare3):-
    Val is H mod 2,
    Val =:= 0,
    !,
    %print(Val),
    Nr_pare2 is Nr_pare + 1,
    descompunere(T,T1,T2,Nr_pare2,Nr_impare,Nr_pare3,Nr_impare3).
    %Nr_pare is Nr_pare + 1.

descompunere([H|T],T1,[H|T2],Nr_pare,Nr_impare,Nr_pare3,Nr_impare3):-
    Val is H mod 2,
    Val \== 0,
    %print(Val),
    Nr_impare2 is Nr_impare + 1,
    descompunere(T,T1,T2,Nr_pare,Nr_impare2,Nr_pare3,Nr_impare3).

%(i,o,o,o)
start2(Lista,[L1,L2],Rezultat2,Rezultat3):-
    descompunere(Lista,L1,L2,0,0,Rezultat2,Rezultat3).
    %Rezultat1 is [L1,L2].

