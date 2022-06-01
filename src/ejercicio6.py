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
    lista = [uno,dos,tres]
    if uno > dos and uno > tres:
        lista[0] = uno
        if dos > tres:
            lista[1] = dos
            lista [2] = tres
        else:
            lista[1] = tres
            lista [2] = dos
    else:
        if dos > tres:
            lista[0] = dos
            if uno > tres:
                lista[1] = uno
                lista[2] = tres
            else:
                lista[1] = tres
                lista[2] = uno
        else:
            lista[0] = tres
            if dos > uno:
                lista[1] = dos
                lista[2] = uno
            else:
                lista[1] = uno
                lista[2] = dos
    tupla = tuple(lista)
    return tupla

def ordenar_menor_a_mayor(uno,dos,tres):
    """ Esta funcion ordena tres numeros ingresados de menor a mayor
    Precondiciones: Ingresar tres numeros.
    Postcondiciones: Se devuelve una tupla ordenada de menor a mayor
    """
    lista = [1,2,3]
    if uno < dos and uno < tres:
        lista[0] = uno
        if dos < tres:
            lista[1] = dos
            lista [2] = tres
        else:
            lista[1] = tres
            lista [2] = dos
    else:
        if dos < tres:
            lista[0] = dos
            if uno < tres:
                lista[1] = uno
                lista[2] = tres
            else:
                lista[1] = tres
                lista[2] = uno
        else:
            lista[0] = tres
            if dos < uno:
                lista[1] = dos
                lista[2] = uno
            else:
                lista[1] = uno
                lista[2] = dos
    tupla = tuple(lista)
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
