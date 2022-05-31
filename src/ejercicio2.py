################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
### 2. Números positivos y negativos

Escribir una función que reciba un número e indique si el mismo es
positivo, negativo o cero utilizando sumas y restas.
"""
def signo(numero):
    """ Esta funcion se encarga de reconocer el signo de un numero
    mediante sumas y restas.
    Precondiciones = ingresar un numero
    Postcondiciones = se devuelve -1 si es negativo, 1 si es positivo
    y 0 si es cero
    """
    suma = numero + numero
    resta = numero - numero
    if suma > numero:
        signos = 1
    elif resta > numero:
        signos = -1
    else:
        signos = 0
    return signos


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del
    ejercicio (La entrada, la llamada al algoritmo y la salida)
    """
    numeros = int(input("Ingrese un numero: "))
    sign = signo(numeros)
    print(f" El numero {numeros} es {sign}")



if __name__ == "__main__":
    principal()
