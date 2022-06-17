from datetime import date

today = date.today()

zi1 = int(today.strftime("%d"))
luna1 = int(today.strftime("%m"))
an1 = int(today.strftime("%Y"))

data = input("Introduceti-va data nasterii sub format zi/luna/an: ")

if(data[2]==data[5]):
    zi2 = int(str(data[0]+data[1]))
    luna2 = int(str(data[3]+data[4]))
    an2 = int(str(data[6]+data[7]+data[8]+data[9]))
    days = 0
    while(an2<an1):
        an2 = an2 + 1
        days = days + 365
    while(luna2<luna1):
        luna2 = luna2 + 1
        days = days + 30
    while(luna2>luna1):
        luna2 = luna2 - 1
        days = days - 30
    while(zi2<zi1):
        zi2 = zi2 + 1
        days = days + 1
    while(zi2>zi1):
        zi2 = zi2 - 1
        days = days - 1
    print(days)
else:
    print("Ati introdus datele gresit")