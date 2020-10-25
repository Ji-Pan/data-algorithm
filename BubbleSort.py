# Bubblesort.  Repeatedly swapping adjacent elements that are out of order. Theta n^2.
import math, random

def bubble_sort(list_A):
    length = len(list_A)
    for i in range(0, length):
        j = length - 1
        while j > i:
            if list_A[j] < list_A[j - 1]:
                list_A[j], list_A[j - 1] = list_A[j - 1], list_A[j]
            j -= 1


my_list = random.sample(range(1, 1000), 15)
print("Original random list of 15 elements: ", my_list)

bubble_sort(my_list)
print("After bubble sort, the list now is: ", my_list) 