# Écrire un programme en Python qui transfère les éléments d’une liste à deux dimensions
# M (L lignes et C colonnes, maximum 10×10) dans une liste à une dimension V contenant
# tous les éléments ligne par ligne.

m = [ [1,8,-7] , [88,-6,6] , [5,97,-8] , [3,-1,4] ]
t = []


for i in range(len(m)) :
    for j in range(len(m[0])) :
        t.append(m[i][j])


print(f"m = {m}")
print(f"t = {t}")