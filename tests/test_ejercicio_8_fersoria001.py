"""
Este archivo se encarga de ejecutar los test para las funciones contenidas
en el ejercicio8
"""
################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest
from src.ejercicio8 import es_primo


def test_es_primo():
    """ Esta funcion se encarga de testear la funcion que indica
    si un numero es primo o no en el ejercicio8
    """
    numero = 617
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert numero%2 != 0 and resultado is True, "Resultado incorrecto"
    assert numero%3 != 0 and resultado is True, "Resultado incorrecto"
    assert numero%5 != 0 and resultado is True, "Resultado incorrecto"
    assert numero%7 != 0 and resultado is True, "Resultado incorrecto"
    assert resultado is True, "Resultado incorrecto"


def test_es_primo_no():
    """ Esta funcion se encarga de testear la funcion que indica
    si un numero es primo o no en el ejercicio8 con valor False
    """
    numero = 36
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert numero%2 == 0 and resultado is False, "Resultado incorrecto"
    assert numero%3 == 0 and resultado is False, "Resultado incorrecto"
    assert resultado is False, "Resultado incorrecto"

def test_es_primo_negativo():
    """ Esta funcion se encarga de testear la funcion que indica
    si un numero negativo
    es primo o no en el ejercicio8
    """
    numero = -7
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is False, "Resultado incorrecto"
