"""Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura del triángulo: 4
*
**
***
****
Autor: Nicolás Arena Ruiz"""

alturatriangulo=int(input("Dime la altura del triangulo:"))
for i in range(alturatriangulo):
    for j in range(i+1):
        print("*", end='')
    print()
