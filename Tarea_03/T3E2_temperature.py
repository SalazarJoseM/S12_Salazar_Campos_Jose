"""
Date:       2021-11-21
Authors:    Jose Magdaleno Salazar Campos
File:       T3E2_temperature.py
Brief:      Se tienen dos funciones que convierten temperatura de grados celsius a fahrenheit y viceversa.
Score:      80 (75)
Version:    1.1.1
Fixes:      - [25] PEP8 recomienda no rebasar los 99 carácteres en una
                línea de código, yo establecí en los requerimientos
                máximo 72 carácteres (aplica para comentarios también)
"""


def celsius_a_fahrenheit():
    grados_celsius_1 = float(input("Ingresa la temperatura en grados celsius: "))
    grados_fahrenheit_1 = grados_celsius_1 * 1.8 + 32
    resultado_1 = "El resultado en grados fahrenheit es " + str(round(grados_fahrenheit_1, 2))
    return resultado_1


def fahrenheit_a_celsius():
    grados_fahrenheit_2 = float(input("Ingresa la temperatura en grados fahrenheit: "))
    grados_celsius_2 = (grados_fahrenheit_2 - 32) / 1.8
    resultado_2 = "El resultado en grados celsius es " + str(round(grados_celsius_2, 2))
    return resultado_2


if __name__ == '__main__':
    print(celsius_a_fahrenheit())
    print('\n')
    print(fahrenheit_a_celsius())
