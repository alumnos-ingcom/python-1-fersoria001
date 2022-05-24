################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 10. Palíndromo
Escribir una función que indique con True si una palabra o frase
ingresada se trata de un palindromo.Palíndromo, es si se lee igual
de derecha a izquierda que de izquierda a derecha.
"""


def es_palindromo(texto):
    """ Esta funcion invierte el indice de la cadena y resuelve si
     es igual al derecho que al revés.
     Precondiciones = Ingresar un identificador entre ""
     Postcondiciones = Se retorna un valor booleano.
     """
    if texto == texto[::-1]:
        palindromo = True
    else:
        palindromo = False
    return palindromo

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del
    ejercicio(La entrada, la llamada al algoritmo y la salida)
    """
    entrada = input(" Ingrese una frase o texto: ")
    comprobacion = es_palindromo(entrada)
    print(f"la frase {entrada} es un palindromo : {comprobacion}")


if __name__ == "__main__":
    principal()
