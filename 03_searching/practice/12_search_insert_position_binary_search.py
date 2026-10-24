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

    return low


nums = [1, 3, 5, 6]

print(binary_search(nums, target=5))
print(binary_search(nums, target=2))
print(binary_search(nums, target=7))
print(binary_search(nums, target=0))
