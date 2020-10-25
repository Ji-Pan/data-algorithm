# Heap (binary) sort.  Min heap.
import math, random

def min_heapify(heap_A, i, heap_size):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < heap_size and heap_A[l] < heap_A[i]:
        smallest = l
    else:
        smallest = i
    if r < heap_size and heap_A[r] < heap_A[smallest]:
        smallest = r
    if smallest != i:
        heap_A[i], heap_A[smallest] = heap_A[smallest], heap_A[i]
        min_heapify(heap_A, smallest, heap_size)


def build_min_heap(list_A):
    heap_size = len(list_A)
    if heap_size <= 1:
        return
    for i in reversed(range(0, len(list_A) // 2)):
        min_heapify(list_A, i, heap_size)


def min_heap_sort(heap_A):    # assume we are starting from a min heap.
    heap_size = len(heap_A)
    for i in reversed(range(1, len(heap_A))):
        heap_A[0], heap_A[i] = heap_A[i], heap_A[0]
        heap_size -= 1
        min_heapify(heap_A, 0, heap_size)


def heap_minimum(heap_A):    # assume we are starting from a min heap.
    return heap_A[0]


def heap_extract_min(heap_A):    # assume we are starting from a min heap.
    heap_size = len(heap_A)
    if heap_size < 1:
        raise ValueError("Heap underflow")
    min = heap_A[0]
    heap_A[0] = heap_A[heap_size - 1]
    del heap_A[heap_size - 1]
    heap_size -= 1
    min_heapify(heap_A, 0, heap_size)
    return min


def heap_decrease_key(heap_A, i, key):
    # decrease the value of heap_A[i]
    if key > heap_A[i]:
        raise ValueError("New key is larger than current key")
    heap_A[i] = key
    while i > 0 and heap_A[(i - 1) // 2] > heap_A[i]:
        heap_A[(i - 1) // 2], heap_A[i] = heap_A[i], heap_A[(i - 1) // 2]
        i = (i - 1) // 2


def min_heap_insert(heap_A, key):
    # insert a new node of value key.
    heap_size = len(heap_A)
    heap_size += 1
    heap_A.append(math.inf)
    heap_decrease_key(heap_A, heap_size - 1, key)


def heap_delete(heap_A, i):
    # delete the i-th node in the heap.
    heap_size = len(heap_A)
    heap_A[i], heap_A[heap_size - 1] = heap_A[heap_size - 1], heap_A[i]
    heap_size -= 1
    del heap_A[-1]
    min_heapify(heap_A, i, heap_size)

'''
my_list = random.sample(range(0, 1000), 15)
print(my_list)

min_heap_sort(my_list)
print(my_list)    

my_list = random.sample(range(0, 1000), 15)
print("Original random list: ", my_list)

minroot = heap_minimum(my_list)
print(minroot)

minroot = heap_extract_min(my_list)
print(minroot, my_list)


build_min_heap(my_list)
print(my_list)

min_heap_insert(my_list, 25)
print(my_list)

'''