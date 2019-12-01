"""4.-Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. El programa termina escribiendo los dos números tal y como se pide:
Escribe un número: 6
Escribe un número mayor que 6: 6
6 no es mayor que 6. Vuelve a introducir un número: 1
1 no es mayor que 6. Vuelve a introducir un número: 8
Los números que has escrito son 6 y 8
Autor:Nicolás Arena Ruiz
"""
entrada=float(input("Dime un numero:"))
segundonumero=float(input("Dime un numero mayor que %f:" % (entrada)))
while(entrada>=segundonumero):
    segundonumero=float(input("El numero %f no es mayor que %f, dime otro numero:"
                       % (segundonumero, entrada)))
print("Los numeros que has escrito son %f y %f" % (entrada, segundonumero))
