def bubble_sort(nums):
    n = len(nums)
    for i in range(n-2, -1, -1):
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums


nums = [5, 6, 8, 2 ,7, 3]

print(bubble_sort(nums))

# TC: o(n**2)
# SC: o(1)
