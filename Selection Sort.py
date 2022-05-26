def selection_sort(arr):
         n = len(arr)
         for i in range(n):
             minimum = i
             for j in range(i+1, n):
                 if arr[j]< arr[minimum]:
                     minimum= j
             arr[i], arr[minimum]= arr[minimum], arr[i]


arr = [4,8,100,2,54,70,9]
selection_sort(arr)
print("Sorted Array:" , end=" ")
print(arr)
