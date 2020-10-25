# Merge sort.  Divide the part of list to be sorted into two parts, then merge.  Theta n(lgn)
import math, random

def merge(list_A, p, q, r):
    n1 = q - p
    n2 = r - q
    L = list()
    R = list()
    for i in range(0, n1):
        L.append(list_A[p + i])
    for j in range(0, n2):
        R.append(list_A[q + j])
    L.append(math.inf)    # sentinel to guarantee the latter comparison
    R.append(math.inf)
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:    # for two identical numbers, the one with smaller index gets first.
            list_A[k] = L[i]
            i += 1
        else:
            list_A[k] = R[j]
            j += 1


def merge_sort(list_A, p, r):
    length = len(list_A)
    if p >= length or r > length:
        print("Index out of range.")
        return
    elif p >= r - 2:
        q = math.floor((p + r) / 2)
        merge(list_A, p, q, r)
    else:
        q = math.floor((p + r) / 2)
        merge_sort(list_A, p, q)
        merge_sort(list_A, q, r)
        merge(list_A, p, q, r)
 

my_list = random.sample(range(1, 1000), 15)
print("Original random list of 15 elements: ", my_list)

merge_sort(my_list, 0, 15)
print("After merge sort, the list now is: ", my_list) 