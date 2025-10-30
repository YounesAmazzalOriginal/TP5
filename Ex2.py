# Combien Un Nombre Répete D'un nombre X

N = [3.5, 2.1, 7.8, 1.0, 9.2, 4.4, 6.3, 8.1, 5.0, 7.8,
     2.1, 3.5, 9.2, 4.4, 6.3, 10.5, 11.2, 5.0, 4.4, 13.9,
     14.0, 8.1, 15.6, 16.8, 17.3]

X = 4.4
count = 0

for i in range(len(N)) :
    if N[i] == X :
        count += 1

print(f"le nombre {X} répété {count} fois")