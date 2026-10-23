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


nums = [1, 3, 5, 6]
target = 2
print(lower_bound(nums, target))


nums = [1, 3, 5, 6]
target = 7
print(lower_bound(nums, target))
