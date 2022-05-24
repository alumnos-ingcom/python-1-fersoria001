################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
### 8. Números primos
Escribir una función que indique con `True` si un numero
indicado es Primo.
"""

def es_primo(numero):
    """ Esta funcion utiliza un bucle while para determinar si un
     numero es primo, dependiendo de su cantidad de divisores
     exactos.
     Precondiciones: Ingresar un numero positivo.
     Postcondiciones: Se devuelve un valor booleano. True si es primo y
     False si no lo es.
     """
    if numero > 1:
        divisores = 0
        divisor = 2
        while divisor < numero and divisores ==0:
            resto = numero % divisor
            if resto == 0:
                divisores = divisores + 1
            divisor = divisor + 1
        if divisores == 0:
            primo = True
        else:
            primo = False
    else:
        primo = False
    return primo


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    num = int(input(" Enter a number: "))
    determine = es_primo(num)
    print(f" Your number is a prime number?: {determine}")

if __name__ == "__main__":
    principal()
