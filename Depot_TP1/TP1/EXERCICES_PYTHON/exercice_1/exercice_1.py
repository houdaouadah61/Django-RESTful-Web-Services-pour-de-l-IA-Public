def test_distinct(nombres):
    nombres_deja_vus = []

    for nombre in nombres:
        if nombre in nombres_deja_vus:
            return False

        nombres_deja_vus.append(nombre)

    return True


print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))