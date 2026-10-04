n = int(input())

arr = []

i = 1

while i < n:
    arr.append(i)

    for j in range(n):
        print(i, j)

    i = i * 2

# TC: o(n log n)
# SC: o(log n)
