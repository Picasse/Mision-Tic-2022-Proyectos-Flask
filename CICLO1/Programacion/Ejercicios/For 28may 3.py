from os import system
system("cls")

print("Digite el numero de estudiantes: ")
n=int(input())
promedio=0
nota=0
acumulador=0
for i in range(n):
    nota=float(input(f"Digite la nota {i+1} (Use punto):"))
    acumulador+=nota
print(f"El promedio es: {acumulador/n:.2f}")
