primernumero=int(input("Dime un numero:"))
segundonumero=int(input("Dime otro numero:"))
if primernumero<segundonumero:
    for i in range(primernumero,segundonumero):
        if i%2==0:
            print("El numero %d es par" %(i))
        else:
            print("El numero %d es impar" %(i))
elif segundonumero<primernumero:
    for i in range(segundonumero,primernumero):
        if i%2==0:
            print("El numero %d es par" %(i))
        else:
            print("El numero %d es impar" %(i))
