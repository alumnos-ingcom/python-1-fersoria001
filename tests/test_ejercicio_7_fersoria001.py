"""
Este archivo se encarga de ejecutar los test para las funciones contenidas
en el ejercicio7
"""
################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest
from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal



def test_sexadecimal_a_decimal():
    """ Esta funcion se encarga de testear convertir de sexadecimal
    a decimal desde funcion en el ejercicio1.
    """
    horas = 3
    minutos = 65
    segundos = 110
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado > (horas+minutos+segundos), "El resultado es erroneo"
    assert resultado > 14400, "El resultado es erroneo"



def test_decimal_a_sexadesimal():
    """ Esta funcion se encarga de testear si la funcion puede
    convertir correctamente de decimal a sexagesimal del
    ejercicio 7
    """
    segundos = 15335
    resultado = decimal_a_sexadecimal(segundos)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla"
    assert resultado[0] >= 4, "La equivalencia es igual o mayor a 4 horas"
    assert resultado == (4, 15, 35), "El resultado es incorrecto"
    