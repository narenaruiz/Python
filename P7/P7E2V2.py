"""2.-Escribe un programa que lea el nombre y los dos apellidos
de una persona (en tres cadenas de caracteres diferentes), los
pase como parámetros a una función, y ésta debe unirlos y devolver
una única cadena. La cadena final la imprimirá el programa por pantalla."""

def Unir_Nombre_Completo(nombre, primer_apellido, segundo_Apellido):
    union=(nombre+" "+primer_apellido+" "+segundo_apellido)
    return union

nombre=str(input("Dime un nombre:"))
primer_apellido=str(input("Dime el primer apellido:"))
segundo_apellido=str(input("Dime el segundo apellido:"))
print(Unir_Nombre_Completo(nombre, primer_apellido, segundo_apellido))

