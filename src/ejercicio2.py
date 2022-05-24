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
    Postcondiciones = se devuelve el signo de el numero ingresado
    """
    suma = numero + numero
    resta = numero - numero
    if suma > numero:
        signos = "positivo"
    elif resta > numero:
        signos = "es negativo"
    else:
        signos = "es cero"
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
