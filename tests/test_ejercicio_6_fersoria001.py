"""
Este archivo se encarga de ejecutar los test para las funciones contenidas
en el ejercicio6
"""
################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest
from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor


def test_ordenar_mayor_a_menor():
    """ Esta funcion se encarga de testear ordenar de mayor a menor del
    ejercicio6.
    """
    uno = 357
    dos = 333
    tres = 1
    descendente = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(descendente, tuple), "Se debe retornar una tupla"
    assert descendente[0] > descendente[1] > descendente[2], "Deben estar ordenados"
    assert descendente[0] > descendente[2], "Deben estar ordenados"

def test_ordenar_menor_a_mayor():
    """ Esta funcion se encarga de testear convertir a centigrados del
    ejercicio2.
    """
    uno = 333
    dos = 1
    tres = 357
    ascendente = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(ascendente, tuple), "Se debe retornar una tupla"
    assert ascendente[0] < ascendente[1] < ascendente[2], "Deben estar ordenados"
    assert ascendente[0] < ascendente[2], "Deben estar ordenados"
    