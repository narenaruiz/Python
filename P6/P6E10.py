"""10.-Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo de 0 a 10, el programa entenderá que no quieres introducir más notas de este alumno. Si no escribes el nombre, el programa entenderá que no quieres introducir más alumnos. Nota: La lista en la que se guardan los nombres y notas tiene esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]
Dame un nombre: Héctor Quiroga
Escribe una nota: 4
Escribe otra nota: 8.5
Escribe otra nota: 12
Dame otro nombre: Inés Valls
Escribe una nota: 7.5
Escribe otra nota: 1
Escribe otra nota: 2
Escribe otra nota: -5
Dame otro nombre:
Las notas de los alumnos son:
Héctor Quiroga: 4.0 - 8.5
Inés Valls: 7.5 - 1.0 - 2.0

Autor:Nicolás Arena Ruiz"""
ListaGeneral=[]
Lista=[]

Nombre=str(input("Dame tu nombre:"))
Lista.append(Nombre)
Notas=float(input("Escribe una nota(escribe un numero fuera del intervalo 0-10 para salir):"))
while(Nombre !=''):
    if Notas>=0 and Notas<=10:
        Lista.append(Notas)
        Notas=float(input("Escribe una nota(escribe un numero fuera del intervalo 0-10 para salir):"))
    else:
        ListaGeneral.append(Lista)
        Nombre=str(input("Dame tu nombre:"))
        if Nombre !='':
            Lista=[Nombre]
            Notas=float(input("Escribe una nota(escribe un numero fuera del intervalo 0-10 para salir):"))
            if Notas>=0 and Notas<=10:
                Lista.append(Notas)
                Notas=float(input("Escribe una nota(escribe un numero fuera del intervalo 0-10 para salir):"))
print(ListaGeneral)
