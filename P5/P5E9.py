"""Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje de la siguiente manera:
Anchura del rectángulo: 5
Altura del rectángulo: 4
*****
*   *
*   *
*****
Autor: Nicolás Arena Ruiz
"""
anchurarectangulo=int(input("Dime la anchura del rectangulo:"))
alturarectangulo=int(input("Dime la altura del rectangulo:"))
for i in range(alturarectangulo):
    for j in range(anchurarectangulo):
        if i==0 or i==alturarectangulo-1:
            print("*", end='')
        else:
            if j==0 or j==anchurarectangulo-1:
                print("*", end='')
            else:
                print(' ', end='')
    print()
