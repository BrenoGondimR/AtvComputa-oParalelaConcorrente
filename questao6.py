from concurrent.futures import ThreadPoolExecutor
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Paraleliza a ordenação em chunks do array
def bubble_sort_parallel(arr, chunk_size):
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
    sorted_chunks = []
    with ThreadPoolExecutor() as executor:
        sorted_chunks = list(executor.map(bubble_sort, chunks))

    sorted_arr = []
    for chunk in sorted_chunks:
        sorted_arr = merge(sorted_arr, chunk)

    return sorted_arr

# Mescla dois arrays ordenados
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


# Teste o Bubble Sort Paralelo
arr = np.random.randint(0, 100, size=1000).tolist()  # Gerar lista aleatória de 1000 números
chunk_size = 100


sorted_arr = bubble_sort_parallel(arr, chunk_size)
print(sorted_arr)
