
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key =arr[i]

        # Move elements of arr[0...i-1], that are greater than key, to one position ahead of their current position

        j=i-1
        print("1",j)
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            print("2",j)
        print("3",j+1)
        arr[j+1]=key


# Driver code to test above
arr=[12,11,13,5,6]
insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])


# Time Complexity:O(n2)


