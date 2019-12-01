"""5.-Escribe un programa que te pida una frase y una
vocal, y pase estos datos como parámetro a una función
que se encargará de cambiar todas las vocales de la
frase por la vocal seleccionada. Devolverá la función
la frase modificada, y el programa principal la imprimirá:
Autor:Nicolás Arena Ruiz"""

def Frase_Editada(frase, vocal):
    vocales="aeiouAEIOU"
    frase_modificada=""
    for i in range(len(frase)):
        if frase[i] in vocales:
            frase_modificada+=vocal
        else:
            frase_modificada+=frase[i]
    return frase_modificada

frase=str(input("Dime una frase:"))
vocal=str(input("Dime una vocal para sustituir las otras:"))
print("La frase modificada es:",Frase_Editada(frase, vocal))
