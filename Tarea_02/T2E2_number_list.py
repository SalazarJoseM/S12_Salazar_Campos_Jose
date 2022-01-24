"""
Date:       2021-11-16
Authors:    Jose Magdaleno Salazar Campos
File:       T2_E2_number_list.py
Brief:      Se crea una lista de n numeros desde el teclado y se realizan acciones como ordenar, añadir, imprimir, etc.
Score:      80
Version:    1.1.1
Fixes:      - PEP8 recomienda no rebasar los 99 carácteres en una línea 
                de código, yo establecí en los requerimientos máximo 72
                carácteres (aplica para comentarios también)
            
            - En el paso 1 de este ejercicio, falto imprimir el tipo de 
                dato
"""


if __name__ == '__main__':
    lista_numeros = []

    n = int(input("¿Cuantos numeros desea ingresar? "))
    for i in range(n):
        numero = float(input("Ingresa el numero " + str(i+1) + " "))
        lista_numeros.append(numero)

    # Paso 1: Imprimir elementos
    print("\nElementos de la lista")
    for elemento in lista_numeros:
        print(elemento)

    # Paso 2: Cambiar todos los elementos a tipo int
    for i in range(len(lista_numeros)):
        lista_numeros[i] = int(lista_numeros[i])
    print("\n")
    print("Lista convertida a int: ")
    print(lista_numeros)

    # Paso 3: Imprimir un elemento indicado por el usuario
    indice = int(input("\nIngrese un indice de elemento de la lista para mostrar desde 0 hasta " + str(len(lista_numeros)-1) + " "))
    print(lista_numeros)
    print("El elemento seleccionado fue " + str(lista_numeros[indice]))

    # Paso 4: Ordenar elementos
    lista_numeros.sort()
    print("\nLista ordenada")
    print(lista_numeros)

    # Paso 5: Ordenar elementos en reversa
    lista_numeros.sort(reverse=True)
    print("\nLista ordenada en reversa")
    print(lista_numeros)
