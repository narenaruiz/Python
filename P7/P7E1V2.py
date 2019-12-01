"""1.-Escribe un programa que pida un texto por pantalla, este texto
lo pase como parámetro a un procedimiento, y éste lo imprima primero
todo en minúsculas y luego todo en mayúsculas.
Autor: Nicolás Arena Ruiz
"""
def ConvertirMayMin(texto):
    print(texto.lower())
    print(texto.upper())

texto=str(input("Dime una frase:"))
ConvertirMayMin(texto)
