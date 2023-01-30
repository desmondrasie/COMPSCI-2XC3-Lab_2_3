# In the file bad_sorts.py posted alongside this document, you will find implementations of Bubble,
# Insertion, and Selection sort. Run suitable experiments to compare the runtimes of these three
# algorithms. In bad_sorts there is a create_random_list function which may be useful. In your report this
# section should include:

#  An explicit outline of the experiments you ran. That is, list length values, how many “runs”, etc.
#  A graph of list length vs time displaying the three curves corresponding to the three “bad”
# sorting algorithms
#  A brief discussion and conclusion regarding the results. A few sentences are fine here.

import random
import timeit


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

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

# **************************************************************************
# ***** TOSS EVERYTHING ABOVE INTO A MODULE SO ALL EXPERIMENTS CAN USE *****
# **************************************************************************


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
#                       ***** Experiement Begins *****
# **************************************************************************


n = 100
k = 1000
totalBubbleTime = 0;
totalInsertionTime = 0;
totalSelectionTime = 0;

for _ in range(n):
    L = create_random_list(k,k)
    L2 = L.copy()
    L3 = L.copy()

    start1 = timeit.default_timer()
    bubble_sort(L)
    end1 = timeit.default_timer()
    totalBubbleTime += end1 - start1


    start2 = timeit.default_timer()
    insertion_sort(L2)
    end2 = timeit.default_timer()
    totalInsertionTime += end2 - start2

    start3 = timeit.default_timer()
    selection_sort(L3)
    end3 = timeit.default_timer()
    totalSelectionTime += end3 - start3

print("~ Total Run-Times After",n,"Sorts (seconds) ~")
print("----------------")
print("Bubble Sort:",totalBubbleTime)
print("Insertion Sort:",totalInsertionTime)
print("Selection Sort:",totalSelectionTime)





