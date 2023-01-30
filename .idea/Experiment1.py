import Tools
import random
import timeit


# ******************* Bubble sort code *******************
# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                Tools.swap(L, j, j+1)


# ******************* Insertion sort code *******************
# Traditional Insertion sort
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)

def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            Tools.swap(L, i-1, i)
            i -= 1
        else:
            return


# ******************* Selection sort code *******************
# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        Tools.swap(L, i, min_index)

def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


# **************************************************************************
#                       ***** Experiment Begins *****
# **************************************************************************


n = 100
k = 1000
totalBubbleTime = 0;
totalInsertionTime = 0;
totalSelectionTime = 0;

for _ in range(n):
    L = Tools.create_random_list(k,k)
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

print("~ Total Run-Times After",n,"Sorted Lists (seconds) ~")
print("------------------------------------------------------")
print("Bubble sort:",totalBubbleTime)
print("Insertion sort:",totalInsertionTime)
print("Selection sort:",totalSelectionTime)





