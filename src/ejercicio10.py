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
    """ Esta funcion invierte el indice de la cadena,la limpia
    de caracteres especiales y resuelve si es igual al derecho
    que al revés.
     Precondiciones = Ingresar un identificador entre ""
     Postcondiciones = Se retorna un valor booleano.
     """
    texto = texto.replace(" ", "")
    texto = texto.lower()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace(",", "")
    texto = texto.replace(".", "")
    texto = texto.replace(":", "")
    auxiliar = texto
    al_reves = []
    for i in range(len(auxiliar)-1, -1, -1):
        car = auxiliar[i]
        al_reves.append(car)
    palabra = ''.join(al_reves)
    palindromo = palabra == auxiliar
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
