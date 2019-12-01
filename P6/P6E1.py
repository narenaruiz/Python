"""1.-Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter. El programa termina escribiendo la lista de palabras.
Escribe una palabra: viaje
Escribe más palabras: aventura
Escribe más palabras: cómic
Escribe más palabras:
Las palabras que has Escrito son [ 'viaje', 'aventura', 'cómic']
Autor: Nicolás Arena Ruiz
"""
palabras=[]

entrada=input("Pasame una palabra:")
while(entrada!=""):
    palabras.append(entrada)
    entrada=input("Pasame una palabra:")

print("la lista de palabras es",palabras)

"""el append añade al final de la lista el valor que le digas y el += sirve para concatenar listas (unir las listas)"""
