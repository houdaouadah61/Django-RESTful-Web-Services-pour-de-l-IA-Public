temperature = input(
    "Saisissez une température en Fahrenheit : ")

unite = temperature[-1].upper()
valeur = float(temperature[:-1])

if unite == "F":
    resultat = (valeur - 32) * 5 / 9
    print("La température en Celsius est de", round(resultat, 2), "degrés.")

elif unite == "C":
    resultat = valeur * 9 / 5 + 32
    print("La température en Fahrenheit est de", round(resultat, 2), "degrés.")

else:
    print("Unité incorrecte. Utilisez C ou F.")