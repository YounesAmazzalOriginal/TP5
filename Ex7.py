m = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

print()
# 2 - Affichez la matrice en utilisant une double boucle for (boucles imbriquées) pour afficher chaque élément, ligne par ligne.
for i in range(3) :
    for j in range(3) :
        print(f"Tout les element : {m[i][j]}" , end=' ')
    break


print()
# 3 - Affichez la valeur de l'élément de la deuxième ligne et de la troisième colonne
for i in range(3) :
    for j in range(3) :
        print(f"2 ligne 3 colonne : {m[1][2]}")
    break


print()
# 4 - Modifiez la valeur de l'élément de la première ligne et de la première colonne
for i in range(3) :
    for j in range(3) :
        m[1][2] = 10
    break
print(f"m = {m}")


print()
# 5 - Affichez l'ensemble de la deuxième ligne
for i in range(3) :
    print(m[1])
    break

print()