%scoateDubluri([2,3,1,2,5,3,2,1,2,1,4],Rez,1).

scoateDubluri([],[],_):-!.

scoateDubluri([Cap|Coada],X,Dublura):-
    Cap is Dublura,

    write("fun 1\n"),
    !,
    scoateDubluri(Coada,X,Dublura),

    write("Rez1: "),
    print(X),
    write("\n").

scoateDubluri([Cap|Coada],[Cap|X],Dublura):-
    write("fun 2\n"),
    %!,

    %Cap \== Dublura,
    scoateDubluri(Coada,X,Dublura),

    write("Rez2: "),
    print([Cap|X]),
    write("\n").


listaMultime([],[]).
listaMultime([Cap|Coada],[Cap|X]):- scoateDubluri(Coada,CoadaNoua,Cap),
    listaMultime(CoadaNoua,X),!.
