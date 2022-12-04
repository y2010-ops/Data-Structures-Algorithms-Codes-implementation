nums =[5,6,2,7,10,9,1]
def bucket_sort(nums):
    j =0
    while j<len(nums):
        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                nums[i-1],nums[i] = nums[i], nums[i-1]
            else:
                continue
        j += 1
    print(nums)

bucket_sort(nums)
