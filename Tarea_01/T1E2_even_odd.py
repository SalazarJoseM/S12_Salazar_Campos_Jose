""""
Date:       2021-11-13
Authors:    José Magadaleno Salazar Campos
File:       T1E2_even_odd.py
Brief:      Programa que obtiene un numero entero o flotante y determina
            si par o impar
Score:
Version:    A.B.1
Fixes:
"""

if __name__ == '__main__':
    numero = float(input("Ingresa un numero "))
    if numero%2 == 0: print("El numero es par")
    else: print("El numero es impar")