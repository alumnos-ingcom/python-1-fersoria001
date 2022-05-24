################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
### 7. Transformación de un número
Escribir un programa que permita transformar un número solicitado
expresado en grados, minutos y segundos a segundos a segundos.
Y otra que haga el cambio en el sentido contrario, devolviendo
una `tuple`.
 Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
"""
def sexadecimal_a_decimal(horas,minutos,segundos):
    """ Esta funcion convierte horas,minutos y segundos a segundos.
    Precondiciones: Ingrese tres numeros enteros.
    Postcondiciones : Se devuelve un numero expresado en segundos
    """
    segundo = 0
    while horas > 0:
        horas = horas -1
        minutos = minutos + 60
    while minutos > 0:
        minutos = minutos -1
        segundo = segundo + 60
    segundos = segundos + segundo
    return segundos


def decimal_a_sexadecimal(numero):
    """ Esta funcion convierte segundos a horas minutos y segundos.
    devolviendo una tuple
    Precondiciones : Ingresar un numero entero.
    Postcondiciones : Devuelve una tupla de tres numeros.
    """
    minutos = 0
    horas = 0
    while numero > 59:
        minutos = minutos + 1
        numero = numero - 60
    while minutos > 59:
        horas = horas + 1
        minutos = minutos - 60
    return horas, "horas", minutos, "minutos", numero, 'segundos'

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del
    ejercicio(La entrada, la llamada al algoritmo y la salida)
    """
    horas = int(input("Ingrese las horas: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))
    numero = int(input("Ingrese un numero: "))
    convert = sexadecimal_a_decimal(horas,minutos,segundos)
    convierta = decimal_a_sexadecimal(numero)
    print(f" {horas} ° {minutos} ' {segundos} \" son {convert} segundos")
    print(f"{numero} segundos son {convierta} ")


if __name__ == "__main__":
    principal()
