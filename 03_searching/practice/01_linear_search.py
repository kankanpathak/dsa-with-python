def linear_search(nums, target):
    n = len(nums)

    for i in range(0, n):
        if nums[i] == target:
            return i

    return -1


print(linear_search([4, 7, 2, 9, 5], 9))


print(linear_search([8, 3, 8, 6], 8))


print(linear_search([1, 2, 3, 4], 10))


print(linear_search([], 5))
