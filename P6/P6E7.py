"""7.-Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los números introducidos supere el límite inicial. El programa termina escribiendo la lista de números.
Escribe límite: 50
Escribe un valor: 10
Escribe otro valor: 25
Escribe otro valor: 7
Escribe otro valor: 14
El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56
Autor"""

Lista=[]
Suma=0
Limite=int(input("Escribe un limite:"))
numero=int(input("Dime un valor:"))
Lista.append(numero)
Suma+=numero
while(Suma<=Limite):
    numero=int(input("Dime otro valor:"))
    Lista.append(numero)
    Suma+=numero
print("El limite a superar es %d. La lista creada es" %(Limite), end=' ')
for i in Lista:
    if i !=Lista[-1]:
        print(i, end=', ')
    else:
        print(i)
print("ya que la suma de estos numeros es", Suma)
