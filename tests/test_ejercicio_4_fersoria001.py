"""
Este archivo se encarga de ejecutar los test para las funciones contenidas
en el ejercicio4.
"""
################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio4 import suma_lenta


def test_suma_lenta_positivos():
    """ Esta funcion se encarga de testear la funcion suma lenta del
    ejercicio4 con numeros positivos
    """
    numero = 15
    otro_numero = 30
    suma = suma_lenta(numero,otro_numero)
    assert isinstance(suma, int), "se debe devolver un numero entero"
    assert suma > 30, "el resultado debe ser mayor a sus componentes"
    assert suma == 15+30, "el resultado debe ser la suma de ambos identificadores"


def test_suma_lenta_negativo_con_positivo():
    """ Esta funcion se encarga de testear la funcion suma lenta del
    ejercicio4 con numeros positivos
    """
    numero = -10
    otro_numero = 20
    suma = suma_lenta(numero,otro_numero)
    assert isinstance(suma, int), "se debe devolver un numero entero"
    assert suma == -10+20, "el resultado debe ser la suma de ambos identificadores"
    assert suma == 10, "el resultado aritmetico es diez"

def test_suma_lenta_positivo_con_negativo():
    """ Esta funcion se encarga de testear la funcion suma lenta del
    ejercicio4 con numeros positivos
    """
    numero = 15
    otro_numero = -15
    suma = suma_lenta(numero,otro_numero)
    assert isinstance(suma, int), "se debe devolver un numero entero"
    assert suma == -15+15, "el resultado debe ser la suma de ambos identificadores"
    assert suma == 0, "Este resultado debe ser cero"


def test_suma_lenta_negativos():
    """ Esta funcion se encarga de testear la funcion suma lenta del
    ejercicio4 con numeros positivos
    """
    numero = -15
    otro_numero = -15
    suma = suma_lenta(numero,otro_numero)
    assert isinstance(suma, int), "se debe devolver un numero entero"
    assert suma < 0, "el resultado debe ser negativo"
    assert suma == -15 +(-15), "el resultado debe ser la suma de ambos identificadores"
    assert suma == -30, "el resultado de esta cuenta debe ser -30"
