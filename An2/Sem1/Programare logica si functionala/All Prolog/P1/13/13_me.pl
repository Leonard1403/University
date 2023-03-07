%a. Sa se scrie un predicat care transforma o lista intr-o multime, in
% ordinea ultimei aparitii. Exemplu: [1,2,3,1,2] e transformat in
% [3,1,2].
%a-----------------------------------------

%(i,i,o)
invers([],Rezultat,Rezultat):-!.
invers([H|T],Lista,Rezultat):-
    invers(T,[H|Lista],Rezultat).

%(i,i,o)
apare([],_,0):-!.
apare([H|T],Element,Rezultat):-
    H =:= Element,
    !,
    apare(T,Element,Rezultat1),
    Rezultat is Rezultat1 + 1.
apare([_|T],Element,Rezultat):-
    apare(T,Element,Rezultat).

%eliminaElementLista([H|T],Element,Rezultat)
%(i,i,o)
eliminaElementLista([],_,[]):-!.
eliminaElementLista([H|T],Element,[H|T1]):-
    H \== Element,
    !,
    eliminaElementLista(T,Element,T1).
eliminaElementLista([_|T],Element,T1):-
    eliminaElementLista(T,Element,T1).

%(i,o),(i,i)
identic(X,X).

%(i,i,o)
%start([],Rezultat,Rezultat):-
start([],[]):-
    !.

start([H|T],[H|T2]):-
    apare(T,H,Rez),
    Rez\==0,
    %print([H|T]),nl,
    !,
    eliminaElementLista(T,H,Lista),
    start(Lista,T2).
start([H|T],[H|T2]):-
    start(T,T2).

%GRESIT
%--------------------------------------
%start([H|T],_,Rezultat):-
    %apare(T,H,Rez),
    %Rez \== 0,

    %write('Lista: '),print(Lista),nl,
    %write('[H|T]:'),print([H|T]),nl,
    %write('pana aici'),nl,

    %apare(Lista,H,Rez2),

    %write('Rez2: '),print(Rez2),nl,
    %not(Rez2 =:= 1),
    %!,
    %write('intrat'),nl,
    %eliminaElementLista(Lista,H,Lista2),
    %write('Lista2: '),
    %print(Lista2),nl,nl,
    %start(T,Lista2,Rezultat).

%    apare(T,H,Rez),
%    Rez \== 0,
%    eliminaElementLista(T,H,Lista2),
%    start(Lista2,Lista2,Rezultat).

%start([_|T],Lista,Rezultat):-
%    start(T,Lista,Rezultat).
%-------------------------------------


%(i,o)
start_aux([H|T],Rezultat):-
    invers([H|T],[],Rez),
    %print(Rez),
    start(Rez,Rez2),
    invers(Rez2,[],Rezultat).


%b. Sa se calculeze cel mai mare divizor comun al elementelor unei
% liste.
%b------------------------------------------

%(i,i,o)
cmmdc(A,A,A):-!.
cmmdc(A,B,Rezultat):-
    A > B,
    !,
    A1 is A - B,
    cmmdc(A1,B,Rezultat).
cmmdc(A,B,Rezultat):-
    B > A,
    B1 is B - A,
    cmmdc(A,B1,Rezultat).

%(i,i,o)
cmmmc(A,B,Rezultat):-
    Produs is A*B,
    cmmdc(A,B,Rez),
    %!,
    Rezultat is Produs/Rez.

%cmmmcLista(Lista,Rezultat)
%(i,o)
cmmmcLista([Rezultat],Rezultat):-!.
cmmmcLista([H1,H2|T],Rezultat):-
    cmmmc(H1,H2,Rez),
    cmmmcLista([Rez|T],Rezultat).

