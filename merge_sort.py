# MERGE SORT - Dividir para Conquistar
def mergeSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)

    if fim - inicio > 1:
        meio = (fim + inicio) // 2

        mergeSort(lista, inicio, meio)
        mergeSort(lista, meio, fim)

        merge(lista, inicio, meio, fim)


def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]

    topo_left, topo_right = 0, 0

    for k in range(inicio, fim):
        if topo_left >= len(left):
            lista[k] = right[topo_right]
            topo_right += 1
        elif topo_right >= len(right):
            lista[k] = left[topo_left]
            topo_left += 1

        elif left[topo_left] < right[topo_right]:
            lista[k] = left[topo_left]
            topo_left += 1
        else:
            lista[k] = right[topo_right]
            topo_right += 1
