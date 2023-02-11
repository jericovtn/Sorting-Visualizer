# Name: Jerico James F. Viteño
# Final Project: Sorting Visualizer on a Merge Sort
# February 18, 2023 

import matplotlib.pyplot as plt
import numpy as np
import random

random.seed('ABC')

numbers = [random.randint(0, 1000)]

def mergeSort(numberList, left, right):
    
    if left >= right:
        return

    mid = (left + right) // 2

    mergeSort(numberList, left, mid)
    mergeSort(numberList, mid + 1, right)

    merge(numberList, left, right, mid)

def merge(numberList, left, right, mid):
    
    leftCopy = numberList[left : mid +1]
    rightCopy = numberList[mid + 1 : right + 1]

    leftCounter, rightCounter = 0, 0
    sortedCounter = left

    while leftCounter < len(leftCopy) and rightCounter < len(rightCopy):
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
