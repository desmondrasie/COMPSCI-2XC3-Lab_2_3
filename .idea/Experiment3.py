import Tools
import timeit
import matplotlib.pyplot as plt

# ******************* Swap Function code *******************
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# ******************* Traditional Bubble sort code *******************
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

# ******************* Traditional Selection sort code *******************
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

# ******************* Traditional Insertion sort code *******************
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

# **************************************************************************
#                       ***** Experiments Begin *****
# **************************************************************************

def compareRunTimes():
    numOfSwaps = -100 #start at -100 since first iteration increments by 100; 0 swaps to start
    n = 5000
    #creating empty lists to store the Run Times of each sort
    bubbleSortTime=[]
    insertionSortTime=[]
    selectionSortTime=[]

    #creating empty lists to store the Number of Swaps of each sort
    elementsBubbleSort=[]
    elementsInsertionSort=[]
    elementsSectionSort=[]


    while numOfSwaps < 3000:
        numOfSwaps += 100

        #running tests for the bubble sort
        L = Tools.create_near_sorted_list(n,n,numOfSwaps)
        L2 = L.copy()
        L3 = L.copy()
        start = timeit.default_timer()
        bubble_sort(L)
        end = timeit.default_timer()
        bubbleSortTime.append(end - start)
        elementsBubbleSort.append(numOfSwaps)

        #running tests for the insertion sort
        start = timeit.default_timer()
        insertion_sort(L2)
        end = timeit.default_timer()
        insertionSortTime.append(end - start)
        elementsInsertionSort.append(numOfSwaps)

        #running tests for the selection sort
        start = timeit.default_timer()
        selection_sort(L3)
        end = timeit.default_timer()
        selectionSortTime.append(end - start)
        elementsSectionSort.append(numOfSwaps)

    #plotting the graph
    plt.plot(elementsBubbleSort,bubbleSortTime,label = "bubble sort")
    plt.plot(elementsInsertionSort,insertionSortTime,label = "insertion sort")
    plt.plot(elementsSectionSort,selectionSortTime,label = "selection sort")
    plt.legend()
    plt.title("Experiment #3")
    plt.xlabel("Number Of Swaps")
    plt.ylabel("Run Time (s)")
    plt.show()

compareRunTimes()

