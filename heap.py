from heapq import heappush, heappop
def heap_sort_easy(arr):
    heap = []
    for element in arr:
        heappush(heap, element)
    sorted_arr = []
    while heap:
        sorted_arr.append(heappop(heap))
    return sorted_arr
numbers = [12, 11, 13, 5, 6, 7]
print("Sorted array:", heap_sort_easy(numbers))