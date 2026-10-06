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


nums = [3, 5, 6, 9, 2, 10, 1]

print(insertion_sort(nums))

# Best Case TC: O(n)
# Average Case TC: O(n²)
# Worst Case TC: O(n²)
# SC: O(1)
