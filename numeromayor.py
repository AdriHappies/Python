print("Escribe un numero:")
num1 = int(input())
print("Escribe otro numero:")
num2 = int(input())

if num1 < num2:
    print("El numero " + str(num2) + " es mayor que el numero " + str(num1))
elif num1 > num2:
    print("El numero " + str(num1) + " es mayor que el numero " + str(num2))
else:
    print("Ambos números son iguales")