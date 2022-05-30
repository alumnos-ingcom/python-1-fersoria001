"""
Este archivo se encarga de ejecutar los test para las funciones contenidas
en el ejercicio2 que debe indicar con palabras el signo de un numero
"""
################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio2 import signo


def test_signo_positivo():
    """ Esta funcion se encarga de testear la funcion signo del
    ejercicio2 con un valor positivo.
    """
    numero_pos = 10
    signo_pos = signo(numero_pos)
    assert isinstance(signo_pos, str), "se debe devolver una cadena de texto"
    assert signo_pos == "positivo", "el numero es positivo"



def test_signo_negativo():
    """ Esta funcion se encarga de testear la funcion signo del
    ejercicio2 con un valor negativo.
    """
    numero_neg = -1.5
    signo_neg = signo(numero_neg)
    assert isinstance(signo_neg, str), "se debe devolver una cadena de texto"
    assert signo_neg == "es negativo", "el numero es negativo"


def test_signo_cero():
    """ Esta funcion se encarga de testear la funcion signo del
    ejercicio2 con un igual a cero.
    """
    numero_cero = 0
    signo_cero = signo(numero_cero)
    assert isinstance(signo_cero, str), "se debe devolver una cadena de texto"
    assert signo_cero == "es cero", "el numero ingresado es cero"
