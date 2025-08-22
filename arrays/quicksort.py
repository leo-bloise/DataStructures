def swap(arr: list[int], i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr: list[int], lo: int, hi: int) -> int:

    pivot = arr[hi]

    i = lo - 1

    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    i += 1
    swap(arr, i, hi)

    return i

def qs(arr: list[int], lo: int, hi: int):
    if lo < hi:
        pivot = partition(arr, lo, hi)

        qs(arr, lo, pivot - 1)
        qs(arr, pivot + 1, hi)

def quicksort(arr: list[int]) -> list[int]:
    new_arr = [element for element in arr]
    
    qs(new_arr, 0, len(new_arr) - 1)

    return new_arr