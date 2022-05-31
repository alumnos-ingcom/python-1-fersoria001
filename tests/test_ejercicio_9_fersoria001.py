"""
Este archivo se encarga de ejecutar los test para las funciones contenidas
en el ejercicio9
"""
################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest
from src.ejercicio9 import factores_primos


def test_factores_primos():
    """ Esta funcion se encarga de testear la funcion que descompone
    un numero en sus factores primos
    """
    numero = 36
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla"
    assert resultado[0] == 2,"El numero es divisible por dos"
    assert resultado[3]%2 != 0, "El factor no es primo"
    assert resultado == (2, 2, 3, 3), "Resultado incorrecto"
    
    
