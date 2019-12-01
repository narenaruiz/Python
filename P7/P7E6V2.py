"""6.-Escribe un programa que lea el nombre de una
persona y un carácter, le pase estos datos a una
función que comprobará si dicho carácter está en
su nombre. El resultado de dicha función lo imprimirá
el programa principal por pantalla.
Autor:Nicolás Arena Ruiz
"""

def Comprobacion(nombre, caracter):
    if caracter in nombre:
            comprobacion_completa="El caracter sí que esta dentro del nombre"
    else:
            comprobacion_completa="El caracter no esta dentro del nombre"
    return comprobacion_completa

nombre=str(input("Dime un nombre:"))
caracter=str(input("Dime un caracter para comprobar:"))
print(Comprobacion(nombre, caracter))
