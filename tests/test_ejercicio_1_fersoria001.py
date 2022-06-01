"""
Este archivo se encarga de ejecutar los test para las funciones contenidas
en el ejercicio1
"""
################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest
from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados


def test_convertir_a_fahrenheit():
    """ Esta funcion se encarga de testear convertir a fahrenheit del
    ejercicio1.
    """
    centigrados = 100
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "el resultado debe ser de tipo float"
    assert resultado > centigrados, "1 centigrado equivale a 33.8 fahrenheit"
    assert resultado == 212.0


def test_convertir_a_centigrados():
    """ Esta funcion se encarga de testear convertir a centigrados del
    ejercicio2.
    """
    fahrenheit = 50
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "el resultado debe ser tipo float"
    assert resultado < fahrenheit, "1 fahrenheit equivale a -17,22 centigrados"
    assert resultado == 10, "el resultado no es correcto"
