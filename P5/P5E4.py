primernumero=int(input("Escribe un numero:"))
resultado=1
for i in range(1,primernumero+1):
    resultado*=i
print("El factorial de %d es: %d" %(primernumero,resultado))
