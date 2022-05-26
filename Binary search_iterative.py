# iterative Method
def binary_search(arr, l, u, x):
    l = 0
    u = len(arr)-1
    while l <= u:
        mid = (l+u)//2
        if (arr[mid] == x):
            return mid
        elif (x< arr[mid]):
            u = mid - 1
        else:
            l = mid+1

    return -1


arr = [1,2,3,4,5,8,10, 50,61, 100,121]

x = 5

# calling function
result = binary_search(arr, 0, len(arr)-1, x)

if result == -1:
    print("Value not found")
else:
    print("Value Found at index: ", result)


