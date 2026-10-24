def binary_search(nums, target, low, high):
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


nums = [2, 5, 8, 12, 16, 23, 38, 45, 56]
target = 23
low = 2
high = 6

print(binary_search(nums, target, low, high))

print(binary_search(nums, 45, 2, 6))

print(binary_search(nums, 8, 3, 6))
