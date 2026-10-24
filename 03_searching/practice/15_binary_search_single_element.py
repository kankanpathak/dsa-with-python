def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


nums = [42]

print(binary_search(nums, target=42))
print(binary_search(nums, target=10))
