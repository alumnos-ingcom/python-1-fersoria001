################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
### 6. Ordenar 3 valores
Escribir una función que a partir de tres variables de tipo entero
retorne una tupla con dichos valores ordenados de
menor a mayor. Y Viceversa
"""

def ordenar_mayor_a_menor(uno,dos,tres):
    """ Esta función ordena de mayor a menor tres valores dados.
    Precondiciones: Deben ingresarse tres numeros en cualquier orden.
    Postcondiciones: Se devuelve una tupla con los valores ordenados de mayor
    a menor.
    """
    if uno > dos > tres:
        tupla = (uno, dos, tres)
    elif uno > tres > dos:
        tupla = (uno, tres, dos)
    elif dos > uno > tres:
        tupla = (dos, uno, tres)
    elif dos > tres > uno:
        tupla = (dos, tres, uno)
    elif tres > uno > dos:
        tupla = (tres, uno, dos)
    else:
        tupla = (tres, dos, uno)
    return tupla


def ordenar_menor_a_mayor(uno,dos,tres):
    """ Esta funcion ordena tres numeros ingresados de menor a mayor
    Precondiciones: Ingresar tres numeros.
    Postcondiciones: Se devuelve una tupla ordenada de menor a mayor
    """
    if  uno < dos < tres:
        tupla = (uno, dos, tres)
    elif uno < tres < dos:
        tupla = (uno, tres, dos)
    elif dos < uno < tres:
        tupla = (dos, uno, tres)
    elif dos < tres < uno:
        tupla = (dos, tres, uno)
    elif tres < uno < dos:
        tupla = (tres, uno, dos)
    else:
        tupla = (tres, dos, uno)
    return tupla


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    primer = int(input("Ingrese el primer numero"))
    segundo = int(input("Ingrese el segundo numero"))
    tercer = int(input("Ingrese el tercer numero"))
    asc = ordenar_mayor_a_menor(primer,segundo,tercer)
    desc = ordenar_menor_a_mayor(segundo,tercer,primer)
    print( f" Nros. ordenados ascendente{asc} y , descente {desc}")

if __name__ == "__main__":
    principal()
