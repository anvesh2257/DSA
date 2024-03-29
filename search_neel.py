# l=[3,5,2,9,6]
#
# def linear_search(target,list1):
#     for index,element in enumerate(list1):
#         if element==target:
#             print("the element is in position: ",index)
# linear_search(5,[5,6,93,4,12,6,3])
# linear_search(9,[6,2,3,6,9,45,])
# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1

def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# If x is greater, ignore left half
		if arr[mid] < x:
			low = mid + 1

		# If x is smaller, ignore right half
		elif arr[mid] > x:
			high = mid - 1

		# means x is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
