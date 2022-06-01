################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
### 4. Suma lenta
Escribir una funcion que haga la suma entre dos numeros enteros sin
hacer la operacion de manera directa. Esto quiere decir que para
hacer la suma entre 4 y 3, las operaciones resultante deberán
ser 4+1+1+1.La funcion debe ser capaz de sumar cualquier
numero entero positivo y negativo.
"""
def suma_lenta(numero, otro_numero):
    """
    Esta función se encarga de sumar a un numero , otro numero de 1 en
    1.
    Precondiciones = Ingresar dos numeros enteros independientes.
    Postcondiciones = Se retornara un numero entero, que es
    igual a la suma de ambos numeros ingresados.
    """
    if otro_numero >= 0:
        while otro_numero > 0:
            numero = numero + 1
            otro_numero = otro_numero - 1
    elif otro_numero <= 0:
        while otro_numero < 0:
            numero = numero - 1
            otro_numero = otro_numero + 1
    return numero


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del
    ejercicio(La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un numero: "))
    otro_numero = int(input("Ingrese otro numero: "))
    sumar = suma_lenta(numero,otro_numero)
    print(f" {numero} sumado a {otro_numero} es igual a {sumar}")


if __name__ == "__main__":
    principal()
