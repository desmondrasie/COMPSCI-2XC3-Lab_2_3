import Tools
import timeit
import matplotlib.pyplot as plt


# ******************* Swap Function code *******************
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# ******************* Traditional Bubble sort code *******************
L = [1,9,2,6,3,4,5,1]
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            # print(j,len(L),count)
            if L[j] > L[j+1]:
                swap(L, j, j+1)

# ******************* Optimizied Bubble sort code *******************
def bubble_sort2(L):
    count = 1
    for i in range(len(L)):
        value = L[0]
        for j in range(len(L) - count):
            if value > L[j+1]:
                L[j] = L[j+1]
            else:
                L[j] = value
                value = L[j+1]
        L[-count] = value
        count += 1

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

# ******************* Optimized Selection sort code *******************
def selection_sort2(L):
    for i in range((len(L)+1)//2):
        min_index = find_min_index2(L, i)
        max_index = find_max_index2(L,len(L)-i-1)
        swap(L, i, min_index)
        swap(L, len(L)-i-1, max_index)

def find_min_index2(L, n):
    min_index = n
    for i in range(n+1, len(L)-n):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

def find_max_index2(L,n):
    max_index = n
    for i in range(n,n-1):
        if L[i] > L[max_index]:
            max_index = i
    return max_index


# **************************************************************************
#                       ***** Experiments Begin *****
# **************************************************************************

def compareRunTimes():
    n = 0
    # creating empty lists to store times for each sort
    bubbleSortTime=[]
    bubbleSortTime2=[]
    selectionSortTime=[]
    selectionSortTime2=[]

    #creating empty lists to store the list length
    elementsBubbleSort=[]
    elementsBubbleSort2=[]
    elementsSelectionSort=[]
    elementsSelectionSort2=[]

    while n < 5000:
        n += 100

        L = Tools.create_random_list(n,n)
        L2 = L.copy()
        L3 = L.copy()
        L4 = L.copy()

        #running tests for Traditional Bubble sort
        start = timeit.default_timer()
        bubble_sort(L)
        end = timeit.default_timer()
        bubbleSortTime.append(end - start)
        elementsBubbleSort.append(n)

        #running tests for Traditional Selection sort
        start = timeit.default_timer()
        selection_sort(L2)
        end = timeit.default_timer()
        selectionSortTime.append(end - start)
        elementsSelectionSort.append(n)

        #running tests for Optimized Bubble sort
        start = timeit.default_timer()
        bubble_sort2(L3)
        end = timeit.default_timer()
        bubbleSortTime2.append(end - start)
        elementsBubbleSort2.append(n)

        #running tests for Optimized Selection sort
        start = timeit.default_timer()
        selection_sort2(L4)
        end = timeit.default_timer()
        selectionSortTime2.append(end - start)
        elementsSelectionSort2.append(n)

    #plotting the graph
    figure, (ax1, ax2) = plt.subplots(2,sharex=True)
    ax1.plot(elementsBubbleSort,bubbleSortTime,label = "Traditional")
    ax1.plot(elementsBubbleSort2,bubbleSortTime2,label = "Optimized")
    ax1.set_title("Bubble Sort Comparison")
    ax1.legend()

    ax2.plot(elementsSelectionSort,selectionSortTime,label = "Traditional")
    ax2.plot(elementsSelectionSort2,selectionSortTime2,label = "Optimized")
    ax2.set_title("Selection Sort Comparison")
    ax2.legend()

    figure.suptitle("Experiment #2")
    figure.supxlabel("List Length")
    figure.supylabel("Run Time (s)")

    plt.show()


compareRunTimes()
