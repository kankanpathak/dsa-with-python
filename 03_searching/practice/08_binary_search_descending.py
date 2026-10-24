def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


nums = [90, 75, 60, 45, 30, 15]

print(binary_search(nums, target=45))
print(binary_search(nums, target=50))
