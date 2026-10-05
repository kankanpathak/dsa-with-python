def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


nums = [8, 3, 5, 2, 7, 1, 6]

print(selection_sort(nums))

# TC: o(n**2)
# SC: o(1)
