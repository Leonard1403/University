%a. Sa se intercaleze un element pe pozitia a n-a a unei liste.
%a--------------------------------------

%interclasare(Lista,Element,Pozitie,Rezultat)

%(i,i,i,o)
%interclasare([1,2,3,4],10,4,Rezultat).
interclasare([],Element,Pozitie,[Element]):-
    Pozitie \== 0,
    %write('intrat in asta'),nl,
    !.
interclasare([],_,_,[]):-!.
interclasare([H|T],Element,0,[H|T1]):-
    !,
    interclasare(T,Element,0,T1).
interclasare([H|T],Element,1,[H,Element|T1]):-
    !,
    %write('intrat in 1'),nl,
    interclasare(T,Element,0,T1).
interclasare([H|T],Element,Pozitie,[H|T1]):-
    !,
    %write('intrat'),
    %rint(Pozitie),nl,
    Pozitie1 is Pozitie - 1,
    interclasare(T,Element,Pozitie1,T1).
    %print([H|T1]),nl.


%b. Definiti un predicat care intoarce cel mai mare divizor comun al
%numerelor dintr-o lista.
%b---------------------------------------

%(i,i,o)
cmmdc(A,A,A):-!.
cmmdc(A,B,Rez):-
    A > B,
    !,
    A1 is A - B,
    cmmdc(A1,B,Rez).
cmmdc(A,B,Rez):-
    A < B,
    B1 is B - A,
    cmmdc(A,B1,Rez).

%(i,o)
%cmmdcLista([100,120,50],Rezultat).
cmmdcLista([H1,H2],Rez):-
    cmmdc(H1,H2,Rez),
    !.
cmmdcLista([H1,H2|T],Rez):-
    cmmdc(H1,H2,Rezultat),
    cmmdcLista([Rezultat|T],Rez).
