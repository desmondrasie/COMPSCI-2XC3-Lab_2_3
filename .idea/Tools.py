# Tools Module
import random

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

create_near_sorted_list(3,2,3)
