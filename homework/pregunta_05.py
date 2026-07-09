"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    stats = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                key = parts[0]
                val = int(parts[1])
                if key in stats:
                    cur_min, cur_max = stats[key]
                    stats[key] = (min(cur_min, val), max(cur_max, val))
                else:
                    stats[key] = (val, val)
    # convert to (letter, max, min) per expected order (max, min) but tests expect (letter, max, min?)
    # Tests expect (letter, max, min) where order shows max then min
    result = []
    for k in sorted(stats.keys()):
        cur_min, cur_max = stats[k]
        result.append((k, cur_max, cur_min))
    return result
