################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 9. Factores Primos
Escribir una función que retorne una `tuple` con factores primos
de un numero entero positivo.
"""


def factores_primos(numero):
    """ Esta funcion busca los numeros primos que son factores
    de un numero dado.
    Precondiciones : Se debe ingresar un numero entero positivo.
    Postcondiciones: Se devuelve una tupla con todos los factores
    primos del numero.
    """
    contador = 2
    factores = []
    while numero > 1:
        if numero % contador == 0:
            factores.append(contador)
            numero = numero / contador
        else:
            contador = contador + 1
    return tuple(factores)


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    num = int(input("Ingrese un numero entero mayor a cero: "))
    factorizar = factores_primos(num)
    print(f" El numero {num} puede factorizarse en {factorizar} nros primos")

if __name__ == "__main__":
    principal()
