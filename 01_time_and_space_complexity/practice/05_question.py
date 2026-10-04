n = int(input())

i = 1

while i < n:
    for j in range(n):
        print(i, j)
    i = i * 2

# TC: o(n log n)
# SC: o(1)
