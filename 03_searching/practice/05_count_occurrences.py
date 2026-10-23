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

def upper_bound(nums, target):
    n = len(nums)
    ub = n
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub

nums = [1, 2, 2, 2, 2, 4, 5, 7]
target = 2

count = upper_bound(nums, target) - lower_bound(nums, target)

print(count)
