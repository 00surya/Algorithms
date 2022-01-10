def exchange(arr,i,j):
    elem_j = arr[j]
    arr[j] = arr[i]
    arr[i] = elem_j
    return



def max_heapify(arr,i):
    global heap_size
    L = 2*i
    R = 2*i + 1
    # heap_size = len(arr) - 1
    if L <= heap_size and arr[L] > arr[i]:
            largest = L
    else:
        largest = i

    if R <= heap_size and arr[R] > arr[largest]:
        largest = R

    
    if largest != i:
        exchange(arr,i,largest)
        max_heapify(arr,largest)


def max_heap(arr):
    for i in range(heap_size,-1,-1):
        max_heapify(arr,i)    


def heap_sort(arr):
    global heap_size
    max_heap(arr)
    n = len(arr)-1
    for i in range(n,-1,-1):
        exchange(arr,i,0)
        heap_size -= 1
        max_heap(arr)
    return 

def main(arr):
    global heap_size
    heap_size = len(arr)-1
    heap_sort(arr)
    
    print(arr)
    

if __name__ == "__main__":
    arrs = [ [9,8,7,6,5,4,3,2,1], [], [1,2,3,4,5], [900,800,345,12232123112,93292,2313], [2,0] ]

    for arr in arrs:
        main(arr)
        