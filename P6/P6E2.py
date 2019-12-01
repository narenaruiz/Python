"""2.-Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, simplemente escribe “Salir”. El programa termina escribiendo la lista de números.
Escribe un nombre: 14
Escribe una otro nombre: 123
Escribe una otro nombre: -25
Escribe una otro nombre: 123
Escribe una otro nombre: Salir
Los números que has escrito son [14, 123, -25, 123]
Autor: Nicolás Arena Ruiz
"""
palabras=[]

entrada=input("Dame un numero (si quieres salir pon 'salir'):")
while(entrada!="salir"):
    palabras.append(entrada)
    entrada=input("Dame otro numero (si quieres salir pon 'salir'):")
print("La lista de numeros es:",palabras)
