from operator import truediv
import timeit
import matplotlib.pyplot as plt
import random

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

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

def dual_quicksort(L):
    copy = dual_quicksort_copy(L)
    for i in range (len(L)):
        L[i] = copy[i]
    return

def dual_quicksort_copy(L):
    # in theory quite similar to normal quicksort
    # but instead of left+pivot+right, we have
    # left+lpivot+middle+rpivot
    # where left={all x<lpivot<=rpivot},
    # and  right={all lpivot<=rpivot<x}
    # and middle={all lpivot<=x<=rpivot}
    # by maintaining lpivot<rpivot, their
    # positions in order are maintained
    # in the recursive sorting

    if len(L) < 2:
        return L
    pivotL = 0
    pivotR = 1
    # we need pivotL<pivotR, so swap if not true
    if(L[pivotL]>L[pivotR]):
        temp = pivotL
        pivotL = pivotR
        pivotR = temp

    left, middle, right = [], [], []
    for i in range(len(L)):
        if(i!=pivotL and i!=pivotR):
            num=L[i]
            if num < L[pivotL] and num < L[pivotR]:
                left.append(num)
            elif num > L[pivotL] and num > L[pivotR]:
                right.append(num)
            else:
                middle.append(num)
    return dual_quicksort_copy(left) + [L[pivotL]] + dual_quicksort_copy(middle) + [L[pivotR]] + dual_quicksort_copy(right)



# ************ Algorithm Correctness Testing ************

def sorted(L):
    for x in range(len(L)):
        if(x<len(L)-1):
            if(L[x]>L[x+1]):
                return False
    return True

def test_dual_quicksort():
    n=10000 # number of lists
    l=100  # length of each list
    m=100  # max value of each element
    for i in range (0,n-1):
        L = create_random_list(l,m)
        dual_quicksort(L)
        if(not sorted(L)): 
            print('failure on: ')
            print(L)
    print('dual quicksort testing on ',n,' lists complete')

def test_dual_quicksort_detailed():
    testlists=[]
    n = 10
    for i in range (0,n-1):
        l = create_random_list(n,100)
        print('Sort via Dual Quicksort')
        print('Start: ', l)
        dual_quicksort(l)
        print('Sorted: ', l)
        print(sorted(l))
        l = create_random_list(n,100)
        print('Sort via QuickSort')
        print('Start: ', l)
        quicksort(l)
        print('Sorted: ', l)
        print(sorted(l))

#test_dual_quicksort()
    

# **************************************************************************
#                       ***** Experiments Begin *****
# **************************************************************************

def compareRunTimes():
    s = 0   # min length of list tested
    i = 1000    # interval of length increase
    l = 50000  # max length of list tested
    m = 1000    # max integer value per element
    n = 10     # number of trials per length l_k

    # creating empty lists to store times for each sort
    quickSortTime=[]
    dualQuickSortTime=[]

    j = s
    while j<=l:
        quickSortDT=[]
        dualQuickSortDT=[]

        # take average of n trials for each list length l_k
        for _ in range (0,n):
            #running tests for the quick sort
            L = create_random_list(j,m)
            L2 = L.copy()
            start = timeit.default_timer()
            quicksort(L)
            end = timeit.default_timer()
            quickSortDT.append(end - start)

            #running tests for dual quick sort
            start = timeit.default_timer()
            dual_quicksort(L2)
            end = timeit.default_timer()
            dualQuickSortDT.append(end - start)

        quickSortTime.append(sum(quickSortDT)/len(quickSortDT))
        dualQuickSortTime.append(sum(dualQuickSortDT)/len(dualQuickSortDT))

        j+=i


    #plotting the graph
    plt.plot(range(s,l+1,i),quickSortTime,label = "quick sort")
    plt.plot(range(s,l+1,i),dualQuickSortTime,label = "dual quick sort")
    plt.legend()
    plt.title("Experiment #6")
    plt.xlabel("Length of List")
    plt.ylabel("Run Time (s)")
    plt.show()

compareRunTimes()
