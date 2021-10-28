print("Escribe un número:")
num = int(input())
print("\n")

while num != 1 : 
    if num % 2 == 0 :
        num = int(num / 2)
    else:
        num = num * 3 + 1
    print(num)
print("\nFin de programa")