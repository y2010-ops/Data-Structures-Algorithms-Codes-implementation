def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        x = arr[i]
        j = i-1
        while j>=0 and x < arr[j]:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = x

arr = [9,5,1,4,3]
insertion_sort(arr)
print('Sorted Array:', end=" ")
print(arr)