# Ejercicio 1: par o impar (if / else)
# Autor: Compañero

try:

    numero = int(input("Introduce un número entero: "))

    if numero % 2 == 0:
	    print(numero, "es par")
    else:
	    print(numero, "es impar")
except:
    print("La entrada no es valida")
