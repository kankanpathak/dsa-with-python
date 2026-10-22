def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low+high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid -1

    return -1


print(binary_search([2, 5, 8, 12, 16, 23, 38], 5))

print(binary_search([2, 5, 8, 12, 16, 23, 38], 38))

print(binary_search([2, 5, 8, 12, 16, 23, 38], 10))

print(binary_search([], 5))


# TC - o(log n)
# SC - o(1)
