import random

'''

Sorting Algorithms

'''

def countingSort(arr, digit):
    length = len(arr)
    output = [0 for i in range(length)]
    C =  [0 for i in range(0, 10)]

    # Store count of each number
    for i in range(0, length):
        pos = arr[i] // digit
        C[pos % 10] += 1

    # C[i] contains actual position of this character
    for i in range(1, 10):
        C[i] += C[i-1]

    # Build the output array
    for i in reversed(arr):
        pos = i // digit
        output[C[pos % 10] - 1] = i
        C[pos % 10] -= 1

    # reorganize the initial array based on the output
    for i in range(0, length):
        arr[i] = output[i]


def radixSort(arr):
    maxValue = max(arr)

    digit = 1
    while maxValue // digit > 0:
        countingSort(arr, digit)
        digit *= 10


def insertionSort(A):
    # count = 0
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -=1
            # count +=1
        A[i+1] = key
    # print(f"Number of comparisons: {count}")
    # return count


def bucketSort(array):
    # create empty buckets
    buckets = []
    numBuckets = 100
    length = len(array)
    for i in range(numBuckets):
        buckets.append([])

    # insert elements into respective buckets
    for j in array:
        ID = j//length
        buckets[ID].append(j)
    
    # sort buckets with insertion sort
    for n in buckets:
        insertionSort(n)

    # insert the sorted elements into the original array
    count = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            array[count] = buckets[i][j]
            count += 1
    
    return array

def isSorted(arr): # check if array is sorted in ascending order
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

'''

Min-Heap

'''

def minHeapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1  # for termination condition \
    smallest = i

    if left <= length and array[i][0] > array[left][0]:
        smallest = left
        
    if right <= length and array[smallest][0] > array[right][0]:
        smallest = right

    if smallest != i:
        array[i][0], array[smallest][0] = array[smallest][0], array[i][0]
        minHeapify(array, smallest)   # largest == new i


def buildMinHeap(array):
    for i in reversed(range(len(array)//2)):
        minHeapify(array, i)


def is_min_heap(arr):
    n = len(arr)
    
    # check all but leaf nodes nodes
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        
        # check if min heap condition is violated for left child
        if left < n and arr[i][0] > arr[left][0]:
            return False
        
        # check if min heap condition is violated for right child
        if right < n and arr[i][0] > arr[right][0]:
            return False
    
    return True

'''
Merge K Sorted Lists

'''

def mergeKSortedLists(kSortedLists): # takes in a list of k sorted lists as parameter
    mergedList = []
    minHeap = []

    for i in kSortedLists: # pull the min value from each list and append to min heap
        minValue = i.pop(0) 
        minHeap.append((minValue, i, 0))
    buildMinHeap(minHeap) # need to change minHeapify function to use tuples

    while len(mergedList) > 0: # take min value from the min heap and add to the merged list
        minValue = minHeap.pop(1) 
        mergedList.append(minValue[0])
        nextValue = kSortedLists[minValue[1]][minValue[2]] # finds the next value to add to the min heap based on the list number and position
        minHeap.append((nextValue, minValue[1], minValue[2]+1))
        buildMinHeap(minHeap)

    return mergedList


def main():

    data = [121, 432, 564, 23, 1, 45, 788]
    radixSort(data)
    print(data)
    print(isSorted(data))

    data2 = random.sample(range(1000000), 1000)
    bucketSort(data2)
    print(isSorted(data2))


if __name__ == '__main__':
    main()