"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    totals = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            if not parts:
                continue
            letter = parts[0]
            if len(parts) >= 5 and parts[4].strip() != "":
                items = parts[4].split(",")
                s = 0
                for it in items:
                    if not it:
                        continue
                    _, v = it.split(":")
                    s += int(v)
                totals[letter] = totals.get(letter, 0) + s
            else:
                totals[letter] = totals.get(letter, 0)
    return totals
