# Quick Sort


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

# for obj in list:
#     print(obj)


def CMP_LUNGIME_DESCRIERE(a , b):
    # pt carti
    if len(a.getDescriere()) == len(b.getDescriere()):
        if a.getAutor() < b.getAutor():
            return 1
        # print(a.getDescriere())
        # print(b.getDescriere())
    elif len(a.getDescriere()) <= len(b.getDescriere()):
        return 1
    return 0

def swap(a,b):
    aux = a
    a = b
    b = aux

def partition(arr, low, high, key, reversed, cmp ):
    i = (low - 1)  # index of smaller element
    # pivot = key(arr[high])  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if cmp == None:
            if reversed == False:
                if key(arr[j]) <= key(arr[high]) :
                    # increment index of smaller element
                    i = i + 1
                    arr[i] , arr[j] = arr[j] , arr[i]
                    # swap(key([arr[i]),key(arr[j]]))
            else:
                if key(arr[j]) >= key(arr[high]) :
                    # increment index of smaller element
                    i = i + 1
                    arr[i] , arr[j] = arr[j] , arr[i]
                    # swap(key([arr[i]),key(arr[j]]))
        else:
            if reversed == False:
                # print("Am intrat")

                if cmp(key(arr[j]),key(arr[high])):
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]
            else:
                if cmp(key(arr[j]), key(arr[high])) == 0:
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high,key , reversed , cmp ):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high,key , reversed , cmp )

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1,key , reversed  , cmp)
        quickSort(arr, pi + 1, high,key  , reversed , cmp )


def sorted(list, key = lambda x : x , reversed = False , cmp = None):
    # print(cmp)
    quickSort(list,0,len(list)-1,key , reversed , cmp )

# test = [125,346,3,-7323,52,645,12,-856,345231,-125]

# sorted(list,lambda x : x.getDescriere())
# sorted(list,reversed= False, cmp = CMP_LUNGIME_DESCRIERE)
# sorted(list,lambda x : x.getTitlu())
# sorted(list)
# sorted(list,reversed=True)

for obj in list:
    print(obj)
