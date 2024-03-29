def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)

def merge(array, left_index, right_index, middle):

    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # left =[4,8]
    # right=[2,7]

    left_copy_index = 0      #  0,1
    right_copy_index = 0     # 0,1
    sorted_index = left_index    # 0,1,2
    #sorted list=[4,2,]

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):


        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1

        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
merge_sort(array, 0, len(array) -1)
print(array)


# def selectionSort(array, size):
#     # arr=[10,6,3,8,9,4] ||
#     for ind in range(size):
#         # ind=0
#         min_index = ind # 0,1,2,3,4,5
#
#         for j in range(ind + 1, size):
#             # j=1,2,3,4,5
#             # select the minimum element in every iteration
#             if array[j] < array[min_index]:
#                 min_index = j
#         # swapping the elements to sort the array
#         (array[ind], array[min_index]) = (array[min_index], array[ind])
#
#
# arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
# size = len(arr)
# selectionSort(arr, size)
# print('The array after sorting in Ascending Order by selection sort is:')
# print(arr)

def partition(array, start, end):
    # [4,7,2,9,1,5,8] ||[4,1,2,9,7,5,8]||[4,
    # pivot=4
    # low=3->9
    # high=2->2
    pivot = array[start]
    print("pivot = ", pivot)
    low = start + 1  # 1, 2, 3
    print("low = ", low)
    high = end  # 5
    print("high = ", high)

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1
            print("(inside while) high = ", high)

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1
            print("(inside while) low = ", low)

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break
        print("array at the end of loop - ", arr)
#
    array[start], array[high] = array[high], array[start]
    # [5, 1, 2, 9, 7, 4, 8]
    return high


def quick_sort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


array = [29, 99, 27, 41, 66, 28, 44, 78, 87,
         19, 31, 76, 58, 88, 83, 97, 12, 21, 44]

arr = [11, 3, 6, 23, 16, 2]


quick_sort(arr, 0, len(arr) - 1)
print(arr)