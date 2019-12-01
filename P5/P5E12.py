"""12.-Escribe un programa que pida un número y escriba si primo o no
Dame un número: 123
El número 123 no es primo
Dame un número:127
El número 127 es primo
Autor: Nicolás Arena Ruiz
"""
numero=int(input("Dame un numero:"))
resultado=0
if numero==1:
    print("El numero 1 es primo.")
else:
    for i in range(1,numero+1):
        if numero%i==0:
            resultado+=1
    if resultado==2:
        print("El numero %d es primo." %(numero))
    else:
        print("El numero %d no es primo." %(numero))
