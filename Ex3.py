# Remplissage D'une liste de n taille et conté le nombre des nombre positive et negative


L = []
n = int(input("n : "))
print(f"alors T[{n}]")
c_pos,c_neg = 0,0

for i in range(n) :
    p = int(input(f"la valeur de l'élement {i+1} : "))
    L.append(p)

    if L[i] > 0 :
        c_pos += 1
    elif L[i] < 0 :
        c_neg += 1

print(f"L = {L}")

print(f"Le nombre des nombres positifs : {c_pos}")
print(f"Le nombre des nombres negatifs : {c_neg}")