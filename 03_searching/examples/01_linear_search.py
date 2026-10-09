def linear_search(nums, target):
    n = len(nums)

    for i in range(0, n):
        if nums[i]  == target:
            return i

    return -1


nums = [5, 3, 9, 8, 1, 6, 4, -10, -100]
target = 4

print(linear_search(nums, target))

# Best TC - o(1)
# Average TC - o(n)
# Worst TC - o(n)
# SC - o(1)

