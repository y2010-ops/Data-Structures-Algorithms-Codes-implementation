
# QuickSort in Python
# Method 1 - Last element as pivot element
def quicksort(arr):
    length = len(arr)
    if length <=1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for i in arr:
        if i < pivot:
            items_lower.append(i)
        else:
            items_greater.append(i)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

print(quicksort([1,202,3,88,5,69.9,69.92,100,1000]))

# Method 2 - Code for choosing Random element as pivot element

