'''

Insetion sort iterates, consuming one input element each repetition, and growing a sorted output list.

At each iteration, insertion sort removes one element from the input data, finds the location it belongs
with in the sorted list, and inserts it there, It repeats until no input elements remain.

'''

def insertion_sort(arr):
    n = len(arr)
    for j in range(1,n):
        key = arr[j]
        i = j-1
        while(i>=0 and arr[i]>key):
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = key

    return 




arr = [1,2,3,4]
insertion_sort(arr)
print(arr)

''' 

- Depends on structure or content? : BOTH
- Internal/ External sort Algorithm? : INTERNAL
- Stable/Unstable sort Algorithm? : TABLE
- Best case time complexity? : O(N) X O(1) = O(N)
- Worst case time complexity? : O(N^2)
- Algorithmic approach? : SUBTRACT AND CONQUER


'''




