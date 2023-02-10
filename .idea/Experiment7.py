from numpy import * 
import math 
import random
import timeit
import matplotlib.pyplot as plt

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L
        
# ************ Bottom Up Merge Sort ************    
def bottom_up_mergesort(L):
    n = len(L)
    step = 1
    while step < n:
        for i in range(0, n, step * 2):
            L[i:i + step * 2] = merge_bottom_up(L[i:i + step], L[i + step:i + step * 2])
        step *= 2
    return L

def merge_bottom_up(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
# ************ Traditional Merge Sort ************
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


def compareRunTimes():
    n=0 
    # creating empty lists to store times for each sort 
    tmergeSortTime=[]
    bmergeSortTime=[]
    
    #creating empty lists to store the list length  
    elementsttmergesort=[]
    elementsbmergesort=[]
     
    while n < 3000:
        n += 100
        #creating random list to run the tests on
        L1 = create_random_list(3000)
        L2=L1.copy()
        
        #running tests for the traditional sort
        start = timeit.default_timer()
        mergesort(L1)
        end = timeit.default_timer()
        tmergeSortTime.append(end - start)
        elementsttmergesort.append(n)
        
        #running tests for the bottom up merge sort
        #L = create_random_list(n,3000)
        start = timeit.default_timer()
        bottom_up_mergesort(L2)
        end = timeit.default_timer()
        bmergeSortTime.append(end - start)
        elementsbmergesort.append(n)
        
        
    
    #plotting the graph
    plt.plot(elementsttmergesort,tmergeSortTime,label = "traditional merge sort")
    plt.plot(elementsbmergesort,bmergeSortTime,label = "bottom up merge sort")
    plt.legend()
    plt.title("Experiment #7")
    plt.xlabel("List Length")
    plt.ylabel("Run Time (s)")
    plt.show
compareRunTimes()
