"""
Date:       2021-11-13
Authors:    José Magadaleno Salazar Campos
File:       T1E3_birthday.py
Brief:      Programa que obtiene una fecha de cumpleaños y lo imprime en pantalla   # PEP8
Score:      80
Version:    1.1.1
Fixes:      - PEP8 recomienda no rebasar los 99 carácteres en una línea 
                de código, yo establecí en los requerimientos máximo 72
                carácteres
                
            - PEP8 recomienda añadir un espacio en blanco después del
                carácter de coma ','
                
            - PEP8 recomienda dejar una línea en blanco al final del
                código
                
            - 10 puntos por no usar f-strings, sino format
"""

if __name__ == '__main__':
    dia = int(input("Ingresa tu dia de cumpleanios "))
    mes = int(input("Ingresa tu mes de cumpleanios en numero "))
    year = int(input("Ingresa tu anio de cumpleanios "))
    # No se uso f-strings para la impresión
    print("Year: {} - Month: {} - Day: {}".format(year,mes,dia))    # PEP8
