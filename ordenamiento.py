# DISEÑO Y ANALISIS DE ALGORITMOS
# ALEJANDRO ANTONIO AMAVIZCA LOPEZ
# METODOS DE ORDENAMIENTO



# BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print("BURBUJA")
print("DATOS ORIGINALES: ")
print(arr)
print("DATOS ORDENADOS: ")
print(bubble_sort(arr))


# INSERTION SORT
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("INSERCIÓN")
print("DATOS ORIGINALES: ")
print(arr)
print("DATOS ORDENADOS: ")
print(insertion_sort(arr))


# POR SELECCIÓN
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print("SELECCIÓN")
print("DATOS ORIGINALES: ")
print(arr)
print("DATOS ORDENADOS: ")
print(selection_sort(arr))

#  QUICK SORT
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    aux = arr[len(arr) // 2]
    left = [x for x in arr if x < aux]
    middle = [x for x in arr if x == aux]
    right = [x for x in arr if x > aux]
    return quick_sort(left) + middle + quick_sort(right)


arr = [64, 34, 25, 12, 22, 11, 90]
print("QUICK SORT")
print("DATOS ORIGINALES: ")
print(arr)
print("DATOS ORDENADOS: ")
print(quick_sort(arr))

# MERGE SORT
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

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


arr = [64, 34, 25, 12, 22, 11, 90]
print("MERGE SORT")
print("DATOS ORIGINALES: ")
print(arr)
print("DATOS ORDENADOS: ")
print(merge_sort(arr))

# HEAP SORT
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print("HEAP SORT")
print("DATOS ORIGINALES: ")
print(arr)
print("DATOS ORDENADOS: ")
print(heap_sort(arr))
