"""
Date: 2021-11-16
Authors: Jose Magdaleno Salazar Campos

File: T2_E1_test_list.py
Brief: Se crea una lista de strings definida y se realizan metodos de listas como append, pop, insert y ordenacion.
Score:
Version: A.B.1
Fixes:
"""


if __name__ == '__main__':
    lista = ["Hola", "Jose", "Python", "Capacitacion", "Redes", "Inteligencia"]
    print("Lista original")
    print(lista)
    print("\n")

    # Paso 1: metodo append
    lista.append("Neurona")
    print("Paso 1")
    print(lista)
    print("\n")

    # Paso 2: metodo insert
    lista.insert(1, "¿como estas?")
    print("Paso 2")
    print(lista)
    print("\n")

    # Paso 3: metodo pop
    lista.pop()
    print("Paso 3")
    print(lista)
    print("\n")

    # Paso 4: ordenar lista de A a Z
    lista.sort()
    print("Paso 4")
    print(lista)
    print("\n")

    # Paso 5: Ordenar lista de Z a A
    lista.sort(reverse=True)
    print("Paso 5")
    print(lista)
