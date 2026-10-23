def lower_bound(nums, target):
    n = len(nums)
    lb = n
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb


nums = [1, 1, 1, 2, 3, 3, 5, 6, 7, 7, 7, 9, 12, 12, 13]


print(lower_bound(nums, target=1))

print(lower_bound(nums, target=7))

print(lower_bound(nums, target=8))

print(lower_bound(nums, target=20))
