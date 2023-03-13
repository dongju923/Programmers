import numpy as np
def solution(array):
    array.sort()
    mid = len(array) // 2
    return array[mid]
    #return np.median(array)

    