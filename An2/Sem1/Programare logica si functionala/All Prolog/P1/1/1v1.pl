%cream un predicat care verifica existenta unui nr intr o lista
%contine(L:Lista, Nr:Intreg)
%model flux: (i,i) determinist

contine([H|_],Nr):- Nr is H,!.
contine([_|T],Nr):-contine(T,Nr).

%a
%diferenta(L1:Lista, L2:Lista, Rez:Lista)
%model flux: (i,i,o) determinist

diferenta([],_,[]):-!.
diferenta([H|T],L,Rez):-contine(L,H),!,diferenta(T,L,Rez).
diferenta([H|T],L,[H|Rez]):-diferenta(T,L,Rez).

%b
%adauga 1 in lisa dupa fiecare element par.
%adauga_unu(L:lista, Rez:Lista)
%model flux: (i,o)

adauga_unu([],[]):-!.
adauga_unu([H|T],[H,1|Rez]):- H mod 2 =:= 0,!,adauga_unu(T,Rez).
adauga_unu([H|T],[H|Rez]):-adauga_unu(T,Rez).

