from numpy import * 
import math 
import random
import timeit
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L

# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return
        # ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L
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

# *************************************
# **************************************************************************
#                       ***** Experiments Begin *****
# **************************************************************************

def compareRunTimes():
    # creating empty lists to store times for each sort
    n=0
    mergeSortTime=[]
    quickSortTime=[]
    insertionSortTime=[]
    
    #creating empty lists to store the list length  
    elementsInsertionSort=[]
    elementsMergeSort=[]
    elementsQuickSort=[]
    
    while n<50:
        
        L1 = create_random_list(n)
        L2=L1.copy()
        L3=L1.copy()
        #running tests for the insertion sort
        start = timeit.default_timer()
        insertion_sort(L1)
        end = timeit.default_timer()
        insertionSortTime.append(end - start)
        elementsInsertionSort.append(n)
        
        #running tests for the merge sort
        #L = create_random_list(n,3000)
        start = timeit.default_timer()
        mergesort(L2)
        end = timeit.default_timer()
        mergeSortTime.append(end - start)
        elementsMergeSort.append(n)
        
        #running tests for the quick sort
        #L = create_random_list(n,3000)
        start = timeit.default_timer()
        quicksort(L3)
        end = timeit.default_timer()
        quickSortTime.append(end - start)
        elementsQuickSort.append(n)
        n+=5
# plotting the graph with 3 curves for each sort         
    plt.plot(elementsInsertionSort,insertionSortTime,label = "insertion sort")
    plt.plot(elementsMergeSort,mergeSortTime,label = "merge sort")
    plt.plot(elementsQuickSort,quickSortTime,label = "quick sort")
    plt.legend()
    plt.title("Experiment #8")
    plt.xlabel("List Length")
    plt.ylabel("Run Time (s)")
    plt.show
    
compareRunTimes()
