print("Escribe un número inicial:")
inicio = int(input())
print("Escribe un número final:")
fin = int(input())
print("\n")
print("Lista de números pares:")
for i in range(inicio, (fin + 1)):
    if (i % 2) == 0:
        print(i)