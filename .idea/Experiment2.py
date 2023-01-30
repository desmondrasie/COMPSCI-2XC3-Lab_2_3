import Tools
import timeit

import Tools
import timeit


# ******************* Swap Function code *******************
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# ******************* Bubble sort code *******************
# Traditional Bubble sort


L = [1,9,2,6,3,4,5,1]
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            # print(j,len(L),count)
            if L[j] > L[j+1]:
                swap(L, j, j+1)
def bubble_sort2(L):
    count = 1
    for i in range(len(L)):
        value = L[0]
        for j in range(len(L) - count):
            # print(j,len(L),count)
            if value > L[j+1]:
                L[j] = L[j+1]
            else:
                L[j] = value
                value = L[j+1]
        L[len(L)-count] = value
        count += 1

print(L)
bubble_sort2(L)
print(L)

# **************************************************************************
#                       ***** Experiments Begin *****
# **************************************************************************


n = 100                 #number of simulations
k = 1000                #length of the list
maxElement = 100        #max size of an element

totalBubbleTime1 = 0;
totalBubbleTime2 = 0;

for _ in range(n):
    L = Tools.create_random_list(k,maxElement)
    L2 = L.copy()

    start = timeit.default_timer()
    bubble_sort(L)
    end = timeit.default_timer()
    totalBubbleTime1 += end - start

    start = timeit.default_timer()
    bubble_sort2(L)
    end = timeit.default_timer()
    totalBubbleTime2 += end - start

print("~ Total Run-Times After",n,"Sorted Lists (seconds) ~")
print("List Size:",k,"\t"+"Max Element Size:",maxElement)
print("------------------------------------------------------")
print("Bubble sort original:",totalBubbleTime1)
print("Bubble sort optimized:",totalBubbleTime2)
