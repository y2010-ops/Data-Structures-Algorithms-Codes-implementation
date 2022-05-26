def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [5,3,8,6,7,2]

bubble_sort(arr)

print("Sorted Array:", end=" ")
for i in range(len(arr)):
    print(arr[i], end=" ")