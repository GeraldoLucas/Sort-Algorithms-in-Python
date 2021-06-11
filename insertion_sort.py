# TERCEIRO: INSERTION SORT

"""
     Algoritmo de classificação de inserção
     É um algoritmo baseado em comparação no local.
     Para cada posição, troque o elemento atual à sua esquerda
     enquanto o elemento esquerdo é maior do que o elemento atual.
"""


# Insert Sort Não Otimizado
def insertionSort2(lista):
    compares2, assigns2 = 0, 0
    for i in range(0, len(lista)):
        if i > 0:
            compares2 += 1

        while i > 0:
            if lista[i - 1] > lista[i]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
            assigns2 += 1
            i = i - 1


# 41 861
# 419 87990
# 998 498501


# Insert Sort Otimizado em Complexidade e Performace
def insertionSort(lista):
    compares, assigns = 0, 0
    for i in range(1, len(lista)):
        if i > 0:
            compares += 1
        k = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > k:
            lista[j + 1] = lista[j]
            assigns += 1
            j = j - 1
        lista[j + 1] = k

# 41 376
# 419 44177
# 998 250041