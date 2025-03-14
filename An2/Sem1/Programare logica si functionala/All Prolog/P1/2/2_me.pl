%a.Sa se scrie un predicat care determina cel mai mic multiplu comun al
%elementelor unei liste formate din numere intregi.

%a--------------------------------
%lista(i,o)

%(i,i,o)
cmmdc(A,A,A):-!.
cmmdc(A,B,Rez):-
    A > B,
    %write(' '),
    %print(A),
    U is A - B,
    !,
    cmmdc(U,B,Rez).

%(i,i,o)
cmmdc(A,B,Rez):-
    A < B,
    U is B - A,
    %!,
    cmmdc(A,U,Rez).

cmmmc(A,B,Rez):-
    cmmdc(A,B,Rez2),
    Prod is A*B,
    Rez is Prod/Rez2.

%(i,o)
lista([H1,H2],Rez):-
    cmmmc(H1,H2,Rez2),
    Rez is Rez2,
    !.
lista([H1,H2|T],Rez):-
    cmmmc(H1,H2,Rez2),
    lista([Rez2|T],Rez).


%b-------------------------------
%b. Sa se scrie un predicat care adauga dupa 1-ul, al 2-lea, al 4-lea,
% al 8-lea ...element al unei liste o valoare v data

%add_lista(lista,valoare,poz,rez)
%(i,i,i,o)

add_lista([],_,0,[]):-!.
add_lista([],Val,_,[Val]):-!.
add_lista([H|T],Val,0,[H|T1]):-
    !,
    add_lista(T,Val,0,T1).
add_lista([H|T],Val,1,[H,Val|T1]):-
    !,
    add_lista(T,Val,0,T1).
add_lista([H|T],Val,Poz,[H|T1]):-
    Poz1 is Poz - 1,
    add_lista(T,Val,Poz1,T1).




