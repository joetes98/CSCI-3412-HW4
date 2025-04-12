import random
import time
import heapq

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
    buckets = []
    numBuckets = 100

    minNum = min(array)
    maxNum = max(array)

    for i in range(numBuckets):
        buckets.append([])

    # insert elements into respective buckets
    for j in array:
        ID = int((j - minNum) / (maxNum - minNum + 1) * numBuckets)
        ID = min(ID, numBuckets - 1)
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


def isSorted(arr): # check if array is sorted in ascending order
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True


'''
Merge K Sorted Lists

'''

def mergeKSortedListsOptimal(kSortedLists): # takes in a list of k sorted lists as parameter
    '''
    This function merges k Sorted lists into a single list with O(nlog(k)) efficiency
    '''
    mergedList = []
    minHeap = []

    for i,j in enumerate(kSortedLists): # pull the min value from each list and append to min heap
        if len(j) > 0: 
            heapq.heappush(minHeap, (j[0], i, 0))

    while len(minHeap) > 0:
        # take min value from the min heap and add to the merged list
        value, index, nextIndex = heapq.heappop(minHeap)
        mergedList.append(value)

        if nextIndex + 1 < len(kSortedLists[index]): # index out of bounds
            # finds the next value to add to the min heap based on the list number and position
            nextValue = kSortedLists[index][nextIndex+1]
            heapq.heappush(minHeap, (nextValue, index, nextIndex + 1))

    return mergedList


def mergeKSortedLists(kSortedLists): # takes in a list of k sorted lists as parameter
    '''
    This function merges k Sorted lists into a single list with O(nk) efficiency
    '''
    mergedList = []

    while True:
        # initialize minimum value and index
        minValue = 10000000
        index = -1

        # find the minimum value in all lists
        for i in range(len(kSortedLists)):
            if len(kSortedLists[i]) > 0:
                if kSortedLists[i][0] < minValue:
                    minValue = kSortedLists[i][0]
                    index = i

        if index == -1: # checks if all list are empty
            break

        # add value to merged list
        mergedList.append(minValue)
        kSortedLists[index].pop(0)

    return mergedList
'''

Splitting the lists

'''

def splitList(array, sublistCount):
    length = len(array)
    sublistLength = length // sublistCount
    sublists = [array[i:i + sublistLength] for i in range(0, length, sublistLength)]

    return sublists


def main():


    '''
    nlog(k) test
    
    '''
    # read input data from file
    with open("rand1000000.txt", 'r') as file:
        nums = file.read().split()

        integers = [int(num) for num in nums]

    # split into 100 sublists
    sublists = splitList(integers,100)

    # sort the first 50 sublists using radixSort
    for i in range(50):
        radixSort(sublists[i])

    # sort the remaining 50 sublists using bucketSort
    for i in range(50, 100):
        bucketSort(sublists[i])

    # merge  K sorted lists O(nlogk)
    start = time.time()
    mergedSortedList = mergeKSortedListsOptimal(sublists)
    end = time.time()
    total = end - start

    # print(mergedSortedList)
    # print(isSorted(mergedSortedList))

    '''
    nk test
    
    '''
    with open("rand1000000.txt", 'r') as file:
        nums = file.read().split()

        integers2 = [int(num) for num in nums]

    # split into 100 sublists
    sublists2 = splitList(integers2,100)

    # sort the first 50 sublists using radixSort
    for i in range(50):
        radixSort(sublists2[i])

    # sort the remaining 50 sublists using bucketSort
    for i in range(50, 100):
        bucketSort(sublists2[i])


    # merge k sorted lists O(nk)
    start2 = time.time()
    mergedSortedList2 = mergeKSortedLists(sublists2)
    end2 = time.time()
    total2 = end2 - start2

    # print(mergedSortedList2)
    # print(isSorted(mergedSortedList2))

    # output results
    print(f"nlog(k) total time: {total}")
    print(f"nk total time: {total2}")

if __name__ == '__main__':
    main()