n = int(input())

for i in range(n):
    for j in range(i):
        print(i, j)

# TC: o(n**2)
# SC: o(1)
