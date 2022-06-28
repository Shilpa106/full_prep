# # Python3 program for Bubble Sort Algorithm Implementation
# def bubbleSort(arr):
	
# 	n = len(arr)

# 	# For loop to traverse through all
# 	# element in an array
# 	for i in range(n):
        

# 		for j in range(0, n - i - 1):
# 			print(i,j)
# 			# Range of the array is from 0 to n-i-1
# 			# Swap the elements if the element found
# 			#is greater than the adjacent element
# 			if arr[j] > arr[j + 1]:
# 				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				
# # Driver code

# # Example to test the above code
# arr = [ 2, 1, 10, 23 ]

# bubbleSort(arr)

# print("Sorted array is:")
# for i in range(len(arr)):
# 	print("%d" % arr[i])



# # Selection Sort

# def selectionSort(array, size):
#     for s in range(size):
#         min_idx=s
#         for i in range(s+1,size):
#             if array[i]<array[min_idx]:
#                 min_idx = i 
#         (array[s],array[min_idx])=(array[min_idx],array[s])

# data=[7,2,1,6]
# size=len(data)
# selectionSort(data,size)
# print(data)


# insertion sort
# Creating a function for insertion sort algorithm
def insertion_sort(list1):

		# Outer loop to traverse on len(list1)
		for i in range(1, len(list1)):

			a = list1[i]

			# Move elements of list1[0 to i-1],
			# which are greater to one position
			# ahead of their current position
			j = i - 1
		
			while j >= 0 and a < list1[j]:
				list1[j + 1] = list1[j]
				j -= 1
				
			list1[j + 1] = a
			
		return list1
			
# Driver code
list1 = [ 7, 2, 1, 6 ]
print("The unsorted list is:", list1)
print("The sorted new list is:", insertion_sort(list1))

