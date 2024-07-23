import random
import timeit

# Сортування злиттям 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged



# Сортування вставками 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Порівняння алгоритмів
def to_compare():
    num_elements = [50, 500, 5000]

    for n in num_elements:
        data = [random.randint(0, 10000) for i in range(n)]

        print(
            f"{n} elements: Merge Sort: ", timeit.timeit(stmt=f"merge_sort({data})", setup="from __main__ import merge_sort", number=5),
        )
        print(
            f"{n} elements: Insertion Sort: ", timeit.timeit(stmt=f"insertion_sort({data})", setup="from __main__ import insertion_sort", number=5),
        )
        print(
            f"{n} elements: Timsort (sorted): ", timeit.timeit(stmt=f"sorted({data})", setup="import random", number=5),
        )
        print(
            f"{n} elements: Timsort (sort): ",timeit.timeit(stmt=f"{data}.sort()", setup="import random", number=5),
        )
        print("\n")

to_compare()