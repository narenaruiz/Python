"""3.-Escribe un programa que lea una frase, y la pase
como parámetro a un procedimiento, y éste debe mostrar
la frase con un carácter en cada línea.
Autor:Nicolás Arena Ruiz
"""
def Separacion_De_Linea(frase):
    for i in frase:
        print(i)

frase=str(input("Dime una frase:"))
Separacion_De_Linea(frase)
