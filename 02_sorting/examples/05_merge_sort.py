def merge(left, right):
    result = []
    i  = 0
    j = 0
    n = len(left)
    m = len(right)

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < n:
        while i < n:
            result.append(left[i])
            i += 1

    if j < m:
        while j < m:
            result.append(right[j])
            j += 1

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge(left, right)


nums = [3, 1, 2, 4, 1, 5, 2, 6, 4]

print(merge_sort(nums))

# Best TC - o(n log n)
# Average TC - o(n log n)
# Worst TC - o(n log n)
# SC - o(n)
