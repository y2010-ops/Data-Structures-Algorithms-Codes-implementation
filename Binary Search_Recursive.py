def binary_search(arr, l, u, x):
    if u>=1:
        mid = l+u//2 +l
        if arr[mid]==x:
            return mid
        elif arr[mid]> x:
             return binary_search(arr, 0, mid-1, x)
        else:
            return binary_search(arr, mid +1, u, x)
    return -1

arr = [1,2,3,4,5,8,10, 50,61, 100,121]

x = 4

# calling function
result = binary_search(arr, 0, len(arr)-1, x)

if result == -1:
    print("Value not found")
else:
    print("Value Found at index: ", result)


