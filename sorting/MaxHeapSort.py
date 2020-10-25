# Heap (Binary) sort. Max heap
import math, random

def max_heapify(heap_A, i, heap_size):    # O(lgn)
    l = 2 * i + 1
    r = 2 * i + 2
    if l < heap_size and heap_A[l] > heap_A[i]:
        largest = l
    else: 
        largest = i
    if r < heap_size and heap_A[r] > heap_A[largest]:
        largest = r
    if largest != i:
        heap_A[i], heap_A[largest] = heap_A[largest], heap_A[i]
        max_heapify(heap_A, largest, heap_size)


def build_max_heap(list_A):    # O(n)
    heap_size = len(list_A)
    if heap_size <= 1: 
        return
    for i in reversed(range(0, len(list_A) // 2)):
        max_heapify(list_A, i, heap_size)


def max_heap_sort(heap_A):
    heap_size = len(heap_A)
    for i in reversed(range(1, len(heap_A))):
        heap_A[0], heap_A[i] = heap_A[i], heap_A[0]
        heap_size -= 1
        max_heapify(heap_A, 0, heap_size)


def heap_maximum(heap_A):    # assume we are starting from a min heap.
    return heap_A[0]


def heap_extract_max(heap_A):    # assume we are starting from a min heap.
    heap_size = len(heap_A)
    if heap_size < 1:
        raise ValueError("Heap underflow")
    max = heap_A[0]
    heap_A[0] = heap_A[heap_size - 1]
    del heap_A[heap_size - 1]
    heap_size -= 1
    max_heapify(heap_A, 0, heap_size)
    return max


def heap_increase_key(heap_A, i, key):
    # increase the value of heap_A[i]
    if key < heap_A[i]:
        raise ValueError("New key is smaller than current key")
    heap_A[i] = key
    while i > 0 and heap_A[(i - 1) // 2] < heap_A[i]:
        heap_A[(i - 1) // 2], heap_A[i] = heap_A[i], heap_A[(i - 1) // 2]
        i = (i - 1) // 2


def max_heap_insert(heap_A, key):
    # insert a new node of value key.
    heap_size = len(heap_A)
    heap_size += 1
    heap_A.append(-math.inf)
    heap_increase_key(heap_A, heap_size - 1, key)


def heap_delete(heap_A, i):
    # delete the i-th node in the heap.
    heap_size = len(heap_A)
    heap_A[i], heap_A[heap_size - 1] = heap_A[heap_size - 1], heap_A[i]
    heap_size -= 1
    del heap_A[-1]
    max_heapify(heap_A, i, heap_size)


my_list = random.sample(range(0, 100), 15)
print("Original random list: ", my_list)

build_max_heap(my_list)
print(my_list)

heap_delete(my_list, 5)
print(my_list)

'''
max_heap_insert(my_list, 79)
print(my_list)

max_heap_sort(my_list)
print("After heap sort, the list: ", my_list)    # should be a sorted list.

'''