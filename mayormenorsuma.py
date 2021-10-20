print("Este programa pide 3 números y comprueba cual es mayor")
print("\n")
print("Escribe el primer numero:")
num1 = int(input())
print("Escribe el segundo numero:")
num2 = int(input())
print("Escribe el tercer número")
num3 = int(input())
print("\n")

suma = 0

if (num1 < num2 and num1 < num3 and num2 < num3) or (num3 > num1) :
    print("El mayor es: " + str(num3))
elif (num1 < num2 and num1< num3 and num3 < num2) or (num2 > num1) :
    print("El mayor es: " + str(num2))
elif (num1 > num2 and num1 > num3) or (num1 > num2) or (num1 > num3):
    print("El mayor es: " + str(num1))
else: 
    print("Has introducido el mismo número 3 veces")

print("\n")

if (num1 > num2 and num1 > num3 and num2 > num3) or (num3 < num1) :
    print("El menor es: " + str(num3))
elif (num1 > num2 and num1 > num3 and num3 > num2) or (num2 < num1) :
    print("El menor es: " + str(num2))
elif (num1 < num2 and num1 < num3) or (num1 < num2) or (num1 < num3):
    print("El menor es: " + str(num1))
else: 
    print("Has introducido el mismo número 3 veces")


print("\n")
suma = num1 + num2 + num3
print("La suma de todos los números es: " + str(suma))

print("\n")
print("Fin de programa")