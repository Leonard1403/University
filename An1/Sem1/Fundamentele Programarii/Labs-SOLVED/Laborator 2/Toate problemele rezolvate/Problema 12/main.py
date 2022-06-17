def main():
    n = int(input("Introduceti un nr: "))

    ok = 0
    if(n==1):
        print(n)
    else:
        d = 2
        while True:
            putere = 2
            copie = d
            while copie!=1:
                ok = 0
                while copie % putere == 0:
                    copie = copie / putere
                    ok = 1
                if ok==1:
                    n = n-1
                    #print(putere,end=" ")
                if n==1:
                    print("Numar: " + str(putere))
                    return 0
                putere = putere + 1
            #print("\n")
            d = d + 1

main()