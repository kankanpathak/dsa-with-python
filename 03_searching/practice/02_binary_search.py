def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print(binary_search([3, 8, 12, 17, 21, 29, 34, 40, 46], 29))

print(binary_search([3, 8, 12, 17, 21, 29, 34, 40, 46], 3))

print(binary_search([3, 8, 12, 17, 21, 29, 34, 40, 46], 46))

print(binary_search([3, 8, 12, 17, 21, 29, 34, 40, 46], 25))
