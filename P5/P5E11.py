"""11.-Escribe un programa que pida un número e imprima todos sus divisores.

Dame un número: 200
Los divisores de 200 son: 1 2 4 5 8 10 20 25 40 50 100 200

Autor: Nicolás Arena Ruiz
"""
numero=int(input("Dime un numero entero:"))
if numero==0:
    print("el numero 0 no tiene divisores.")
else:
    print ("Los divisores de %d son: " %(numero), end=' ')
    for i in range(1,numero+1):
        if numero%i==0:
            print(i,end=' ')

