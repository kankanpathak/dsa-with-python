def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i-1

        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key

    return nums


nums = [5, 2, 8, 1, 6, 3, 7, 4]

print(insertion_sort(nums))

