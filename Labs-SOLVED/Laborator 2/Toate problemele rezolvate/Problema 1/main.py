n = int(input("Introduceti un numar: "))


def verificare_prim(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    elif x == 3:
        return True
    else:
        i = 3
        for i in range(i, int(x / 2), +2):
            # print(str(i)+ " ",end = "")
            if x % i == 0:
                return False
    return True


copie = n
while True:
    n = n + 1
    # print(str(n) + ":",end = "")
    if verificare_prim(n):
        print("Primul numar prim mai mare decat " + str(copie) + " este : " + str(n))
        break
