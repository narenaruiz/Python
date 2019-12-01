"""6.-Escribe un programa que pida primero dos números (máximo y mínimo)
y que después te pida números intermedios. Para terminar de escribir
números, escribe un número que no esté comprendido entre los dos
valores iniciales. El programa termina escribiendo la lista de números.

Escribe un número: 6
Escribe un número mayor que 6: 4
4 no es mayor que 6. Vuelve a probar: 50
Escribe un número entre 6 y 50: 45
Escribe otro número entre 6 y 50: 13
Escribe otro número entre 6 y 50: 4
Los números situados entre 6 y 50 que has escrito son: 45, 13 

Autor:Nicolás Arena Ruiz
"""
Lista=[]
maximo=int(input("Dime un numero para que sea el maximo:"))
Lista.append(maximo)
minimo=int(input("Dime un numero para que sea el minimo:"))
Lista.append(minimo)
numerointermedio=int(input("Dime un numero entre %d y %d (di un numero que no este en medio para salir):" %(maximo,minimo)))
while(numerointermedio>minimo and numerointermedio<maximo):
    Lista.append(numerointermedio)
    numerointermedio=int(input("Dime un numero entre %d y %d (di un numero que no este en medio para salir):" %(maximo,minimo)))
print("Los numeros situados entre %d y %d que has escrito son:" %(maximo,minimo),end=' ')
for i in Lista:
    if i !=Lista[-1]:
        print(i, end=', ')
    else:
        print(i)
