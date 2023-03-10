# Name: Jerico James F. Viteño
# Final Project: Sorting Visualizer on a Bubble Sort
# February 18, 2023 

import matplotlib.pyplot as plt
import numpy as np

amount = 50

list = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

n = len(list)

# Bubble Sort
for i in range(n):
    for j in range(0, n-i-1):
        plt.bar(x, list)
        plt.pause(0.001)
        plt.clf()
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

plt.show()