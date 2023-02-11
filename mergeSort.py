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