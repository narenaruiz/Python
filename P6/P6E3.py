"""3.-Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.
Escribe una nota: 7.5
Escribe una nota: 0
Escribe una nota: 10
Escribe una nota: -1
Las notas que has Escrito son [7.5, 0.0, 10.0]
Autor:Nicolás Arena Ruiz
"""
notas=[]
entrada=float(input("Dime una nota entre 0 y 10 (si quieres salir pon un numero mayor a 10):"))
while(entrada<=10 and entrada>=0):
    notas.append(entrada)
    entrada=float(input("Dime una nota entre 0 y 10 (si quieres salir pon un numero mayor a 10):"))
print("La lista es",notas)
