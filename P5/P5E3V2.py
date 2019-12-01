primernumero=int(input("Escribe un numero:"))
segundonumero=int(input("Escribe otro numero distinto:"))
if primernumero<segundonumero:
    for i in range(segundonumero-primernumero):
        numerosintermedios=primernumero+1
    resultado=(primernumero+segundonumero+numerosintermedios)
    print("La suma de %d hasta %d es: %d" %(primernumero,segundonumero,resultado))
elif segundonumero<primernumero:
    for i in range(segundonumero,primernumero):
        numerosintermedios=segundonumero+1
    resultado=(primernumero+segundonumero+numerosintermedios)
    print("La suma de %d hasta %d es: %d" %(segundonumero,primernumero,resultado))
else:
    print("Error los numeros son iguales")
