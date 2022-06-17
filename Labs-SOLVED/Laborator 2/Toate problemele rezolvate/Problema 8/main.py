"""
Input: 12498714                Output: 98744211
Input: 10000008                Output: 81000000
Input: 3658                    Output: 8653
Input: 1294817                 Output: 9874211
Input: 1249871247812497        Output: 9988777444222111
"""

n = int(input("Introduceti un numar natural n: "))
evidenta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
numar = 0
copie = int(n)
# facem o copie a numarului n


while copie != 0:
    # print(copie%10)
    evidenta[int(copie % 10)] = int(evidenta[int(copie % 10)]) + 1
    # contorizam fiecare cifra a numarului intr-un vector de la 9->0
    copie = int(copie / 10)

for el in range(9, -1, -1):
    while evidenta[el] != 0:
        # parcurgem acest vector de la 9->0 pentru a putea cel mai mare numar generat
        numar = int(numar) * 10 + int(el)
        evidenta[el] = evidenta[el] - 1

print(numar)
