# PRIMEIRO: SELECTION SORT
"""
     Algoritmo de classificação de seleção simples.
     O algoritmo divide a entrada em duas partes: a sublista de itens
     já classificado, que é construído da esquerda para a direita na frente (esquerda)
     da lista, e a sublista de itens restantes a serem classificados que ocupam o
     resto da lista.
     O algoritmo prossegue encontrando o menor elemento na sublista não classificada,
     trocando-o com o elemento não classificado mais à esquerda.
"""


def selectionSort(lista):
    n = len(lista)
    for i in range(0, n):
        min_index = i
        for e in range(i + 1, n):
            if lista[e] < lista[min_index]:
                min_index = e

        lista[i], lista[min_index] = lista[min_index], lista[i]


# 1 + (n)*[3 + x] ---> 1 + 3n + nx