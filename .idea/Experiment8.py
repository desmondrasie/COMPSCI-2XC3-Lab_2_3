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
    #Firstly We're running tests for n value to be less than 20 
    # creating empty lists to store times for each sort
    n=0
    mergeSortTime1=[]
    quickSortTime1=[]
    insertionSortTime1=[]
    
    #creating empty lists to store the list length  
    elementsInsertionSort1=[]
    elementsMergeSort1=[]
    elementsQuickSort1=[]
    
    while n<20:
        n+=1
        L1 = create_random_list(n)
        L2=L1.copy()
        L3=L1.copy()
        #running tests for the insertion sort
        start = timeit.default_timer()
        insertion_sort(L1)
        end = timeit.default_timer()
        insertionSortTime1.append(end - start)
        elementsInsertionSort1.append(n)
        
        #running tests for the merge sort
        #L = create_random_list(n,3000)
        start = timeit.default_timer()
        mergesort(L2)
        end = timeit.default_timer()
        mergeSortTime1.append(end - start)
        elementsMergeSort1.append(n)
        
        #running tests for the quick sort
        #L = create_random_list(n,3000)
        start = timeit.default_timer()
        quicksort(L3)
        end = timeit.default_timer()
        quickSortTime1.append(end - start)
        elementsQuickSort1.append(n)
        
    #Now, We're running tests for n value to be less than 15 
    # creating empty lists to store times for each sort    

    n=0
    mergeSortTime2=[]
    quickSortTime2=[]
    insertionSortTime2=[]
    
    #creating empty lists to store the list length  
    elementsInsertionSort2=[]
    elementsMergeSort2=[]
    elementsQuickSort2=[]
    
    while n<15:
        n+=1
        L1 = create_random_list(n)
        L2=L1.copy()
        L3=L1.copy()
        start = timeit.default_timer()
        insertion_sort(L1)
        end = timeit.default_timer()
        insertionSortTime2.append(end - start)
        elementsInsertionSort2.append(n)
        
        #running tests for the merge sort
        #L = create_random_list(n,3000)
        start = timeit.default_timer()
        mergesort(L2)
        end = timeit.default_timer()
        mergeSortTime2.append(end - start)
        elementsMergeSort2.append(n)
        
        #running tests for the quick sort
        #L = create_random_list(n,3000)
        start = timeit.default_timer()
        quicksort(L3)
        end = timeit.default_timer()
        quickSortTime2.append(end - start)
        elementsQuickSort2.append(n)

    #Now, We're running tests for n value to be less than 9 
    # creating empty lists to store times for each sort
    
    n=0
    mergeSortTime3=[]
    quickSortTime3=[]
    insertionSortTime3=[]
    
    #creating empty lists to store the list length  
    elementsInsertionSort3=[]
    elementsMergeSort3=[]
    elementsQuickSort3=[]
    
    while n<9:
        n+=1
        L1 = create_random_list(n)
        L2=L1.copy()
        L3=L1.copy()
        start = timeit.default_timer()
        insertion_sort(L1)
        end = timeit.default_timer()
        insertionSortTime3.append(end - start)
        elementsInsertionSort3.append(n)
        
        #running tests for the merge sort
        #L = create_random_list(n,3000)
        start = timeit.default_timer()
        mergesort(L2)
        end = timeit.default_timer()
        mergeSortTime3.append(end - start)
        elementsMergeSort3.append(n)
        
        #running tests for the quick sort
        #L = create_random_list(n,3000)
        start = timeit.default_timer()
        quicksort(L3)
        end = timeit.default_timer()
        quickSortTime3.append(end - start)
        elementsQuickSort3.append(n)       
    #plotting all the 3 different plots for different values using gridspec
    gs = gridspec.GridSpec(2, 2)
    plt.figure()
    
    ax = plt.subplot(gs[0, 0]) # row 0, col 0
    plt.plot(elementsInsertionSort1,insertionSortTime1,label = "insertion sort")
    plt.plot(elementsMergeSort1,mergeSortTime1,label = "merge sort")
    plt.plot(elementsQuickSort1,quickSortTime1,label = "quick sort")
    
    
    ax = plt.subplot(gs[0, 1]) # row 0, col 1
    plt.plot(elementsInsertionSort2,insertionSortTime2,label = "insertion sort")
    plt.plot(elementsMergeSort2,mergeSortTime2,label = "merge sort")
    plt.plot(elementsQuickSort2,quickSortTime2,label = "quick sort")
    
    ax = plt.subplot(gs[1, :]) # row 0, col 1
    plt.plot(elementsInsertionSort3,insertionSortTime3,label = "insertion sort")
    plt.plot(elementsMergeSort3,mergeSortTime3,label = "merge sort")
    plt.plot(elementsQuickSort3,quickSortTime3,label = "quick sort")
    
compareRunTimes()
