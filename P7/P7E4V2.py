"""4.-Escribe un programa que pida una frase, y le pase
como parámetro a una función dicha frase. La función
debe sustituir todos los espacios en blanco de una frase
por un asterisco, y devolver el resultado para que el
programa principal la imprima por pantalla.
Autor:Nicolás Arena Ruiz
"""
def Convierte_Espacios(frase):
    FraseCambiada=""
    for i in range (len(frase)):
        if frase[i]==" ":
            FraseCambiada+="*"
        else:
            FraseCambiada+=frase[i]
    return FraseCambiada

frase=str(input("Dime una frase:"))
resultado=Convierte_Espacios(frase)
print(resultado)

