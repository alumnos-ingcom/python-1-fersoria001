"""
Este archivo se encarga de ejecutar los test para las funciones contenidas
en el ejercicio2 que debe indicar con palabras el signo de un numero
"""
################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio2 import signo as signos


def test_signo_positivo():
    """ Esta funcion se encarga de testear la funcion signo del
    ejercicio2 con un valor positivo.
    """
    numero_pos = 10
    signo_pos = signos(numero_pos)
    assert isinstance(signo_pos, int), "se debe devolver un valor int"
    assert signo_pos == 1, "el numero es positivo"



def test_signo_negativo():
    """ Esta funcion se encarga de testear la funcion signo del
    ejercicio2 con un valor negativo.
    """
    numero_neg = -21.53
    signo_neg = signos(numero_neg)
    assert isinstance(signo_neg, int), "se debe devolver un valor int"
    assert signo_neg == -1, "el numero es negativo"


def test_signo_cero():
    """ Esta funcion se encarga de testear la funcion signo del
    ejercicio2 con un igual a cero.
    """
    numero_cero = 0
    signo_cero = signos(numero_cero)
    assert isinstance(signo_cero, int), "se debe devolver un valor int"
    assert signo_cero == 0, "el numero ingresado es cero"
