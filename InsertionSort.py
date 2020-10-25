# Insertion sort.  'Insert' list_A[i] into an already sorted list_A[0 : i-1].  Theta n^2.
import random, math

def insertion_sort(list_A):
    length = len(list_A)
    if length <= 1: 
        return
    else:
        for i in range(1, length):
            key = list_A[i]
            j = i - 1
            while j >= 0 and list_A[j] > key:
                list_A[j + 1] = list_A[j]
                j -= 1
            list_A[j + 1] = key


my_list = random.sample(range(1, 1000), 15)
print("Original random list of 15 elements: ", my_list)

insertion_sort(my_list)
print("After insertion sort, the list now is: ", my_list) 
