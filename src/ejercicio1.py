################
# Nombre - @fersoria001
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
### 1. Conversión de temperaturas
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados
y viceversa.
Escribir las funciones para convertir la temperatura en grados centigrados
en fahrenheit como un número decimal, utilice esta formula para calcular
los grados centígrados y retorne el  resultado obtenido. Y viceversa.
"""
def convertir_a_fahrenheit(centigrados):
    """
    Esta función se encarga de convertir grados centigrados a fahrenheit
    Precondiciones: "entrada" debe ser un numero entero o con decimales.
    Postcondiciones: "salida" devolvera un numero entero o con decimales.
    """
    fahrenheit = (centigrados * 1.8) + 32
    
    return fahrenheit


def convertir_a_centigrados(fahrenheit):
    """
    Esta función se encarga de convertir grados fahrenheit a centigrados
    Precondiciones: "entrada" debe ser un numero entero o con decimales.
    Postcondiciones: "salida" devolvera un numero entero o con decimales.
    """
    centigrados = (fahrenheit - 32) / (1.8)
    return centigrados


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    centigrados = float(
         input("Ingrese grados centigrados: "))
    fahrenheit = float(
        input("Ingrese grados fahrenheit: "))
    cen_a_far = convertir_a_fahrenheit(centigrados)
    far_a_cen = convertir_a_centigrados(fahrenheit)
    print(f' {centigrados} grados centigrados son {cen_a_far} grados fahrenheit')
    print(f' {fahrenheit} grados fahrenheit son {far_a_cen} grados celsius')



if __name__ == "__main__":
    principal()
