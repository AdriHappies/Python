print("\nEste programa realiza la tabla de multiplicar de un número")
print("\n")
print("Escribe un número:")
num = int(input())
multi = 0
print("\n")
print("Tabla de multiplicar:\n")
for i in range(1, 11):
    multi = i * num
    print (str(num) + " * " + str(i) + " = " + str(multi) + "\n")