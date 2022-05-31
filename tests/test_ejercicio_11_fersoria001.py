"""
Este archivo se encarga de ejecutar los test para las funciones contenidas
en el ejercicio11
"""
################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest
from src.ejercicio11 import es_multiplo


def test_es_multiplo_si():
    """ Esta funcion se encarga de testear la funcion de comprobacion
    de multiplos con valor True
    """
    numero = 26
    otro_numero = 2
    resultado = 26%2 == 0 == es_multiplo(numero,otro_numero)
    assert isinstance(resultado, bool), "el resultado debe ser de tipo bool"
    assert resultado is True, "Resultado incorrecto"


def test_es_multiplo_no():
    """ Esta funcion se encarga de testear la funcion de comprobacion
    de multiplos con valor False
    """
    numero = 23
    otro_numero = 2
    resultado = 26%3 == 0 == es_multiplo(numero,otro_numero)
    assert isinstance(resultado, bool), "el resultado debe ser de tipo bool"
    assert resultado is False, "Resultado incorrecto"
