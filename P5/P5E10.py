"""Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura de un triángulo: 5
    *
   ***
  *****
 *******
*********
Autor: Nicolás Arena Ruiz
"""
alturatriangulo=int(input("Dime la altura del triangulo:"))
for i in range(alturatriangulo):
    print((alturatriangulo-i-1)*(' '), ((i*2)+1)*("*"))
    
