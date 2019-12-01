A=float(input("Dime el primer numero para comparar:"))
B=float(input("Dime el segundo numero:"))
C=float(input("Dime el tercer numero"))
D=float(input("Dime el cuarto numero"))
E=float(input("Dime el quinto numero"))
if A>B>C>D>E:
    print("Decreciente")
elif E>D>C>B>A:
    print("Creciente")
else:
    print("Desordenado")
