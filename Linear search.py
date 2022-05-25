def search(arr, n,  x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1

arr = [2,3,45, 67, 88]
x = 88
n = len(arr)

result = search(arr, n, x)
if (result == -1):
    print("Element is not present in array")
else:
    print("Element present in the array at index ", result)
