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


def test_ordenar_mayor_a_menor_uno():
    """ Esta funcion se encarga de testear ordenar de mayor a menor del
    ejercicio6.
    """
    uno = 357
    dos = -333
    tres = -1525
    grupo = (uno, dos, tres)
    tupla = tuple(sorted(grupo, reverse=True))
    descendente = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(descendente, tuple), "Se debe retornar una tupla"
    assert descendente == tupla,  "resultado incorrecto"


def test_ordenar_mayor_a_menor_dos():
    """ Esta funcion se encarga de testear ordenar de mayor a menor del
    ejercicio6.
    """
    uno = 3335
    dos = 357
    tres = 1534
    grupo = (uno, dos, tres)
    tupla = tuple(sorted(grupo, reverse=True))
    descendente = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(descendente, tuple), "Se debe retornar una tupla"
    assert descendente == tupla,  "resultado incorrecto"


def test_ordenar_mayor_a_menor_tres():
    """ Esta funcion se encarga de testear ordenar de mayor a menor del
    ejercicio6.
    """
    uno = -332
    dos = -152
    tres = -350
    grupo = (uno, dos, tres)
    tupla = tuple(sorted(grupo, reverse=True))
    descendente = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(descendente, tuple), "Se debe retornar una tupla"
    assert descendente == tupla,  "resultado incorrecto"


def test_ordenar_mayor_a_menor_cuatro():
    """ Esta funcion se encarga de testear ordenar de mayor a menor del
    ejercicio6.
    """
    uno = 1234
    dos = 357
    tres = 2552
    grupo = (uno, dos, tres)
    tupla = tuple(sorted(grupo, reverse=True))
    descendente = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(descendente, tuple), "Se debe retornar una tupla"
    assert descendente == tupla,  "resultado incorrecto"


def test_ordenar_mayor_a_menor_cinco():
    """ Esta funcion se encarga de testear ordenar de mayor a menor del
    ejercicio6.
    """
    uno = 1234
    dos = 3572
    tres = 5552
    grupo = (uno, dos, tres)
    tupla = tuple(sorted(grupo, reverse=True))
    descendente = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(descendente, tuple), "Se debe retornar una tupla"
    assert descendente == tupla,  "resultado incorrecto"


def test_ordenar_mayor_a_menor_cinco():
    """ Esta funcion se encarga de testear ordenar de mayor a menor del
    ejercicio6.
    """
    uno = 12
    dos = 35
    tres = 21
    grupo = (uno, dos, tres)
    tupla = tuple(sorted(grupo, reverse=True))
    descendente = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(descendente, tuple), "Se debe retornar una tupla"
    assert descendente == tupla,  "resultado incorrecto"



def test_ordenar_mayor_a_menor_tres():
    """ Esta funcion se encarga de testear ordenar de mayor a menor del
    ejercicio6.
    """
    uno = 1
    dos = 357
    tres = 333
    grupo = (uno, dos, tres)
    tupla = tuple(sorted(grupo, reverse=True))
    descendente = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(descendente, tuple), "Se debe retornar una tupla"
    assert descendente == tupla,  "resultado incorrecto"
    
def test_ordenar_menor_a_mayor_uno():
    """ Esta funcion se encarga de testear convertir a centigrados del
    ejercicio2.
    """
    uno = 258
    dos = 150
    tres = -357
    grupo = (uno, dos, tres)
    tupla = tuple(sorted(grupo))
    ascendente = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(ascendente, tuple), "Se debe retornar una tupla"
    assert ascendente == tupla, "Resultado incorrecto"


def test_ordenar_menor_a_mayor_dos():
    """ Esta funcion se encarga de testear convertir a centigrados del
    ejercicio2.
    """
    uno = 333
    dos = -1
    tres = 150
    grupo = (uno, dos, tres)
    tupla = tuple(sorted(grupo))
    ascendente = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(ascendente, tuple), "Se debe retornar una tupla"
    assert ascendente == tupla, "Resultado incorrecto"


def test_ordenar_menor_a_mayor_tres():
    """ Esta funcion se encarga de testear convertir a centigrados del
    ejercicio2.
    """
    uno = -333
    dos = 1
    tres = -357
    grupo = (uno, dos, tres)
    tupla = tuple(sorted(grupo))
    ascendente = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(ascendente, tuple), "Se debe retornar una tupla"
    assert ascendente == tupla, "Resultado incorrecto"


def test_ordenar_menor_a_mayor_cuatro():
    """ Esta funcion se encarga de testear convertir a centigrados del
    ejercicio2.
    """
    uno = 333
    dos = -1
    tres = 357
    grupo = (uno, dos, tres)
    tupla = tuple(sorted(grupo))
    ascendente = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(ascendente, tuple), "Se debe retornar una tupla"
    assert ascendente == tupla, "Resultado incorrecto"


def test_ordenar_menor_a_mayor_cinco():
    """ Esta funcion se encarga de testear convertir a centigrados del
    ejercicio2.
    """
    uno = -333
    dos = 150
    tres = 357
    grupo = (uno, dos, tres)
    tupla = tuple(sorted(grupo))
    ascendente = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(ascendente, tuple), "Se debe retornar una tupla"
    assert ascendente == tupla, "Resultado incorrecto"


def test_ordenar_menor_a_mayor_seis():
    """ Esta funcion se encarga de testear convertir a centigrados del
    ejercicio2.
    """
    uno = -333
    dos = 150
    tres = -150
    grupo = (uno, dos, tres)
    tupla = tuple(sorted(grupo))
    ascendente = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(ascendente, tuple), "Se debe retornar una tupla"
    assert ascendente == tupla, "Resultado incorrecto"
    