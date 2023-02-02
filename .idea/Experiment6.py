import Tools
import timeit
import matplotlib.pyplot as plt


# ************ Quick Sort ************
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

# ************ Dual Quick Sort ************

def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)


def quickSortWithTwoPivots(arr, low, high):
    if low >= high:
        return

    p1, p2 = choosePivots(arr, low, high)
    i = low + 1
    k = low + 1
    j = high
    while k <= j:
        if arr[k] < p1:
            arr[i], arr[k] = arr[k], arr[i]
            i += 1
            k += 1
        elif arr[k] <= p2:
            k += 1
        else:
            arr[k], arr[j] = arr[j], arr[k]
            j -= 1
    i -= 1
    j += 1
    arr[low], arr[i] = arr[i], arr[low]
    arr[high], arr[j] = arr[j], arr[high]

    quickSortWithTwoPivots(arr, low, i - 1)
    quickSortWithTwoPivots(arr, j + 1, high)

def choosePivots(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    arr[low], arr[mid] = arr[mid], arr[low]
    return arr[low], arr[high]

arr = [int(i) for i in input("Enter the elements of the list to be sorted: ").split()]
quickSortWithTwoPivots(arr, 0, len(arr) - 1)
print("Sorted list:", arr)

