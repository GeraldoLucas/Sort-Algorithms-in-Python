# SEGUNDO: BUBBLE SORT
"""
Algoritmo de classificação em bolha
Melhor caso: - Listas quase ordenadas
Uso prático: - Não
Criado: ~ 1950
Também conhecido por: Sinking Sort, Exchange Sort
"""


def bubbleSort(lista):
    for j in range(0, len(lista) - 1):
        for i in range(0, len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

