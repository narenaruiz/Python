"""7.-Escribe un programa que lea una frase, y la pase
como parámetro a un procedimiento. El procedimiento
contará el número de vocales (de cada una) que aparecen,
y lo imprimirá por pantalla."""

def Contar_Vocales(frase):
    VOCAL_A="aA"
    VOCAL_E="eE"
    VOCAL_I="iI"
    VOCAL_O="oO"
    VOCAL_U="uU"
    contador_a=0
    contador_e=0
    contador_i=0
    contador_o=0
    contador_u=0
    for i in range(frase):
        if vocal_a in frase:
            contador_a+=1
        elif vocal_b in frase:
            contador_b+=1
            

frase=str(input("Dime una frase"))
resultado_a, resultado_e, resultado_i, resultado_o, resultado_u=Contar_Vocales(frase)
print(f"El numero de vocales es: a={contador_a}, e={contador_e}, i={contador_i, o={contador_o}, u={contador_u}")
