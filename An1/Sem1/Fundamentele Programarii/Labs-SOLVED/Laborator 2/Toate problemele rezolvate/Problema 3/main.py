an = int(input("Introduceti anul: "))
ziua = int(input("Introduceti ziua din anul respectiv: "))

luna = 1

while(ziua>31):
    if(luna==2):
        if(an%4==0):
            ziua = ziua-29
        else:
            ziua = ziua-28
    elif(luna%2==0):
        ziua = ziua-30
    else:
        ziua = ziua-31
    luna = luna + 1

print(str(ziua) + "/" + str(luna) + "/" + str(an))