numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

nombre_pairs = 0
nombre_impairs = 0

for nombre in numbers:
    if nombre % 2 == 0:
        nombre_pairs += 1
    else:
        nombre_impairs += 1

print("Nombre de nombres pairs :", nombre_pairs)
print("Nombre de nombres impairs :", nombre_impairs)