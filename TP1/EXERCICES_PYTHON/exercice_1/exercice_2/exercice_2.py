nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
nombre3 = float(input("Entrez le troisième nombre : "))

nombres = [nombre1, nombre2, nombre3]

nombres.sort()

mediane = nombres[1]

print("La médiane est :", mediane)