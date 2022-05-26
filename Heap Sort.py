def max_heapify(arr, n, i):

            largest = i
            left = 2*i + 1
            right = 2*i + 2

            if left < n and arr[largest] < arr[left]:
                largest = left
            if right < n and arr[largest] < arr[right]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]

                max_heapify(arr, n, largest)

def heapsort(arr):
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)

arr  = [1,3,8,6,90,48,64,32,3,9]
n = len(arr)

for i in range(n//2 -1, -1,-1):
     max_heapify(arr, n, i)

heapsort(arr)
print("Max heap:", end=" ")
print(arr)

