resultats = []

for nombre in range(1500, 2701):
    if nombre % 7 == 0 and nombre % 5 == 0:
        resultats.append(str(nombre))

print(",".join(resultats))