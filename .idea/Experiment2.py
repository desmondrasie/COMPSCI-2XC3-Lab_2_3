import Tools
import timeit


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
        # print(L)
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

# L = [1,9,2,6,3,4,5,1]
# L2 = L.copy()
# # print(L)
# selection_sort(L)
# selection_sort2(L2)
# # print(L)
# print(L2)



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
    bubble_sort2(L2)
    end = timeit.default_timer()
    totalBubbleTime2 += end - start

print("------------------------------------------------------")
print("~ Total Run-Times After",n,"Sorted Lists (seconds) ~")
print("List Size:",k,"\t"+"Max Element Size:",maxElement)
print("------------------------------------------------------")
print("Bubble sort original:",totalBubbleTime1)
print("Bubble sort optimized:",totalBubbleTime2)
print("")


totalSelectionTime1 = 0;
totalSelectionTime2 = 0;

for _ in range(n):
    L = Tools.create_random_list(k,maxElement)
    L2 = L.copy()

    start = timeit.default_timer()
    selection_sort(L)
    end = timeit.default_timer()
    totalSelectionTime1 += end - start

    start = timeit.default_timer()
    selection_sort2(L2)
    end = timeit.default_timer()
    totalSelectionTime2 += end - start


print("*****************************************************")
print("~ Total Run-Times After",n,"Sorted Lists (seconds) ~")
print("List Size:",k,"\t"+"Max Element Size:",maxElement)
print("------------------------------------------------------")
print("Selection sort original:",totalSelectionTime1)
print("Selection sort optimized:",totalSelectionTime2)
