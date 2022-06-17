n = int(input("Introduceti un numar: "))

# prim = [0]*(100015)
# prim[1] = 1
# for i in range(2,int(100001**0.5),+1):
#     if prim[i] == 0:
#         for j in range(i*i,100000,i):
#             prim[j] = 1


# for el in range(1,101):
#     if prim[el]==0:
#         print("Elementul " + str(el) + " este prim")

#0 = ESTE NUMAR PRIM
#1 = NU ESTE NUMAR PRIM

# copie = n
# if(n%2!=0 or n<=3):
#     print("Numarul nu poate fi scris ca suma de doua numere prime")
# else:
#     for el in range(2,int(copie/2)+1,+1):
#         #print(str(el) + " " + str(n-el))
#         if(prim[el]==0 and prim[n-el]==0):
#             print("p1 = " + str(n-el) + " || p2 = " + str(el))
#             break
#
#

def nr_prim(x):
    if(x==1):
        return False
    elif(x==2):
        return True
    elif(x==3):
        return True
    elif(x%2==0):
        return False
    else:
        for el in range(3,int(x**0.5)+1,+2):
            if x%el==0:
                return False
    return True

# print(nr_prim(n))

# copie = n
if(n%2!=0 or n<=3):
    print("Numarul nu poate fi scris ca suma de doua numere prime")
else:
    for el in range(2, int(n / 2) + 1, +1):
        if(nr_prim(el)==True and nr_prim(n-el)==True):
            print("p1 = " + str(n-el) + "    ||    p2 = " + str(el))
            break
