import random

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

    for i in range(0, length):
        arr[i] = output[i]

    return output

def radixSort(arr):
    maxValue = max(arr)

    digit = 1
    while maxValue // digit > 0:
        countingSort(arr, digit)
        digit *= 10


def isSorted(arr): # check if array is sorted in ascending order
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

def main():

    data = [121, 432, 564, 23, 1, 45, 788]
    radixSort(data)
    print(data)
    print(isSorted(data))


if __name__ == '__main__':
    main()