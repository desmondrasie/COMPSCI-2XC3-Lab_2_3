from numpy import * 
import math 
import random
import timeit
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L
# ************ Dual pivot Quick Sort ************
def dual_quicksort(L):
    copy = dual_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]
        
def dual_quicksort_copy(L):
    if len(L) <= 1:
        return L
    
    pivot1, pivot2 = L[0], L[1]
    if pivot1 > pivot2:
        pivot1, pivot2 = pivot2, pivot1
    
    less, equal, greater = [], [], []
    for i in L:
        if i < pivot1:
            less.append(i)
        elif pivot1 <= i <= pivot2:
            equal.append(i)
        else:
            greater.append(i)
    
    return dual_quicksort_copy(less) + equal + dual_quicksort_copy(greater)


# ************ Traditional Quick Sort ************
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
 
def compareRunTimes():
    n=0 
    # creating empty lists to store times for each sort 
    tquickSortTime=[]
    dquickSortTime=[]
    
    #creating empty lists to store the list length  
    elementstquicksort=[]
    elementsdquicksort=[]
     
    while n < 3000:
        n += 100
        #creating random list to run the tests on
        L1 = create_random_list(3000)
        L2=L1.copy()
        
        #running tests for the traditional quick sort sort
        start = timeit.default_timer()
        quicksort(L1)
        end = timeit.default_timer()
        tquickSortTime.append(end - start)
        elementstquicksort.append(n)
        
        #running tests for the dual pivot quick sort sort
        #L = create_random_list(n,3000)
        start = timeit.default_timer()
        dual_quicksort(L2)
        end = timeit.default_timer()
        dquickSortTime.append(end - start)
        elementsdquicksort.append(n)
        
        
    
    #plotting the graph
    plt.plot(elementstquicksort,tquickSortTime,label = "traditional quick sort")
    plt.plot(elementsdquicksort,dquickSortTime,label = "dual pivot quick sort")
    plt.legend()
    plt.title("Experiment #6")
    plt.xlabel("List Length")
    plt.ylabel("Run Time (s)")
    plt.show
compareRunTimes()
