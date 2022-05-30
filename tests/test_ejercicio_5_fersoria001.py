"""
Este archivo se encarga de ejecutar los test para las funciones contenidas
en el ejercicio5.
"""
################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio5 import division_lenta


def test_division_lenta_positivos():
    """ Esta funcion se encarga de testear la funcion division lenta del
    ejercicio5 con numeros positivos
    """
    dividendo = 15
    divisor = 2
    division = division_lenta(dividendo,divisor)
    assert isinstance(division, tuple), "Debe retornar una tupla con cociente y resto"
    assert division[0] == 15//2, "El resultado no es correcto"
    assert division[1] == 15%2, "El resultado no es correcto"
    assert division == (7,1), "El resultado no es correcto"