Pregunta=input("Para calcular el area del cuadrado pulsa C y para el triangulo T:")
if Pregunta !="C" and Pregunta !="T":
    print("La tecla es incorrecta")
if Pregunta=="C":
    BaseC=float(input("Dime la base:"))
    AlturaC=float(input("Dime la altura"))
    AreaC=BaseC*AlturaC
    print("El area de cuadrado es", AreaC)
elif Pregunta=="T":
    BaseT=float(input("Dime la base"))
    AlturaT=float(input("Dime la altura"))
    AreaT=(BaseT*AlturaT)/2
    print("El area de cuadrado es", AreaT)
