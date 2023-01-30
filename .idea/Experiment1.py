from numpy import *
import math
import random
import timeit
import matplotlib.pyplot as plt

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




# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

# **************************************************************************
#                       ***** Experiments Begin *****
# **************************************************************************



def compareRunTimes():
    n=0
    # creating empty lists to store times for each sort 
    bubbleSortTime=[]
    insertionSortTime=[]
    selectionSortTime=[]

    #creating empty lists to store the list length  
    elementsBubbleSort=[]
    elementsInsertionSort=[]
    elementsSectionSort=[]


    while n < 3000:
        n += 100


        #running tests for the bubble sort
        L = create_random_list(n)
        start = timeit.default_timer()
        bubble_sort(L)
        end = timeit.default_timer()
        bubbleSortTime.append(end - start)
        elementsBubbleSort.append(n)

        #running tests for the insertion sort
        L = create_random_list(n)
        start = timeit.default_timer()
        insertion_sort(L)
        end = timeit.default_timer()
        insertionSortTime.append(end - start)
        elementsInsertionSort.append(n)

        #running tests for the selection sort
        L = create_random_list(n)
        start = timeit.default_timer()
        selection_sort(L)
        end = timeit.default_timer()
        selectionSortTime.append(end - start)
        elementsSectionSort.append(n)

    #plotting the graph
    plt.plot(elementsBubbleSort,bubbleSortTime,label = "bubble sort")
    plt.plot(elementsInsertionSort,insertionSortTime,label = "insertion sort")
    plt.plot(elementsSectionSort,selectionSortTime,label = "selection sort")
    plt.legend()
    plt.show()

compareRunTimes()
