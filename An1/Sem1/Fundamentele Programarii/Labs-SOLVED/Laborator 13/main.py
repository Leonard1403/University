
rez = []*10000
def prim(nr):
    if nr == 2:
        return True
    if nr == 3:
        return True
    if nr%2 == 0:
        return False
    for i in range(3,int(nr/2),+2):
        if nr%i == 0:
            return False
    return True

def bkt(k):
    if(k>=0):
        # print(k)
        if k == 0:
            # conditie solutie
            # aici se afiseaza solutile dupa conditile respectate
            print(rez)
        else:
            # solutie candidat
            # ramura de else unde se genereaza numerele prime pentru formarea sumei
            for i in range(2,int(k)+1,+1):

                # print(i)
                # conditie consistenta
                # partea unde se testeaza daca solutia posibila generata respecta
                # sau nu cerintele
                if prim(i) == True:
                    n = len(rez)
                    # print(n)
                    # print("rez:", end = "")
                    # print("intrat")
                    if n==0:
                        rez.append(i)
                        n = n + 1
                        # print("k: " + str(k))
                        # print("i: " + str(i))
                        # print(rez)

                        bkt(k - i)
                        rez.pop(n - 1)
                        n = n - 1
                    else:
                        if rez[n-1] <= i:
                            rez.append(i)
                            n = n + 1
                            # print("k: " + str(k))
                            # print("i: " + str(i))
                            # print(rez)

                            bkt(k - i)
                            rez.pop(n - 1)
                            n = n - 1
                    # print("after",end=" ")
                    # print(rez)


def main():
    a = int(input("Introduceti un numar intreg pozitiv: "))
    bkt(int(a))
    # if(prim(a) == True):
    #     print("Numarul este prim")
    # else:
    #     print("Numarul nu este prim")

main()

# Descrierea problemei
#     Solutie candidat:     {x = x0, x1 , x2 , ... , xn} x = {nr | nr - reprezinta un nr prim;nr<=aw} si sum = x0 + x1 + ... + xn; sum = a
#     Conditie consistenta: x = {x0, x1, ..., xn} si V(oricare) i , j (apartin) lui N xi <= xj cu i <= j
#     Conditie solutie:     x = {x0, x1, ..., xn} solutie daca e consistenta si sum = a unde sum
#                           reprezinta sum = x0 + x1 + x2 + ... xn