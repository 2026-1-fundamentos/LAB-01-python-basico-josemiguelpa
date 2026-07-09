"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    result = []
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            if not parts:
                continue
            letter = parts[0]
            col4_count = 0
            col5_count = 0
            if len(parts) >= 4 and parts[3].strip() != "":
                col4_count = len(parts[3].split(","))
            if len(parts) >= 5 and parts[4].strip() != "":
                col5_count = len(parts[4].split(","))
            result.append((letter, col4_count, col5_count))
    return result
