import contextlib
import random
import time

from selection_sort import selectionSort
from bubble_sort import bubbleSort
from insertion_sort import insertionSort,insertionSort2
from merge_sort import mergeSort


@contextlib.contextmanager
def timeit(name):
    start = time.time()
    yield
    end = time.time()
    took = end - start
    print(f"O {name} levou {took:.4f}s.")


def nearly_array(size):
    array = [i for i in range(0, size + 1)]

    for i in range(10, size, 10):
        array[i], array[i - 1] = array[i - 1], array[i]

    return array


if __name__ == "__main__":
    num_items = 1000

    array = [random.randint(0, num_items) for i in range(num_items)]
    random.shuffle(array)

    nearly_sorted = nearly_array(num_items)
    reversed_array = sorted(array, reverse=True)
    sorted_array = sorted(array)

    algorithms = {
        'Selection_sort': selectionSort,
        'Bubble_sort': bubbleSort,
        'Insertion_sort': insertionSort,
        'Insertion_sort_ruim': insertionSort2,
        'Merge_sort': mergeSort,
    }

    print("\n Lista Randomizada")
    print('=-=-' * 6 + '=')
    for name, sort in algorithms.items():
        copy_array = list(array)

        with timeit(name):
            sort(copy_array)

        assert copy_array == sorted(array)

    print("\n \n Lista quase Orquenada")
    print('=-=-' * 6 + '=')
    for name, sort in algorithms.items():
        copy_array = list(nearly_sorted)

        with timeit(name):
            sort(copy_array)

        assert copy_array == sorted(nearly_sorted)

    print("\n \n Lista ao contrário")
    print('=-=-' * 6 + "=")
    for name, sort in algorithms.items():
        copy_array = list(reversed_array)

        with timeit(name):
            sort(copy_array)

        assert copy_array == sorted(reversed_array)