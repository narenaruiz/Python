"""5.-Escribe un programa que te pida números cada vez más grandes
y que se guarden en una lista. Para acabar de escribir los números,
escribe un número que no sea mayor que el anterior. El programa termina
escribiendo la lista de números:

Escribe un número: 6
Escribe un número mayor que 6: 10
Escribe un número mayor que 10: 12
Escribe un número mayor que 12: 25
Escribe un número mayor que 25: 9
Autor:Nicolás Arena Ruiz
"""
Lista1=[]
indice=0
entrada=int(input("Dime un numero:"))
Lista1.append(entrada)
entrada=int(input("Dime otro numero (si quieres salir escribe un numero menor):"))
while(entrada>Lista1[indice]):
    Lista1.append(entrada)
    indice+=1
    entrada=int(input("Dime otro numero (si quieres salir escribe un numero menor):"))
print("Los numeros que has escrito son:", end=' ')
for i in Lista1:
    if i !=Lista1[-1]:
        print(i, end=', ')
    else:
        print(i)
