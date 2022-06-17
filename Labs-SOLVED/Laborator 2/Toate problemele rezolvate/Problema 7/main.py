"""
input: 238576       output: 29822
input: 16           output: 2
input: 124          output: 62
input: 50           output: 10
input: 9            output: 3
input: 6            output: 6
"""
n = int(input("Se citeste n: "))
p = int(1)

ok = 0

# def fact(n):
#     if(n==1):
#         return int(1)
#     else:
#         return int(n)*fact(n-1)


# initiem un punct de start cu un element prim
for el in range(1,int(n/2)+1,+1):
    #pornim de la 1 pana la jumatatea numarului n
    #si parcurgem din 1 in 1 fiecare element
    if(n%el==0):
        #daca elementul curent este divizibil , atunci este
        #factor propriu
        p = p * el

print("Produsul tuturor factorilor este: ", p)
