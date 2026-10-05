# Unit 01 — Time & Space Complexity

> Understanding how an algorithm's time and memory usage grow as the input size increases.

---

## 1. Time Complexity

Time complexity describes how the amount of work performed by an algorithm grows with the input size `n`.

We focus on **growth**, not the actual time in seconds.

### Example

```python
for i in range(n):
    print(i)
```

The loop runs `n` times.

**Time Complexity: `O(n)`**

---

## 2. Space Complexity

Space complexity describes how much memory an algorithm needs as the input size grows.

When discussing **auxiliary space**, we focus on the extra memory created by the algorithm and normally exclude the input itself.

### Example — O(1) Space

```python
for i in range(n):
    print(i)
```

The loop runs `n` times, but it does not create a growing data structure.

**Time: `O(n)`**  
**Auxiliary Space: `O(1)`**

> A loop running `n` times does NOT automatically mean `O(n)` space.

---

## 3. Big-O Notation

Big-O describes an upper bound on how an algorithm's work grows.

Common complexities:

| Complexity | Common Pattern |
|---|---|
| `O(1)` | Constant work |
| `O(log n)` | Repeated doubling/halving |
| `O(n)` | One linear pass |
| `O(n log n)` | Linear work repeated logarithmically |
| `O(n²)` | Two nested linear loops |
| `O(n³)` | Three nested linear loops |
| `O(2ⁿ)` | Exponential growth |
| `O(n!)` | Factorial growth |

### General growth order

```text
O(1)
  ↓
O(log n)
  ↓
O(n)
  ↓
O(n log n)
  ↓
O(n²)
  ↓
O(n³)
  ↓
O(2ⁿ)
  ↓
O(n!)
```

As `n` becomes very large, the lower levels generally become much more expensive.

---

## 4. Big-O, Theta and Omega

These notations describe different types of bounds:

- **Big-O — `O(f(n))`** → upper bound
- **Theta — `Θ(f(n))`** → tight bound
- **Omega — `Ω(f(n))`** → lower bound

Do not automatically think that `O`, `Θ`, and `Ω` mean worst case, average case, and best case. They describe bounds.

Big-O is commonly used when discussing an algorithm's worst-case growth.

---

# 5. The Most Important Rule: ADD vs MULTIPLY

## Sequential Code → ADD

When blocks execute one after another:

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

Complexity:

```text
O(n) + O(n)
= O(2n)
= O(n)
```

### Rule

> **Sequential blocks → ADD their complexities.**

Example:

```text
O(n) + O(n²)
= O(n + n²)
= O(n²)
```

---

## Nested Code → MULTIPLY

When one loop is inside another:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

The outer loop runs `n` times.

For every outer iteration, the inner loop runs `n` times.

```text
O(n) × O(n)
= O(n²)
```

### Rule

> **Nested loops → MULTIPLY their complexities.**

### Easy memory trick

> **Next to each other → ADD**  
> **Inside each other → MULTIPLY**

---

# 6. Triangular Loops

Consider:

```python
for i in range(n):
    for j in range(i):
        print(i, j)
```

The inner loop runs:

```text
0 + 1 + 2 + ... + (n - 1)
```

Using the sum formula:

```text
n(n - 1) / 2
```

Ignoring constants and lower-order terms:

```text
O(n²)
```

### Important lesson

Do not simply say "inner loop is `n`" for every nested loop.

Sometimes you need to calculate the total number of iterations.

---

# 7. Logarithmic Complexity — O(log n)

Consider:

```python
i = 1

while i < n:
    print(i)
    i = i * 2
```

The values are:

```text
1 → 2 → 4 → 8 → 16 → 32 → ...
```

The value doubles every iteration.

Therefore:

```text
Time Complexity = O(log n)
```

### Common patterns

```python
i *= 2
```

or

```python
i //= 2
```

usually indicate:

```text
O(log n)
```

### Contrast

```text
i += 1   → usually O(n)
i *= 2   → O(log n)
i //= 2  → O(log n)
```

---

# 8. O(n log n)

Consider:

```python
i = 1

while i < n:
    for j in range(n):
        print(i, j)

    i = i * 2
```

Outer loop:

```text
O(log n)
```

Inner loop:

```text
O(n)
```

The inner loop is nested inside the outer loop:

```text
O(log n) × O(n)
= O(n log n)
```

---

# 9. Dropping Constants

In Big-O, constant multipliers are ignored.

```text
O(2n)    → O(n)
O(5n)    → O(n)
O(100n)  → O(n)

O(10n²)  → O(n²)
```

We care about how the function grows as `n` becomes large.

---

# 10. Dropping Lower-Order Terms

Keep the dominant/highest-growing term.

```text
O(n² + n)
→ O(n²)
```

```text
O(n³ + n² + n + 10)
→ O(n³)
```

### Rule

> **Keep the fastest-growing term.**

---

# 11. Space Complexity Patterns

## O(1) Space

```python
n = int(input())

for i in range(n):
    print(i)
```

Only a fixed number of variables are used.

```text
SC = O(1)
```

---

## O(n) Space

```python
arr = []

for i in range(n):
    arr.append(i)
```

The list contains approximately `n` elements.

```text
SC = O(n)
```

---

## O(log n) Space

A useful example from our practice:

```python
arr = []
i = 1

while i < n:
    arr.append(i)
    i *= 2
```

The values appended are:

```text
1, 2, 4, 8, 16, ...
```

