
def selection_sort(arr):

    for i in range(len(arr)-1):
        min = arr[i]

        for j in range(i+1,len(arr)):
            if min>arr[j]:
                min = arr[j]

                arr[j] = arr[i]
                arr[i] = min

    return arr
import numpy as np


a = np.random.randint(0,100,10)

sorted_arr = selection_sort(a)
print(sorted_arr)



