'''

Bubble sort sometimes reffered to as sink sort, it is a simple sorting algoritm that repeatdly steps through the
list, compares adjacent elements and swap them if they are in wrong order.
Pass throught the list is repeated until the list is sorted The alogrithm, which is comparison sort, is named for
for the way smaller or larger elements "bubble" to the top of list.

EX- [4,3,2,1]
Bubble precessing:
max((4,3)) = 4 swap the max element to the last ....swaped pair (3,4)
- ouput: [3,4,2,1]
max((4,2)) = 4 swap... (2,4)
- output: [3,2,4,1]
max((4,1)) = 4 swap... (1,4)
- output: [3,2,1,4]

.... max(3,2) = 3 (2,3) - output: [2,3,1,4]......max(3,1) = 3 (1,3) - output: [2,1,3,4]
.... max(2,1) = 2 (1,2) - output: [1,2,3,4]....and our array is sorted : )


'''




def bubble_sort(arr):
    n = len(arr)-1 # exact length from 0
    for k in range(1,n):  # from 1 to n-1
        ptr = 0           # ptr = 0 and ptr+1
        while ptr <= n-k: # making right side sorted using divide and conquer alogorithm!
            if arr[ptr]>arr[ptr+1]:
                d = arr[ptr]
                arr[ptr] = arr[ptr+1]
                arr[ptr+1] = d
            ptr+=1
    
    return arr


a = [0,1,2,3,4,5,6]

print(bubble_sort(a))


'''

QAs:
 - Depends on structure or content? - STRUCTURE
 - Internal or External sort alogorithm? - INTERNAL
 - Stable or unstable sort algoritm? - STABLE
 - Best case timecomplexity? - O(N^2) in some cases O(N)
 - Worst case timecomplexity? - O(N^2)
 - Algorithm approch? - SUBTRACT AND CONQUER


'''