The loop runs `O(log n)` times, so the list grows to `O(log n)` elements.

```text
SC = O(log n)
```

### Important lesson

> Growing memory does NOT automatically mean `O(n)`.

You must determine **how quickly the memory grows**.

---

# 12. Auxiliary Space

Auxiliary space means the **extra memory used by the algorithm**, excluding the input data itself.

Example:

```python
def process(arr):
    total = 0

    for x in arr:
        total += x

    return total
```

`arr` is input.

We only use a few extra variables.

```text
Auxiliary Space = O(1)
```

---

# 13. Python Operation Complexities

These are the important ones for DSA.

| Python Operation | Typical Complexity |
|---|---:|
| `arr[i]` | `O(1)` |
| `arr.append(x)` | `O(1)` amortized |
| `arr.pop()` | `O(1)` |
| `arr.insert(0, x)` | `O(n)` |
| `arr.pop(0)` | `O(n)` |
| `x in list` | `O(n)` |
| `x in set` | `O(1)` average |
| `x in dict` | `O(1)` average |
| `len(arr)` | `O(1)` |
| `arr.sort()` | `O(n log n)` |

### Important detail

`append()` is typically/amortized `O(1)`, but an individual append can occasionally take `O(n)` when the list needs to resize.

---

# 14. TLE — Time Limit Exceeded

In competitive programming, a program must finish within a given time limit.

An algorithm can be logically correct but still too slow.

For example:

```text
n = 100
```

An `O(n²)` algorithm may be fine.

But for:

```text
n = 1,000,000
```

`O(n²)` is usually far too slow.

### Important lesson

> Always look at the input constraints before choosing an algorithm.

A rough competitive-programming rule of thumb sometimes uses around `10^8` simple operations per second, but this is only an approximation, not a law.

---

# 15. How to Analyze Time Complexity

When given code, use this process:

```text
1. Identify the loops.
       ↓
2. Determine how many times each loop runs.
       ↓
3. Are the blocks sequential or nested?
       ↓
4. Sequential → ADD
   Nested → MULTIPLY
       ↓
5. Simplify the expression.
       ↓
6. Drop constants.
       ↓
7. Drop lower-order terms.
       ↓
8. Write the final Big-O.
```

---

# 16. How to Analyze Space Complexity

Ask:

```text
1. What extra variables/data structures are created?
       ↓
2. Does their size grow with n?
       ↓
3. If yes, how fast does it grow?
       ↓
4. Determine auxiliary space.
```

---

# 17. Common Mistakes We Corrected

### Mistake 1

> "A loop runs `n` times, so space is `O(n)`."

❌ Wrong.

A loop can run `n` times while using constant extra memory.

```text
Time = O(n)
Space = O(1)
```

---

### Mistake 2

> "Every nested loop is automatically `O(n²)`."

❌ Not always.

Example:

```python
i = 1

while i < n:
    for j in range(n):
        ...
    i *= 2
```

This is:

```text
O(log n) × O(n)
= O(n log n)
```

---

### Mistake 3

> "If memory grows, it must be O(n)."

❌ Not necessarily.

If memory grows once per logarithmic iteration:

```text
Space = O(log n)
```

---

### Mistake 4

For:

```python
for i in range(n):
    for j in range(i):
        ...
```

Don't treat the inner loop as always `n`.

The total work is:

```text
0 + 1 + 2 + ... + (n - 1)
= n(n - 1)/2
= O(n²)
```

---

# 18. Practice Patterns We Learned

### Pattern 1

```python
for i in range(n):
    ...
```

```text
TC = O(n)
SC = O(1)
```

### Pattern 2

```python
for i in range(n):
    for j in range(n):
        ...
```

```text
TC = O(n²)
SC = O(1)
```

### Pattern 3

```python
i = 1

while i < n:
    ...
    i *= 2
```

```text
TC = O(log n)
SC = O(1)
```

### Pattern 4

```python
while i < n:
    for j in range(n):
        ...
    i *= 2
```

```text
TC = O(n log n)
```

### Pattern 5

```python
arr = []

for i in range(n):
    arr.append(i)
```

```text
TC = O(n)
SC = O(n)
```

---

# 19. Quick Revision Cheat Sheet

```text
Sequential → ADD
Nested → MULTIPLY

i += 1 → O(n)
i *= 2 → O(log n)
i //= 2 → O(log n)

One loop → O(n)
Two nested loops → O(n²)
n inside log loop → O(n log n)

Drop constants:
O(5n) → O(n)

Drop lower terms:
O(n² + n) → O(n²)

No growing extra memory → O(1)

List grows to n elements → O(n) space

Memory grows once per log iteration → O(log n) space
```

---

# 20. Unit 01 Final Takeaway

The goal of complexity analysis is **not to memorize answers**.

The goal is to look at an algorithm and reason:

> **How many times does the work happen, and how much extra memory grows as `n` grows?**

The two rules to remember above everything else:

> **Sequential → ADD**  
> **Nested → MULTIPLY**

And:

> **Time asks: "How much work?"**  
> **Space asks: "How much extra memory?"**

---

## Practice completed in Unit 01

We practiced:

- Linear loop — `O(n)`
- Nested loops — `O(n²)`
- Triangular nested loops — `O(n²)`
- Doubling loop — `O(log n)`
- Nested `n` loop inside logarithmic loop — `O(n log n)`
- Sequential loops — `O(n)`
- Growing list — `O(n)` space
- Growing list inside logarithmic loop — `O(log n)` space
