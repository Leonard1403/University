
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


def main():
    a = int(input("Introduceti un numar intreg pozitiv: "))
    stack = []
    t = 2
    stack.append(2)
    sum = 2
    # print(a)
    while(len(stack)!=0 and sum != 0):
        # print(stack)
        # print(sum)

        # conditie solutie
        # partea unde se verifica daca suma efectuata poate sau nu sa
        # reprezinte solutia problemei
        if sum == a:
            print(stack)
            n = len(stack)
            sum = sum - stack[n-1]
            stack.pop()
            n = n-1
            if n>0:
                sum = sum - stack[n-1]
                # print("i = " , end="")
                for i in range(stack[n-1]+1,a+1,+1):
                    # print(i,end=" ")
                    if prim(i) == True:
                        stack[n-1] = i
                        sum = sum + stack[n-1]
                        break

        # conditie consistenta
        # configuratia care verifica daca o posibila solutie
        # respecta criterile sau nu
        elif sum > a:
            n = len(stack)
            sum = sum - stack[n - 1]
            stack.pop()
            n = n - 1
            if n > 0:
                sum = sum - stack[n - 1]
                # print("i = ", end="")
                for i in range(stack[n - 1] + 1, a + 1, +1):
                    if prim(i) == True:
                        # print(i)
                        stack[n - 1] = i
                        sum = sum + stack[n - 1]
                        break
            # solutie candidat
            # configuratia partiala care poate conduce sau nu la solutie

        elif sum < a:
            n = len(stack)
            sum = sum + stack[n-1]
            stack.append(stack[n-1])
            # solutie candidat
            # configuratia partiala care poate conduce sau nu la solutie

    # if(prim(a) == True):
    #     print("Numarul este prim")
    # else:
    #     print("Numarul nu este prim")

main()