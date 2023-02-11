# Name: Jerico James F. Viteño
# Final Project: Sorting Visualizer on a Merge Sort
# February 18, 2023 

import matplotlib.pyplot as plt
import numpy as np
import random

random.seed('ABC')

numbers = [random.randint(0, 100) for _ in range(10)]

def mergeSort(numberList, left, right):
    
    # base case
    if left >= right:
        return

    # find the middle
    mid = (left + right) // 2

    # spilt recursively into left and right values
    mergeSort(numberList, left, mid)
    mergeSort(numberList, mid + 1, right)

    # merge the two results
    merge(numberList, left, right, mid)

def merge(numberList, left, right, mid):
    
    # copy left and right halves into new lists
    leftCopy = numberList[left : mid +1]
    rightCopy = numberList[mid + 1 : right + 1]

    # counters indicating the progress
    leftCounter, rightCounter = 0, 0
    sortedCounter = left

    # until we reach the end of one half
    while leftCounter < len(leftCopy) and rightCounter < len(rightCopy):
        
        # pick the smaller element and put it into the next position and progress the counters
        if leftCopy[leftCounter] <= rightCopy[rightCounter]:
            numberList[sortedCounter] = leftCopy[leftCounter]
            leftCounter += 1
        else:
            numberList[sortedCounter] = rightCopy[rightCounter]
            rightCounter += 1

        sortedCounter += 1

    while leftCounter < len(leftCopy):
        numberList[sortedCounter] = leftCopy[leftCounter]
        leftCounter += 1
        sortedCounter += 1

    while rightCounter < len(rightCopy):
        numberList[sortedCounter] = rightCopy[rightCounter]
        rightCounter += 1
        sortedCounter += 1

print(numbers)    
print(sorted(numbers))
mergeSort(numbers, 0, len(numbers)-1)
print(numbers)
