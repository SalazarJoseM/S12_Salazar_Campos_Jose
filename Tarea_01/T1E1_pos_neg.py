""""
Date:       2021-11-13
Authors:    José Magadaleno Salazar Campos
File:       T1E1_pos_neg.py
Brief:      Programa que obtiene un numero entero o flotante y determina
            si es positivo, negativo o cero.
Score:      80
Version:    1.1.1
Fixes:      - Te hace falta la condición de __main__

            - PEP8 recomienda no usar múltiples declaraciones en una 
                sola línea de código
"""


if __name__ == '__main__':
    numero = float(input("Ingresa un numero "))
    if numero > 0:
        print("El numero es positivo")
    elif numero < 0:
        print("El numero es negativo")
    else:
        print("El numero es cero")
