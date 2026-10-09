# Unit 02 — Sorting Algorithms

Practical DSA revision notes: focus on each algorithm's pattern, complexity, use cases, and common mistakes—not memorizing every line of code.

## 1. Complexity comparison

| Algorithm | Best TC | Average TC | Worst TC | Auxiliary space | Stable? |
|---|---:|---:|---:|---:|---|
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | Usually no |
| Bubble Sort (basic) | O(n²) | O(n²) | O(n²) | O(1) | Yes |
| Bubble Sort (optimized) | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes, with correct merge handling |
| Quick Sort (first-element pivot version studied) | O(n log n) | O(n log n) | O(n²) | O(log n) average; O(n) worst | Usually no |

Stability means equal-key items keep their original relative order. Stability depends on the implementation. Auxiliary space includes temporary memory and recursion stack space, but not the input array.

## 2. Selection Sort

**Pattern:** Find the minimum in the unsorted portion, then swap it with the first unsorted element. Repeat.

```python
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
```

- TC: O(n²) in best, average, and worst cases. SC: O(1).
- Think of it when simplicity matters or minimizing swaps is useful.
- Common mistake: swapping every time a smaller value is found. Track `min_index` and swap after scanning the unsorted portion.

## 3. Bubble Sort

**Pattern:** Compare adjacent elements and swap if they are out of order. After each pass, the largest remaining element moves to the right.

```python
if nums[j] > nums[j + 1]:
    nums[j], nums[j + 1] = nums[j + 1], nums[j]
```

For optimized Bubble Sort, set `swapped = False` at the beginning of each pass, set it to `True` after a swap, and break if no swap occurred.

- Basic TC: O(n²) in all cases.
- Optimized TC: best O(n), average/worst O(n²). SC: O(1).
- Useful for learning adjacent swaps; optimized version can detect already-sorted input.
- Common mistake: forgetting to reset `swapped = False` for each outer pass.

## 4. Insertion Sort

**Pattern:** Keep a sorted prefix. Save the next item as `key`, shift larger items right, and insert the key into the gap.

```python
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums
```

- TC: best O(n), average/worst O(n²). SC: O(1).
- Useful for small or nearly sorted arrays and for inserting incoming items into sorted order.
- `key` stores the value being inserted. `nums[j + 1] = key` places it after shifting.
- Common mistake: forgetting the `nums[j] > key` condition or checking an index before confirming `j >= 0`.

## 5. Merge Sort

**Pattern: Divide and Conquer**
1. Divide the array into halves recursively.
2. Base case: a list of zero or one item is already sorted.
3. Recursively sort both halves.
4. Merge the two sorted halves.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

`merge(left, right)` assumes both inputs are already sorted:
- Compare the next available element from each side.
- Append the smaller one and advance that pointer.
- When one side ends, append the remaining elements from the other side.

```python
while i < len(left) and j < len(right):
    # compare left[i] and right[j]

while i < len(left):
    # append remaining left items

while j < len(right):
    # append remaining right items
```

- TC: O(n log n) in best, average, and worst cases.
- SC: O(n) auxiliary space for temporary arrays in this implementation; recursion stack is O(log n).
- Use when guaranteed O(n log n) time or stability is important and extra memory is acceptable.
- Common mistake: using `i <= len(left)`. Valid indices end at `len(left) - 1`; use `<`.
- Why O(n log n): O(log n) levels, with O(n) total merge work per level.

## 6. Quick Sort

**Pattern:** Choose a pivot, partition the current range in place, put the pivot in its final position, then recursively sort the left and right ranges.

Our studied version chooses the first element as pivot and uses two pointers. A bounds-safe version of the partition pattern is:

```python
def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high

    while True:
        while i <= high - 1 and nums[i] <= pivot:
            i += 1
        while j >= low + 1 and nums[j] > pivot:
            j -= 1

        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    return j


def quick_sort(nums, low, high):
    if low < high:
        p_index = partition(nums, low, high)
        quick_sort(nums, low, p_index - 1)
        quick_sort(nums, p_index + 1, high)
```

Example:

```python
nums = [4, 1, 7, 6, 3, 2, 8]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
```

- Best/average TC: O(n log n). Worst TC: O(n²) when partitions repeatedly become unbalanced.
- Auxiliary space: O(log n) average recursion stack; O(n) worst. Partition itself uses O(1) extra space.
- Often fast in practice due to in-place partitioning and good cache locality.
- With a first-element pivot, sorted or all-equal input can produce poor partitions for this scheme.
- Common mistake: assuming Quick Sort always splits the array in half.

## 7. When to think of each

| Problem clue | Algorithm to consider | Reason |
|---|---|---|
| Simple; minimize swaps | Selection Sort | One main swap per pass |
| Adjacent comparisons/swaps | Bubble Sort | Largest unsorted item moves right each pass |
| Nearly sorted or items arrive one by one | Insertion Sort | Few shifts when data is nearly sorted |
| Guaranteed worst-case O(n log n) | Merge Sort | Time remains O(n log n) |
| Average-case speed and in-place partitioning | Quick Sort | Often fast in practice; worst case O(n²) |

These are useful clues, not absolute rules. Input size, memory, stability, and implementation details also matter.

## 8. Common mistakes and corrections

- A loop that grows memory is not automatically O(n) space: count how many elements are stored. A list appended to once per logarithmic iteration uses O(log n) space.
- `len(arr)` is a count, not the last index. Use `i < len(arr)`, not `i <= len(arr)`.
- Sequential code blocks are added and the dominant term remains; nested loops are often multiplied. Analyze actual iteration counts.
- Merge Sort divides first and sorts while merging; division itself does not sort.
- Quick Sort is not always O(n log n); unbalanced partitions can cause O(n²).
- Quick Sort partition uses O(1) extra space, but recursive calls require stack space.
- Do not choose based only on best-case complexity. Consider input properties, worst-case guarantees, memory, and stability.
- Do not memorize every line: learn the algorithm pattern, reconstruct code, test edge cases, and debug.

## 9. Testing checklist

Test each implementation with:
- Unsorted input
- Already-sorted input
- Reverse-sorted input
- Duplicate values
- One-element list
- Empty list

Also check whether the function mutates the input or returns a new list.

## 10. Quick revision cheat sheet

```text
Selection Sort:
Find minimum in unsorted portion → swap
TC: O(n²) all cases | SC: O(1)

Bubble Sort:
Compare adjacent items → swap if needed
Basic TC: O(n²) all cases
Optimized best: O(n) | SC: O(1)

Insertion Sort:
Save key → shift larger items → insert key
Best TC: O(n) | Average/Worst: O(n²) | SC: O(1)

Merge Sort:
Divide → recursively sort halves → merge
TC: O(n log n) all cases | SC: O(n) for our implementation

Quick Sort:
Choose pivot → partition → recurse
Best/Average TC: O(n log n) | Worst: O(n²)
Average stack: O(log n) | Worst stack: O(n)
```

## Unit 02 takeaways

1. Understand the algorithm pattern before recalling its code.
2. Time complexity measures how work grows with input size.
3. Auxiliary space includes temporary structures and recursion stack space.
4. Insertion Sort is a strong choice for nearly sorted data.
5. Merge Sort guarantees O(n log n) time; Quick Sort is often fast but can degrade to O(n²).
6. Testing edge cases and debugging mistakes are part of learning.
