# On suppose qu’on a L une liste remplie par des entiers. On veut remplir deux listes L1 et
# L2 à partir de la liste L tel que :
# 1- les nombres pairs dans L seront copiés dans L1.
# 2- Le reste dans L2

L = []
L1 = []
L2 = []

for i in range(5) :
    N = int(input(f"L[{i}] : "))
    L.append(N)

    if N % 2 == 0 :
        L1.append(N)
    else :
        L2.append(N)

print(f"L = {L}")
print(f"L1 (Nombre Pair) = {L1}")
print(f"L2 (Nombre Impair) = {L2}")