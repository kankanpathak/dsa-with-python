def first_occurrence(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    possible = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            possible = mid
            high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return possible

def last_occurrence(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    possible = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            possible = mid
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return possible

def count_occurrences(nums, target):
    first = first_occurrence(nums, target)

    if first == -1:
        return 0

    last = last_occurrence(nums, target)
    return last - first + 1


nums = [1, 2, 2, 2, 2, 4, 5, 7]

print(count_occurrences(nums, target=2))
print(count_occurrences(nums, target=3))
