"""
Este archivo se encarga de ejecutar los test para las funciones contenidas
en el ejercicio3.
"""
################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest
from src.ejercicio3 import comparacion_de_numeros


def test_comparacion_de_numeros_primero_mayor_a_segundo():
    """ Esta funcion se encarga de testear la funcion comparacion de numeros del
    ejercicio3 cuando el primero es mayor al segundo.
    """
    numero = 15
    otro_numero = -15.5
    comparacion = comparacion_de_numeros(numero,otro_numero)
    assert isinstance(comparacion, int), "se debe devolver un valor entero"
    assert -1 <= comparacion >= 1, "se debe devolver un valor entre -1 y 1"
    assert comparacion == 1, "1 indica que el primer numero es mayor que el segundo"


def test_comparacion_de_numeros_primero_menor_a_segundo():
    """ Esta funcion se encarga de testear la funcion comparacion de numeros del
    ejercicio3 con el segundo mayor al primero.
    """
    numero = -33
    otro_numero = 52.3
    comparacion = comparacion_de_numeros(numero,otro_numero)
    assert isinstance(comparacion, int), "se debe devolver un valor entero"
    assert -1 <= comparacion <= 1, "se debe devolver un valor entre -1 y 1"
    assert comparacion == -1, "-1 indica que el segundo numero es mayor que el primero"


def test_comparacion_de_numeros_iguales():
    """ Esta funcion se encarga de testear la funcion comparacion de numeros del
    ejercicio3 cuando estos son iguales.
    """
    numero = -8
    otro_numero = -8
    comparacion = comparacion_de_numeros(numero,otro_numero)
    assert isinstance(comparacion, int), "se debe devolver un valor entero"
    assert -1 <= comparacion < 1, "se debe devolver un valor entre -1 y 1"
    assert comparacion == 0, "0 indica que son iguales"
