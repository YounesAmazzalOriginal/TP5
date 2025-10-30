# Écrire un script pour trouver le deuxième plus grand élément d'une liste sans utiliser la
# méthode sort.
# Le second maximum d’une liste est sa deuxième plus grande valeur. Par exemple, le second
# maximum de [1, 2, 14, 8, 20, 7] est 14. On suppose que les listes considérées ont
# des éléments tous distincts. 


li = [1, 2, 14, 8, 20, 7]

m1 = li[0]


for i in range(len(li)) :
    if li[i] > m1 :
        m1 = li[i]

m1In = li.index(m1)
li.remove(m1)


m2 = li[0]

for i in range(len(li)) :
    if li[i] > m2 :
        m2 = li[i]

li.insert(m1In,m1)

print(f"li = {li}")
print(f"m1 = {m1} , index : {m1In}")
print(f"m2 = {m2}")