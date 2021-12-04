""""
Date:       2021-11-13
Authors:    José Magadaleno Salazar Campos
File:       T1E2_even_odd.py
Brief:      Programa que obtiene un numero entero o flotante y determina
            si par o impar
Score:      80
Version:    1.1.1
Fixes:      - PEP8 recomienda añadir espacios en blanco alrededor de
                los operadores
                
            - PEP8 recomienda no hacer múltiples declaraciones en una 
                sola línea de código      
                
            - PEP8 recomienda dejar una línea en blanco al final del
                código
"""

if __name__ == '__main__':
    numero = float(input("Ingresa un numero "))
    # Seria bueno validar e indicar cuando el número sea cero
    if numero%2 == 0: print("El numero es par")     # PEP8  PEP8
    else: print("El numero es impar")               # PEP8  PEP8
