chaine = input("Saisissez une chaîne : ")

nombre_lettres = 0
nombre_chiffres = 0

for caractere in chaine:
    if caractere.isalpha():
        nombre_lettres += 1

    elif caractere.isdigit():
        nombre_chiffres += 1

print("Lettres :", nombre_lettres)
print("Chiffres :", nombre_chiffres)