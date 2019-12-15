"""13.-Escribe un programa que le pida al usuario si quiere
calcular si un número es primo con for o con while, por
tanto, habrán dos funciones que se caracterizan por hacer
ese mismo cálculo de una manera (con for y sin breaks), o de
otra (con while). Ambas funciones devolverá true (si es es primo) o
false (si no es primo). El programa principal informará del
resultado. Además, como mejora puedes calcular el tiempo
que tarda en encontrar la solución de una manera
u otra.Comentario: aprovecha el código que tienes ya creado
Autor: Nicolás Arena Ruiz
"""

def mostrarMenu():
    salir="N"
    while(salir=="N"):
        print("==================")
        print("=      Menú      =")
        print("==================")
        print("Que opcion deseas usar para calcular si el numero es primo?")
        print("1) Hacer calculo con for")
        print("2) Hacer calculo con while")
        print("3) Salír")
        print("==================")
        PreguntaMenu=input("Que opción deseas?")      
        if PreguntaMenu=="1":
            resultado = CalculoConFor(numero)
            return resultado
        elif PreguntaMenu=="2":
            resultado = CalculoConWhile(numero)
            return resultado
        elif PreguntaMenu=="3":
            salir=str(input("Estas seguro de que quires salir(Si-S/No-N):")).upper()
            if salir=="N":
                print("Ok")
            elif salir=="S":
                print("Gracias por utilizar nuestro juego")
        else:
            print("Error ese dato no es valido.")

"""Este creo que lo entiendo, pero al principio me ha costado
entenderlo un poco y he tenido que ver un poco algunos de internet y mis
compañeros. En un ejercicio de internet que he buscado para comparar
y entender bien tiene que 'if numero % i == 0:' tiene que devolver
false pero creo que esta mal. Despues de probar un poco he visto que
el 5 como ejemplo me dice que no es primo y si que lo es, es por lo que he
puesto yo de true? No lo entiendo."""
def CalculoConFor(numero):
    if numero < 1:
        return False
    elif numero==2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                """El porcentaje divide el primer numero por
                el segundo y te da el resto"""
                return True
            else:
                return False


"""Este me hace dudar, ya que aunque he buscado en internet y en los ejercicios
de mis compañeros para entenderlo bien todavia no creo entenderlo del
todo. Ademas lo de internet y algunos de mis compañeros no me gustaba
como lo ponian asi que lo he hecho así pero no se si esta bien."""
def CalculoConWhile(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        prueba = 2
        probando = "no"
        while(numero % prueba != 0 and probando == "no"):
            prueba += 1
            if numero % prueba == 0:
                probando = "si"
        return True

numero=int(input("Dime un numero:"))
resultado = mostrarMenu()
if resultado == True:
    print("El numero es primo.")
else:
    print("El numero no es primo.")
