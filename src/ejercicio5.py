################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
### 5. Divisiones
Escribir una función que mediante restas sucesivas, obtenga el valor del
cociente y resto de dos números enteros.
"""
def division_lenta(dividendo,divisor):
    """
    Esta funcion se encarga de realizar una división entera restando el
    divisor al dividendo hasta que dividendo > divisor. También
    nos devolverá el resto de la operacion.
    Precondiciones: Tanto dividendo como divisor, deben ser numeros Reales.
    Postcondicion : La salida devuelve una tupla formada por el cociente y el resto.
    """
    auxiliar_dos = divisor
    auxiliar_uno = dividendo
    cociente = 0
    if divisor < 0:
        auxiliar_dos = divisor
        divisor = (divisor) * -1
    if dividendo < 0:
        auxiliar_uno = dividendo
        dividendo = dividendo * -1
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente = cociente + 1
    if auxiliar_uno > 0 and auxiliar_dos < 0:
        cambio_signo = (cociente *-1), (dividendo *-1)
        dividendo = (auxiliar_dos) - (cambio_signo[1])
        cociente = (cambio_signo[0]) + -1
    elif auxiliar_uno < 0 and auxiliar_dos > 0:
        cambio_signo = (cociente *-1), (dividendo *-1)
        dividendo = (auxiliar_dos) + (cambio_signo[1])
        cociente = (cambio_signo[0]) + -1
    elif auxiliar_dos < 0 and auxiliar_uno < 0:
        dividendo = dividendo * -1
    return(cociente,dividendo)


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    dividir = division_lenta(dividendo,divisor)
    print(f"{dividendo} entre {divisor} es {dividir} cociente,resto")


if __name__ == "__main__":
    principal()
