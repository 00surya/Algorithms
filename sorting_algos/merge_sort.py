   
# def merge(arr1,arr2):
#     arr = []
#     n1 = len(arr1)
#     n2 = len(arr2)
#     j = 0
#     k = 0
#     for i in range(0,n1+n2):
#         if j >= n1 and k < n2:
#             arr.append(arr2[k])
#             k += 1
#         elif j < n1 and k >= n2:
#             arr.append(arr1[j]) 
#             j += 1 

#         elif j < n1 and k < n2:
#             if arr1[j] < arr2[k]:
#                 arr.append(arr1[j])
#                 j += 1
#             else:
#                 arr.append(arr2[k])
#                 k += 1

#     return arr

def merge_sort(arr):

    if len(arr) <= 1:
        return arr
        
    mid = len(arr)//2
    left  = arr[:mid]
    right = arr[mid:]

    left  = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)



def merge(arr1,arr2):
    arr = []
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    
    while i < n1:
        arr.append(arr1[i])
        i += 1

    while j < n2:
        arr.append(arr2[j])
        j += 1

    return arr

 

# optimized verion

# def merge_sort(arr):

#     if len(arr) <= 1:
#         return arr

#     mid = len(arr)//2
#     left  = arr[:mid]
#     right = arr[mid:]

#     merge_sort(left)
#     merge_sort(right)

#     merge(left,right,arr)



# def merge(arr1,arr2,arr):
#     n1 = len(arr1)
#     n2 = len(arr2)
#     i = j = k = 0


#     while i < n1 and j < n2:
#         if arr1[i] < arr2[j]:
#             arr[k] = arr1[i]
#             i += 1
#         else:
#             arr[k] = arr2[j]
#             j += 1
#         k += 1
        
#     while i < n1:
#         arr[k] = arr1[i]
#         i += 1
#         k += 1

#     while j < n2:
#         arr[k] = arr2[j]
#         j += 1
#         k += 1


 


if __name__ == "__main__":
    # arr1 = [17,21,29,38]
    # arr2 = [4,9,25,32,54,252]
    # print(merge(arr1,arr2))

    arr_list = [
        [1,2,3,4,5,6,7],
        [],
        [7,6,5,4,3,2,1],
        [3]
        ]
    
    for arr in arr_list:
        sorted_arr =merge_sort(arr)
        print(arr)
