def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    possible = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            possible = mid
            high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return possible


nums = [2, 4, 4, 4, 4, 7, 9]

print(binary_search(nums, target=4))
print(binary_search(nums, target=5))
