lista = [0]*1000
marime = 0

def citirea_listei():
    global marime
    global lista
    marime = int(input("Marimea listei: "))
    for i in range(1,marime+1):
        x = int(input("Elementul de pe pozitia " + str(i) + " : "))
        lista[i] = x

def afisarea_listei():
    print("Marimea listei este: " + str(marime))
    print("Elementele listei sunt: ",end = "")
    for i in range(1,marime+1):
        print(str(lista[i])+" ",end = "")
    print("\n")

def secv_max_elemconsecv():
    global lista
    secv_max = 0
    secventa = 1
    i1 = 1
    copi1 = 1
    copi2 = 0
    i = 0
    for i in range(2,marime+1):
        if (lista[i-1]<=0 and lista[i]>0) or (lista[i-1]>=0 and lista[i]<0):
            #print("Respecta" + str(lista[i]))
            secventa = secventa + 1
        else:
            secventa = 1
            copi1 = i
        if secventa >= secv_max:
            secv_max = secventa
            i1  = copi1
            i2 = i
    if secventa >= secv_max:
        secv_max = secventa
        i1 = copi1
        i2 = i
    print("Lungimea secventei maxime este: " + str(secv_max))
    print("Secventa maxima cu elemente consecuvite de semne contrare este: " + str(i1) + " | " + str(i2))

def secv_max_sumaelem5():
    i1 = 0
    i2 = 0
    lungime = 0
    maxi1 = 0
    maxi2 = 0
    suma = 0
    lungime_max = 0
    for i in range(1,marime+1):
        suma = 0
        for j in range(i,marime+1):
            suma = int(suma + lista[j])
            #print(suma)
            if suma == 5:
                i1 = i
                i2 = j
                lungime = i2-i1 + 1
                if lungime > lungime_max:
                    maxi1 = i1
                    maxi2 = i2
                    lungime_max = lungime
            elif suma>5:
                break
    print("Secventa de lungime maxima cu proprietatea ca suma elementelor ei este egala cu 5 este")
    print(str(maxi1) + " || " + str(maxi2))
    print("Si are lungimea " + str(lungime_max))

def cif_comun(nr1 , nr2):
    number1 = [0]*10
    number2 = [0]*10
    copie1 = int(nr1)
    copie2 = int(nr2)
    while(copie1!=0):
        number1[int(copie1%10)] = 1
        #print(int(copie1%10))
        copie1 = int(copie1 / 10)
    #print("\n")
    while(copie2!=0):
        number2[int(copie2%10)] = 1
        #print(int(copie2%10))
        copie2 = int(copie2 / 10)
    ok = 0
    # print("Indici: ")
    # for i in range(0,10):
    #     print(str(number1[i])+ " ",end = "")
    # print("\n")
    # for i in range(0,10):
    #     print(str(number2[i])+" ",end = "")
    # print("\n")
    #print("\n")
    for i in range(0,10):
        if(number1[i]==number2[i] and number1[i] == 1):
            ok = ok + 1
        if ok == 2:
            return True
    return False

def secv_max_cifredisct():
    i1 = 1
    i2 = 0
    lungime = 0
    maxi1 = 0
    maxi2 = 0
    lungime_maxima = 0
    global lista
    for i in range(2,marime+1):
        if cif_comun(lista[i],lista[i-1]) == True:
            i2 = i
            lungime = i2-i1 + 1
            if lungime > lungime_maxima:
                maxi1 = i1
                maxi2 = i2
                lungime_maxima = lungime
        else:
            i1 = i
    print("Lungimea maxima a secventei este: " + str(lungime_maxima))
    print("Indicii : " + str(maxi1) + " || " + str(maxi2))


def print_meniu():
    global secv_max
    secv_max = 0
    while True:
        print("1.Citirea unei liste de numere intregi")
        print("2.Secventa de lungime maxima in care oricare doua elemente consecutive sunt de semne contrare")
        print("3.Secventa de lungime maxima in care suma elementelor este egala cu 5")
        print("4.Oricare doua elemente consecutive au cel putin 2 cifre distincte comune")
        print("5.Afisarea listei")
        print("6.Iesirea idn aplicatie")
        n = int(input("Raspuns: "))
        if n == 1:
            citirea_listei()
        elif n == 2:
            secv_max_elemconsecv()
        elif n == 3:
            secv_max_sumaelem5()
        elif n == 4:
            secv_max_cifredisct()
        elif n == 5:
            afisarea_listei()
        elif n == 6:
            return 0

print_meniu()


