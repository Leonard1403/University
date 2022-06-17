# Gnome sort

# Gnome sort (dubbed stupid sort) is a sorting
# algorithm originally proposed by Iranian computer scientist
# Hamid Sarbazi-Azad (professor of Computer Science and Engineering at Sharif University of Technology)
# [1] in 2000. The sort was first called stupid sort[2] (not to be confused with bogosort), and then later described
# by Dick Grune and named gnome sort.[3]

# procedure gnomeSort(a[]):
#     pos := 0
#     while pos < length(a):
#         if (pos == 0 or a[pos] >= a[pos-1]):
#             pos := pos + 1
#         else:
#             swap a[pos] and a[pos-1]
#             pos := pos - 1

from domain.entities import Clienti
from domain.entities import Carti
from domain.entities import Inchirieri

from domain.validators import CartiValidator

from service.carti_service import CartiService
from repository.carti import CartiMemoryRepository

# def __init__(self, repo, validator):
repo = CartiMemoryRepository()
validator = CartiValidator()
test = CartiService(repo,validator)
da = test.Default()
list = repo.get_all()

# def ret_sec(list):
#     return list[1]

def CMP_LUNGIME_DESCRIERE(a , b):
    # pt carti
    if len(a.getDescriere()) <= len(b.getDescriere()):
        # print(a.getDescriere())
        # print(b.getDescriere())
        return 1
    return 0

def gnomeSort(list,key , reversed , cmp):
    pos = 0
    while pos < len(list):
        if cmp == None:
            # print("Intrat")
            if reversed == False:
                if pos == 0 or key(list[pos]) >= key(list[pos-1]):
                    pos = pos + 1
                else:
                    aux = list[pos]
                    list[pos] = list[pos-1]
                    list[pos-1] = aux
                    pos = pos - 1
            else:
                if pos == 0 or key(list[pos]) <= key(list[pos - 1]):
                    pos = pos + 1
                else:
                    aux = list[pos]
                    list[pos] = list[pos - 1]
                    list[pos - 1] = aux
                    pos = pos - 1
        else:
            # print("Intrat")
            if reversed == False:
                if pos == 0 or (cmp(key(list[pos-1]), key(list[pos])) == 1):
                    pos = pos + 1
                else:
                    aux = list[pos]
                    list[pos] = list[pos-1]
                    list[pos-1] = aux
                    pos = pos - 1
            else:
                print("Intrat")
                if pos == 0 or (cmp(key(list[pos-1]), key(list[pos])) == 0):
                    pos = pos + 1
                else:
                    aux = list[pos]
                    list[pos] = list[pos - 1]
                    list[pos - 1] = aux
                    pos = pos - 1

# test = [125,346,3,-7323,52,645,12,-856,345231,-125]
# test2 = [[12,1],[1265,5],[21,4],[87,6]]
# gnomeSort(test2,key = ret_sec,reversed=False)
# gnomeSort(test2,key = ret_sec,reversed=True)

# print(test2)

def sorted(list, key = lambda x : x , reversed = False , cmp = None):
    # print(cmp)
    gnomeSort(list,key , reversed , cmp )

# sorted(list,lambda x : x.getDescriere())
# sorted(list,reversed= False, cmp = CMP_LUNGIME_DESCRIERE)
# sorted(list,lambda x : x.getTitlu())
# sorted(list)
# sorted(list,reversed=True)
#
# for obj in list:
#     print(obj)
