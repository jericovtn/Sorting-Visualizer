# Name: Jerico James F. Viteño
# Final Project: Sorting Visualizer on a Merge Sort
# February 18, 2023 

import matplotlib.pyplot as plt
import numpy as np
import random

random.seed('ABC')

amount = 20

numbers = [random.randint(0, 1000) for _ in range(amount)]

def mergeSort(numberList, left, right):
    
    # base case
    if left >= right:
        return

    # find the middle
    mid = (left + right) // 2

    # // Animations
    plt.bar(list(range(amount)), numberList)
    plt.pause(0.001)
    plt.clf()

    # spilt recursively into left and right values
    mergeSort(numberList, left, mid)
    mergeSort(numberList, mid + 1, right)

    # // Animations
    plt.bar(list(range(amount)), numberList)
    plt.pause(0.001)
    plt.clf()

    # merge the two results
    merge(numberList, left, right, mid)

    # // Animations
    plt.bar(list(range(amount)), numberList)
    plt.pause(0.001)
    plt.clf()

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

mergeSort(numbers, 0, len(numbers)-1)
print(numbers)

# // Animations
plt.bar(list(range(amount)), numbers)
plt.show()
