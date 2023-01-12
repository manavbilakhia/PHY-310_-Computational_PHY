#fill in a array with 1000 elements in which each element is 1

import numpy as np
import time

def main():
    a = np.zeros(1000)
    start = time.time()
    for i in range(1000):
        a[i] = 1
    end = time.time()
    print(end - start)
