"""
Este archivo se encarga de ejecutar los test para las funciones contenidas
en el ejercicio10
"""
################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest
from src.ejercicio10 import es_palindromo


def test_es_palindromo_si():
    """ Esta funcion se encarga de testear la funcion de comprobacion
    de palindromos con valor true
    """
    texto = "Dabale arroz a la Zorra el Abad"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "el resultado debe ser de tipo bool"
    assert resultado is True, "Resultado incorrecto2"


def test_es_palindromo_no():
    """ Esta funcion se encarga de testear la funcion de comprobacion
    de palindromos con valor False
    """
    texto = "aQuel Codigo esta mal"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "el resultado debe ser de tipo bool"
    assert resultado is False, "Resultado incorrecto"

def test_es_palindromo_tildes_puntuacion():
    """ Esta funcion se encarga de testear la funcion de comprobacion
    de palindromos con valor False
    """
    texto = "No subas, abusón"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "el resultado debe ser de tipo bool"
    assert resultado is True, "Resultado incorrecto"
