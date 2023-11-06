from concurrent.futures import ThreadPoolExecutor
import time

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr, parallel=False):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    if parallel:
        with ThreadPoolExecutor() as executor:
            left_half, right_half = executor.map(merge_sort, (left_half, right_half), (False, False))
    else:
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

    return merge(left_half, right_half)

# Teste a lista com Merge Sort Serial
start_time = time.time()
lista_desordenada = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
lista_ordenada_serial = merge_sort(lista_desordenada)
end_time = time.time()
print("Serial Merge Sort levou:", end_time - start_time, "segundos")

# Teste a lista com Merge Sort Paralelo
start_time = time.time()
lista_ordenada_parallel = merge_sort(lista_desordenada, parallel=True)
end_time = time.time()
print("Parelelo Merge Sort levou:", end_time - start_time, "segundos")


print("Lista ordenada (Serial):", lista_ordenada_serial)
print("Lista ordenada (Paralelo):", lista_ordenada_parallel)
