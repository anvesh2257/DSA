# def linear_search(parameter,list1):
#     for index,element in enumerate(list1):
#         if element==parameter:
#             return index
# x=linear_search(8,[9,6,3,2,5,8])
# print(x)
# print(linear_search(5,[2,3,5]))

def binary_search(arr,x):
    low=0
    high=arr[x]-1
    mid=0

    while low<=high:
        mid=(high+low)//2

        if arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            return mid
    return -1

arr=[2,3,4,5,6,7,8,9]
x=7
print(binary_search(arr,x))
