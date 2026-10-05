def bubble_sort(nums):
    n = len(nums)
    for i in range(n-2, -1, -1):
        is_swap = False
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True
        if not is_swap:
            break

    return nums


nums = [6, 5, 4, 3, 2, 1]

print(bubble_sort(nums))

# Best Case TC: O(n)
# Average Case TC: O(n²)
# Worst Case TC: O(n²)
# SC: O(1)
