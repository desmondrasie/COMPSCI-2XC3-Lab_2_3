import Tools
import random
import timeit
import matplotlib.pyplot as plt


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
#                       ***** Experiments Begin *****
# **************************************************************************


# ******************* ~ Experiment A ~ *******************

nA = 100                 #number of simulations
kA = 1000                #size of the list
maxElementA = 100        #max size of an element

totalBubbleTimeA = 0;
totalInsertionTimeA = 0;
totalSelectionTimeA = 0;

for _ in range(nA):
    L = Tools.create_random_list(kA,maxElementA)
    L2 = L.copy()
    L3 = L.copy()

    start1 = timeit.default_timer()
    bubble_sort(L)
    end1 = timeit.default_timer()
    totalBubbleTimeA += end1 - start1

    start2 = timeit.default_timer()
    insertion_sort(L2)
    end2 = timeit.default_timer()
    totalInsertionTimeA += end2 - start2


    start3 = timeit.default_timer()
    selection_sort(L3)
    end3 = timeit.default_timer()
    totalSelectionTimeA += end3 - start3

# ******************* ~ Experiment B ~ *******************

print("~ Total Run-Times After",nA,"Sorted Lists (seconds) ~")
print("List Size:",kA,"\t"+"Max Element Size:",maxElementA)
print("------------------------------------------------------")
print("Bubble sort:",totalBubbleTimeA)
print("Insertion sort:",totalInsertionTimeA)
print("Selection sort:",totalSelectionTimeA)

# plt.plot()
# plt.show()


