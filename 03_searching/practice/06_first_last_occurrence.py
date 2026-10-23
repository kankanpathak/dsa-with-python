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

def first_last_occurrence(nums, target):
    first = lower_bound(nums, target)

    if first == len(nums) or nums[first] != target:
        return [-1, -1]

    last = upper_bound(nums, target) - 1

    return [first, last]

nums = [1, 2, 2, 2, 2, 4, 5, 7]
target = 2

print(first_last_occurrence(nums, target))
print(first_last_occurrence(nums, target=3))
print(first_last_occurrence(nums, target=10))
